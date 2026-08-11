# GenericSuite Scripts para Desarrollo de Frontend

[GenericSuite Scripts (frontend version)](https://github.com/tomkat-cr/genericsuite-fe-scripts) es un conjunto de características para mejorar el proceso de desarrollo de las aplicaciones ReactJS.

Este repositorio contiene los scripts de frontend necesarios para construir e implementar aplicaciones ReactJS hechas por [GenericSuite (frontend version)](../GenericSuite-Core/index.md) y [GenericSuite AI (frontend version)](../GenericSuite-AI/index.md).

## Funciones

- **Scripts de Desarrollo y Producción:** Comandos rápidos para iniciar el desarrollo o construir tu aplicación para entornos de QA, staging y producción en AWS.
- **Despliegue en AWS**: Despliegue a AWS como sitio web de CloudFront con un bucket S3.
- **Entorno de Desarrollo Local**: ejecutándose con http o https, con o sin Docker.
- **Gestión de configuración JSON común**: para añadir el submódulo de Git con los directorios de configuración JSON comunes.

## Inicio

Para empezar con GenericSuite Scripts (versión frontend), sigue estos pasos:

### Instalar los Scripts Frontend de GenericSuite

```bash
npm init
```

```bash
npm install -D genericsuite-fe-scripts
```

### Preparar el Makefile

Copiar la plantilla de `Makefile` desde `node_modules/genericsuite-fe-scripts`:

```bash
cp node_modules/genericsuite-fe-scripts/Makefile ./Makefile
```

### Inicializa tu proyecto

Consulta la [Guía de Inicio de GenericSuite](../GenericSuite-Core/index.md#inicio) para obtener más detalles.

## Uso

### Iniciar el Servidor de Desarrollo

Para iniciar el servidor de desarrollo:

```bash
make run
```

## Realizar la primera compilación

```bash
make build
```

### Despliegue a entornos de QA, Staging, Demo y Producción

Consulta la [Guía de Despliegue](../deployment.md) para obtener más detalles.