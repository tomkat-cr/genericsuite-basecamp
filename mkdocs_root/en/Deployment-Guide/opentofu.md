# OpenTofu (Infrastructure as Code)

GenericSuite ships an [OpenTofu](https://opentofu.org/) (Terraform-compatible) implementation of every AWS deployment that was previously performed with CloudFormation templates and raw AWS CLI calls. It gives the DevOps, security, and infrastructure teams a single Infrastructure-as-Code (IaC) toolchain, with remote state, drift detection, and reviewable plans.

The OpenTofu path lives alongside the existing scripts — the CloudFormation templates and CLI deploy scripts are **not** removed or modified. You can adopt OpenTofu stack by stack, and run both worlds in the same AWS account.

- Frontend stacks: `genericsuite-fe-scripts/scripts/aws_tf/`
- Backend stacks: `genericsuite-be-scripts/scripts/aws_tf/`

## Why OpenTofu

- **One toolchain for every team.** The same `plan`/`apply` workflow covers frontend hosting, backend compute, databases, secrets, and DNS.
- **Reviewable changes.** `tofu plan` shows exactly what will change before anything is applied — no more "delete the stack and retry" recovery flows.
- **Remote, locked state.** State is stored in S3 with native locking, so the whole team shares one source of truth.
- **Security hardening.** The conversion took the opportunity to fix long-standing issues (see [Security improvements](#security-improvements)).

## Coexistence with CloudFormation

Resource names match the current conventions (`{app}-{stage}-secrets`, `{app}_{stage}_{table}`, `{lambda}-{stage}`, `genericsuite-key`, etc.) so the OpenTofu resources are recognizable next to the legacy ones. The existing CloudFormation stacks are left untouched.

For stacks whose resource names are **globally or account-unique** (the EC2 + ALB stack's ALB, Auto Scaling Group, target group, and launch template; the KMS `alias/genericsuite-key`), OpenTofu and a still-live CloudFormation stack of the same name cannot both own the resource at once. Delete the CloudFormation stack first, or import the existing resource into OpenTofu state (see [Migration notes](#migration-notes)). Stacks that create net-new resources (secrets, DynamoDB tables, ECR repositories, the chatbot S3 bucket) coexist without conflict.

## Prerequisites

- **OpenTofu ≥ 1.10** — required for S3-native state locking.
  ```bash
  brew install opentofu     # macOS
  tofu version              # confirm >= 1.10
  ```
- **AWS CLI** configured with credentials for the target account (`aws sts get-caller-identity`).
- **`jq`** (used by the secrets variable builder).
- A consuming application with a stage-specific `.env` file (the same `.env` the legacy scripts read). Run the wrapper from the application's root directory.

## State management

Each application gets its own state bucket:

- **Bucket:** `{app_name_lowercase}-tf-state-{aws_account_id}`
- **Key:** `{stage}/{stack}.tfstate` (e.g. `dev/frontend.tfstate`, `prod/dynamodb.tfstate`)
- Versioned, SSE-encrypted, all public access blocked, and locked via S3-native locking (`use_lockfile` — no DynamoDB lock table needed).

The bucket is created automatically the first time you run the wrapper (it calls `bootstrap-tf-state.sh` before `tofu init`). You never edit backend configuration by hand — the wrapper injects it via `tofu init -backend-config=...`.

## Backend deployments

All backend stacks are driven by one wrapper:

```bash
bash node_modules/genericsuite-be-scripts/scripts/aws_tf/run-tf-deployment.sh ACTION STAGE STACK
```

- **ACTION:** `init` | `validate` | `plan` | `apply` | `destroy` | `output`
- **STAGE:** `dev` | `qa` | `staging` | `demo` | `prod`
- **STACK:** one of `kms`, `secrets`, `s3`, `dynamodb`, `ecr`, `domain`, `ec2`, `lambda`

Set `CICD_MODE=1` for non-interactive runs (adds `-auto-approve` on `apply`/`destroy`).

### Stacks

| Stack | Replaces | Creates |
|---|---|---|
| `kms` | `cf-template-kms-key.yml` | KMS key + `alias/genericsuite-key` + key-admin/use/attach/ASG IAM roles |
| `secrets` | `aws_secrets_manager.sh` + `cf-template-secrets.yml` | `{app}-{stage}-secrets` (KMS-encrypted) and `{app}-{stage}-envs` |
| `s3` | `create_s3_bucket.sh` / `create_chatbot_s3_bucket.sh` | Chatbot-attachments S3 bucket (private) + policy |
| `dynamodb` | `run-dynamodb-deploy.sh` | DynamoDB tables from the JSON config (`PAY_PER_REQUEST`, PITR) |
| `ecr` | `run-fastapi-ecr-creation.sh` / `clean_ecr_images.sh` | Lambda + EC2 ECR repositories with scan-on-push and retention |
| `domain` | `cf-template-ec2-domain.yml` | ACM certificate with native DNS validation + Route53 records |
| `ec2` | `cf-template-ec2-elb.yml` | VPC, subnets, IAM, security groups, launch template, ASG, ALB, HTTPS listener, Route53 alias |
| `lambda` | `template-sam.yml` (SAM) | Lambda (container or zip) + API Gateway REST API + optional custom domain |

### Required `.env` variables

Common (all backend stacks): `APP_NAME`, `AWS_REGION`, `CLOUD_PROVIDER=aws`, and optionally `AWS_ACCOUNT_ID` (auto-detected via STS if unset) and `KMS_KEY_ALIAS` (defaults to `genericsuite-key`).

Per stack, additionally:

- **secrets** — the core/AI/app secret and env variables (same lists as `aws_secrets_manager.sh`), plus `APP_DOMAIN_NAME`. Secret values travel only as sensitive `TF_VAR_*` environment variables — they are never written to `.tfvars` files on disk.
- **s3** — `AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_{STAGE}`.
- **dynamodb** — `GIT_SUBMODULE_LOCAL_PATH` (the JSON config directory; its `frontend/` files, merged with `backend/`, define the tables).
- **ecr / ec2 / lambda** — `AWS_LAMBDA_FUNCTION_NAME` (the base resource name), and `ECR_DOCKER_IMAGE_TAG` for the image to deploy. The `ec2` stack additionally reads the `domain` stack's outputs (certificate ARN, hosted zone) via remote state; the `lambda` stack uses the default `execute-api` URL unless you pass a custom domain and certificate explicitly.

### Recommended apply order

```bash
BE=node_modules/genericsuite-be-scripts/scripts/aws_tf/run-tf-deployment.sh

CICD_MODE=1 bash $BE apply qa kms       # once per account (skip if alias/genericsuite-key exists)
CICD_MODE=1 bash $BE apply qa secrets
CICD_MODE=1 bash $BE apply qa s3
CICD_MODE=1 bash $BE apply qa dynamodb
CICD_MODE=1 bash $BE apply qa ecr
CICD_MODE=1 bash $BE apply qa domain    # EC2/ALB path only
CICD_MODE=1 bash $BE apply qa ec2       # or: apply qa lambda
```

`secrets` reads the existing KMS key by alias, so if `alias/genericsuite-key` already exists in the account you can run `kms` as `plan` only and keep the existing key. Docker image build and push to ECR remain in the existing bash scripts (that is application packaging, not infrastructure); point them at the `ecr` stack's repository output.

### Retrieving outputs

```bash
bash $BE output qa lambda      # endpoint_url, function_arn, custom_domain_url
bash $BE output qa ec2         # load_balancer_dns_name, app_url
```

## Frontend deployments

The frontend has its own wrapper plus a full deploy pipeline:

```bash
# Infra only (S3 + CloudFront):
bash node_modules/genericsuite-fe-scripts/scripts/aws_tf/run-tf-deployment.sh apply STAGE frontend

# Full pipeline (infra + build + upload + cache invalidation):
bash node_modules/genericsuite-fe-scripts/scripts/aws_tf/aws_tf_deploy_to_s3.sh STAGE [VARIABLE_TYPE]
```

`aws_tf_deploy_to_s3.sh` is the OpenTofu counterpart of the legacy `aws_deploy_to_s3.sh` (which stays in place). It applies the `frontend` stack, reads the bucket and distribution from its outputs, builds the app with the configured bundler (`vite`, `webpack`, or `react-app-rewired`), runs `aws s3 sync`, and invalidates the CloudFront cache.

Required `.env`: `AWS_S3_BUCKET_NAME_{TYPE}` (a `[STAGE]` token is substituted), `APP_{TYPE}_URL`, `AWS_REGION`, and optionally `AWS_SSL_CERTIFICATE_ARN[_{TYPE}]` (`TYPE` defaults to `FE`). If no certificate ARN is provided and the app URL is set, the stack looks the certificate up in `us-east-1` by domain.

### What changed vs. the legacy frontend script

- **Origin Access Control (OAC)** instead of the deprecated Origin Access Identity (OAI); the S3 bucket is fully private (all public-access-block flags on), served only through CloudFront.
- `ViewerProtocolPolicy` is now **redirect-to-https**, and the minimum TLS version is **TLSv1.2_2021**.
- **SPA routing** — S3 403/404 responses are mapped to `/index.html` (200).
- No more public bucket ACL grants; `aws s3 sync` runs without ACL flags.

## Security improvements

The conversion hardened several areas relative to the CloudFormation/CLI originals:

- CloudFront uses OAC with a private bucket (no OAI, no public ACLs); TLS floor raised to TLSv1.2_2021; HTTP redirected to HTTPS.
- Secrets are passed as sensitive OpenTofu variables and stored in Secrets Manager — never as CloudFormation stack parameters (which are visible in the console and CloudTrail).
- IAM policies are scoped down — for example, `secretsmanager:GetSecretValue` is limited to the two application secret ARNs rather than `*`.
- Native ACM DNS validation replaces the two Lambda-backed custom resources and the placeholder A-record in the old EC2 domain template.
- The EC2 AMI is resolved from the Amazon Linux 2 SSM public parameter instead of a hardcoded, deprecation-prone AMI ID; both ALB subnets are route-table-associated; SSH ingress is opened only when a CIDR is explicitly provided.

## Migration notes

- **Run both paths side by side.** Because resource names match, you can validate the OpenTofu stacks with `plan` against a live environment before cutting over.
- **Importing existing resources.** For account-unique resources you want OpenTofu to manage without recreating, import them into state, e.g.:
  ```bash
  cd node_modules/genericsuite-be-scripts/scripts/aws_tf/stacks/secrets
  tofu import module.secrets.aws_secretsmanager_secret.encrypted \
    arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:myapp-qa-secrets
  ```
- **KMS alias.** If `alias/genericsuite-key` already exists (from a prior CloudFormation deploy), keep it — run the `kms` stack as `plan` only, and the `secrets`/`ec2`/`lambda` stacks will reference the existing key by alias.
- **EC2/ALB cutover.** Delete the legacy CloudFormation EC2 stack (or import its ALB/ASG/target-group/launch-template) before applying the `ec2` stack, since those names are account-unique.

## Not yet covered

These deployments are not part of the OpenTofu path yet and remain on their existing tooling:

- RDS (PostgreSQL / MySQL) — `genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh`.
- Chalice-native deploys — `genericsuite-be-scripts/scripts/aws/run_aws.sh`.
- LocalStack testing for the OpenTofu stacks (the CloudFormation processor's LocalStack mode is unchanged).
