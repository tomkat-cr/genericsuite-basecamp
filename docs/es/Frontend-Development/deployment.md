# Despliegue del Frontend

### Despliegue en QA

Para realizar un despliegue de QA sobre AWS S3:

```bash
make deploy_qa
```

### Despliegue en otros entornos

Para realizar un despliegue de Staging, Demo y Producción sobre AWS S3:

```bash
make deploy_staging
```
```bash
make deploy_demo
```
```bash
make deploy_prod
```

## Solución de problemas

Si recibes el error `ERROR running aws s3api put-bucket-policy --bucket BUCKET_NAME --policy S3_BUCKET_POLICY`, probablemente el script no pudo desactivar la opción 'Bloquear todo el acceso público' en el bucket de S3.

Para solucionarlo:

* Ve a la Consola de AWS.
* Ve a S3.
* Busca el bucket de la App (p. ej. `exampleapp-frontend-website`).
* Haz clic en el nombre del bucket.
* Haz clic en la pestaña 'Permisos'.
* Haz clic en 'Editar' en la sección 'Bloqueo de acceso público (configuración del bucket)'.
* Desactiva 'Bloquear todo el acceso público'.
* Haz clic en 'Guardar cambios'.
* Confirma la operación.
 
Para vincular este bucket de S3 al dominio de la App:
 
* Ve a Route 53.
* Haz clic en la Zona correspondiente al dominio de la App.
* Haz clic en 'Crear registro'.
* Introduce el subdominio: 'app-qa', 'app-staging', 'app-demo' o 'app' (para producción).
* Activa 'alias'.
* En 'Dirigir el tráfico a' selecciona la opción 'Alias a CloudFront'.
* En 'Elegir distribución' selecciona la que corresponde a la etapa de la App.
* Haz clic en 'Crear registros'.