# Backend Deployment

### Deploy to QA

To perform a QA deployment over AWS S3:

```bash
make deploy_qa
```

### Other environments deployment

To perform a Staging, Demo and Production deployment over AWS S3:

```bash
make deploy_staging
```
```bash
make deploy_demo
```
```bash
make deploy_prod
```

IMPORTANT: for more deployment options and instructions, check the [Deployment](./GenericSuite-Scripts/index.md#deployment) section in the GenericSuite Scripts documentation.