# OpenTofu (Infraestructura como Código)

GenericSuite trae una implementación de [OpenTofu] (compatible con Terraform) de cada implementación de AWS que anteriormente se realizaba con plantillas de CloudFormation y llamadas de AWS CLI en crudo. Proporciona a los equipos de DevOps, seguridad e infraestructura una única cadena de herramientas de Infraestructura como Código (IaC), con estado remoto, detección de deriva y planes revisables.

La ruta de OpenTofu convive junto a los scripts existentes — las plantillas de CloudFormation y los scripts de despliegue CLI no se eliminan ni se modifican. Puede adoptar la pila OpenTofu pila por pila, y ejecutar ambos enfoques en la misma cuenta de AWS.

- Pila de Frontend: `genericsuite-fe-scripts/scripts/aws_tf/`
- Pila de Backend: `genericsuite-be-scripts/scripts/aws_tf/`

## Por qué OpenTofu

- **Una cadena de herramientas para todos los equipos.** El mismo flujo de trabajo de `plan`/`apply` cubre hosting del frontend, cómputo del backend, bases de datos, secretos y DNS.
- **Cambios revisables.** `tofu plan` muestra exactamente qué cambiará antes de que se aplique algo — ya no hay flujos de recuperación de “eliminar la pila y reintentar”.
- **Estado remoto y bloqueado.** El estado se almacena en S3 con bloqueo nativo, de modo que todo el equipo comparte una única fuente de verdad.
- **Fortalecimiento de la seguridad.** La conversión aprovechó la oportunidad para corregir problemas antiguos (véase [Mejoras de seguridad](#mejoras-de-seguridad)).

## Coexistencia con CloudFormation

Los nombres de recursos coinciden con las convenciones actuales (`{app}-{stage}-secrets`, `{app}_{stage}_{table}`, `{lambda}-{stage}`, `genericsuite-key`, etc.), por lo que los recursos de OpenTofu son reconocibles junto a los heredados. Las pilas de CloudFormation existentes quedan intactas.

Para pilas cuyos nombres de recurso son **globalmente únicos o únicos por cuenta** (el ALB de la pila EC2 + ALB, Auto Scaling Group, target group y launch template; el alias de KMS `alias/genericsuite-key`), OpenTofu y una pila de CloudFormation aún viva con el mismo nombre no pueden poseer el recurso al mismo tiempo. Elimina primero la pila de CloudFormation, o importa el recurso existente al estado de OpenTofu (ver [Notas de migración](#notas-de-migracion)). Las pilas que crean recursos netos nuevos (secretos, tablas de DynamoDB, repositorios ECR, el bucket S3 del chatbot) coexisten sin conflicto.

## Requisitos previos

- **OpenTofu ≥ 1.10** — requerido para el bloqueo de estado nativo de S3.
  ```bash
  brew install opentofu     # macOS
  tofu version              # confirmar >= 1.10
  ```
- **AWS CLI** configurado con credenciales para la cuenta objetivo (`aws sts get-caller-identity`).
- **`jq`** (utilizado por el constructor de variables de secretos).
- Una aplicación consumidora con un archivo `.env` por etapa (el mismo `.env` que leen los scripts heredados). Ejecute el wrapper desde el directorio raíz de la aplicación.

## Gestión del estado

Cada aplicación tiene su propio bucket de estado:

- **Bucket:** `{app_name_lowercase}-tf-state-{aws_account_id}`
- **Key:** `{stage}/{stack}.tfstate` (p. ej. `dev/frontend.tfstate`, `prod/dynamodb.tfstate`)
- Versionado, cifrado SSE, todo acceso público bloqueado y bloqueo mediante bloqueo nativo de S3 (`use_lockfile` — no es necesario una tabla de bloqueo de DynamoDB).

El bucket se crea automáticamente la primera vez que ejecuta el wrapper (llama a `bootstrap-tf-state.sh` antes de `tofu init`). Nunca edita la configuración del backend a mano — el wrapper la inyecta mediante `tofu init -backend-config=...`.

## Despliegues de backend

Todas las pilas de backend se gestionan con un único wrapper:

```bash
bash node_modules/genericsuite-be-scripts/scripts/aws_tf/run-tf-deployment.sh ACTION STAGE STACK
```

- **ACCIÓN:** `init` | `validate` | `plan` | `apply` | `destroy` | `output`
- **ETAPA:** `dev` | `qa` | `staging` | `demo` | `prod`
- **PILE:** una de `kms`, `secrets`, `s3`, `dynamodb`, `ecr`, `domain`, `ec2`, `lambda`

Establezca `CICD_MODE=1` para ejecuciones no interactivas (agrega `-auto-approve` en `apply`/`destroy`).

### Pilas

| Pila | Reemplaza | Crea |
|---|---|---|
| `kms` | `cf-template-kms-key.yml` | Clave KMS + `alias/genericsuite-key` + roles IAM key-admin/use/attach/ASG |
| `secrets` | `aws_secrets_manager.sh` + `cf-template-secrets.yml` | `{app}-{stage}-secrets` (KMS-encriptado) y `{app}-{stage}-envs` |
| `s3` | `create_s3_bucket.sh` / `create_chatbot_s3_bucket.sh` | Bucket de adjuntos del chatbot S3 (privado) + política |
| `dynamodb` | `run-dynamodb-deploy.sh` | Tablas DynamoDB desde la configuración JSON (`PAY_PER_REQUEST`, PITR) |
| `ecr` | `run-fastapi-ecr-creation.sh` / `clean_ecr_images.sh` | Repositorios ECR de Lambda + EC2 con escaneo on-push y retención |
| `domain` | `cf-template-ec2-domain.yml` | Certificado ACM con validación DNS nativa + registros de Route53 |
| `ec2` | `cf-template-ec2-elb.yml` | VPC, subredes, IAM, grupos de seguridad, plantilla de lanzamiento, ASG, ALB, escuchador HTTPS, alias de Route53 |
| `lambda` | `template-sam.yml` (SAM) | Lambda (contenedor o zip) + API Gateway REST API + dominio personalizado opcional |

### Variables `.env` requeridas

Comunes (todas las pilas de backend): `APP_NAME`, `AWS_REGION`, `CLOUD_PROVIDER=aws`, y opcionalmente `AWS_ACCOUNT_ID` (detección automática vía STS si no se establece) y `KMS_KEY_ALIAS` (predeterminado a `genericsuite-key`).

Por pila, adicionalmente:

- **secrets** — el secreto central/AI/app y variables de entorno (las mismas listas que `aws_secrets_manager.sh`), además `APP_DOMAIN_NAME`. Los valores de secreto viajan solo como variables de entorno sensibles `TF_VAR_*` — nunca se escriben en archivos `.tfvars` en disco.
- **s3** — `AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_{STAGE}`.
- **dynamodb** — `GIT_SUBMODULE_LOCAL_PATH` (el directorio de configuración JSON; sus archivos `frontend/`, fusionados con `backend/`, definen las tablas).
- **ecr / ec2 / lambda** — `AWS_LAMBDA_FUNCTION_NAME` (el nombre base del recurso), y `ECR_DOCKER_IMAGE_TAG` para la imagen a desplegar. La pila `ec2` lee adicionalmente las salidas de la pila `domain` (ARN del certificado, zona hospedada) vía estado remoto; la pila `lambda` usa la URL por defecto `execute-api` a menos que des un dominio personalizado y certificado explícitamente.

### Orden recomendado de aplicación

```bash
BE=node_modules/genericsuite-be-scripts/scripts/aws_tf/run-tf-deployment.sh

CICD_MODE=1 bash $BE apply qa kms       # una vez por cuenta (omitir si existe alias/genericsuite-key)
CICD_MODE=1 bash $BE apply qa secrets
CICD_MODE=1 bash $BE apply qa s3
CICD_MODE=1 bash $BE apply qa dynamodb
CICD_MODE=1 bash $BE apply qa ecr
CICD_MODE=1 bash $BE apply qa domain    # ruta EC2/ALB
CICD_MODE=1 bash $BE apply qa ec2       # o: aplicar qa lambda
```

`secrets` lee la clave KMS existente por alias, así que si `alias/genericsuite-key` ya existe en la cuenta puedes ejecutar `kms` en modo plan solamente y mantener la clave existente. La construcción de imágenes Docker y el push a ECR permanecen en los scripts bash existentes (eso es empaquetado de la aplicación, no infraestructura); dirígelos al output del repositorio de la pila `ecr`.

### Recuperación de salidas

```bash
bash $BE output qa lambda      # endpoint_url, function_arn, custom_domain_url
bash $BE output qa ec2         # load_balancer_dns_name, app_url
```

## Despliegues de Frontend

El frontend tiene su propio wrapper más un pipeline de despliegue completo:

```bash
# Infraestructura solamente (S3 + CloudFront):
bash node_modules/genericsuite-fe-scripts/scripts/aws_tf/run-tf-deployment.sh apply STAGE frontend

# Pipeline completo (infra + build + upload + invalidación de caché):
bash node_modules/genericsuite-fe-scripts/scripts/aws_tf/aws_tf_deploy_to_s3.sh STAGE [VARIABLE_TYPE]
```

`aws_tf_deploy_to_s3.sh` es la contraparte de OpenTofu del legado `aws_deploy_to_s3.sh` (que permanece en su lugar). Aplica la pila `frontend`, lee el bucket y la distribución de sus salidas, compila la aplicación con el empaquetador configurado (`vite`, `webpack`, o `react-app-rewired`), ejecuta `aws s3 sync` e invalida la caché de CloudFront.

Variables `.env` requeridas: `AWS_S3_BUCKET_NAME_{TYPE}` (se sustituye un token `[STAGE]`), `APP_{TYPE}_URL`, `AWS_REGION`, y opcionalmente `AWS_SSL_CERTIFICATE_ARN[_{TYPE}]` (`TYPE` por defecto es `FE`). Si no se proporciona un ARN de certificado y la URL de la aplicación está establecida, la pila busca el certificado en `us-east-1` por dominio.

### Qué cambió respecto al script frontend heredado

- **Control de Acceso de Origen (OAC)** en lugar de la obsoleta Identidad de Acceso de Origen (OAI); el bucket S3 es totalmente privado (todas las banderas de bloqueo de acceso público activadas), servido solo a través de CloudFront.
- `ViewerProtocolPolicy` ahora es **redirect-to-https**, y la versión mínima de TLS es **TLSv1.2_2021**.
- **Ruteo de SPA** — las respuestas 403/404 de S3 se mapean a `/index.html` (200).
- Ya no hay permisos ACL públicos para buckets; `aws s3 sync` se ejecuta sin banderas ACL.

## Mejoras de seguridad

La conversión endureció varias áreas en relación con los originales de CloudFormation/CLI:

- CloudFront usa OAC con un bucket privado (sin OAI, sin ACLs públicas); TLS mínimo elevado a TLSv1.2_2021; HTTP redirige a HTTPS.
- Los secretos se pasan como variables sensibles de OpenTofu y se almacenan en Secrets Manager — nunca como parámetros de pila de CloudFormation (que son visibles en la consola y CloudTrail).
- Las políticas de IAM están restringidas — por ejemplo, `secretsmanager:GetSecretValue` se limita a los dos ARNs de secretos de la aplicación en lugar de `*`.
- Validación DNS nativa de ACM reemplaza a los dos recursos personalizados respaldados por Lambda y al registro A de marcador de posición en la antigua plantilla de dominio de EC2.
- La AMI de EC2 se resuelve a partir del parámetro público SSM de Amazon Linux 2 en lugar de un ID de AMI codificado duro y propenso a la deprecación; ambas subredes de ALB están asociadas a la tabla de enrutamiento; la entrada SSH se abre solo cuando se proporciona un CIDR explícitamente.

## Notas de migración

- **Ejecuta ambas rutas lado a lado.** Debido a que los nombres de recursos coinciden, puedes validar las pilas de OpenTofu con `plan` contra un entorno activo antes de la migración total.
- **Importación de recursos existentes.** Para recursos únicos por cuenta que quieras que OpenTofu gestione sin recrearlos, impórtalos al estado, por ejemplo:
  ```bash
  cd node_modules/genericsuite-be-scripts/scripts/aws_tf/stacks/secrets
  tofu import module.secrets.aws_secretsmanager_secret.encrypted \
    arn:aws:secretsmanager:us-east-1:ACCOUNT:secret:myapp-qa-secrets
  ```
- **Alias de KMS.** Si `alias/genericsuite-key` ya existe (por una implementación previa de CloudFormation), conservalo: ejecuta la pila `kms` solo con `plan`, y las pilas `secrets`/`ec2`/`lambda` harán referencia a la clave existente por alias.
- **Corte EC2/ALB.** Elimina la pila legada de CloudFormation EC2 (o importa su ALB/ASG/grupo objetivo/plantilla de lanzamiento) antes de aplicar la pila `ec2`, ya que esos nombres son únicos por cuenta.

## Aún no cubierto

Estas implementaciones no forman parte aún de la ruta OpenTofu y permanecen en sus herramientas existentes:

- RDS (PostgreSQL / MySQL) — `genericsuite-be-scripts/scripts/sql_db/run_sql_db_deploy.sh`.
- Despliegues Chalice-nativos — `genericsuite-be-scripts/scripts/aws/run_aws.sh`.
- Pruebas LocalStack para las pilas OpenTofu (el modo LocalStack del procesador de CloudFormation no ha cambiado).