# Despliegue del Backend

### Despliegue a QA

Para realizar un despliegue de QA en AWS S3:

```bash
make deploy_qa
```

### Despliegue a otros entornos

Para realizar un despliegue en Staging, Demo y Producción sobre AWS S3:

```bash
make deploy_staging
```
```bash
make deploy_demo
```
```bash
make deploy_prod
```

IMPORTANTE: para obtener más opciones de despliegue e instrucciones, consulta la sección [Despliegue](./GenericSuite-Scripts/index.md#deployment) en la documentación de GenericSuite Scripts.