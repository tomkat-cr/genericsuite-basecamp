# El GitOps de GenericSuite

[GitOps de GenericSuite](https://github.com/tomkat-cr/genericsuite-gitops) proporciona los scripts y configuraciones necesarios para desplegar en varias plataformas (servidores de desarrollo locales, VPS) usando tecnologías de orquestación como Kubernetes, y gestionar artefactos y repositorios con Docker y GitHub.

## Características

- **Despliegue en VPS**: Preparar un servidor VPS con un entorno completamente configurado para ejecutar tu App.
- **K8**: Despliega tu App en un clúster de Kubernetes.
- **Docker**: Construye y empuja tu App a un registro de Docker.
- **Ollama**: instala y configura un servicio local de Ollama.
- **WebUI**: Ejecuta el servicio WebUI local.
- **Stable Diffusion**: instala y configura un servicio local de Stable Diffusion, y ejecuta su WebUI.
- **N8n**: instala y configura un servicio local de N8n.

## Requisitos previos

- Servidor Linux (Debian, Ubuntu, RHEL, Centos, Fedora) con acceso root.

## Inicio

### Generar acceso con clave privada al servidor

Si aún no lo has hecho, genera acceso con clave privada al servidor:

- Copiar el script [vps/generate_client_private_key.sh](https://github.com/tomkat-cr/genericsuite-gitops/blob/main/vps/generate_client_private_key.sh) en tu PC local

- Ejecuta el script:<br>
IMPORTANTE: Este script debe ejecutarse en la PC local, no en el servidor.

```bash
sh generate_client_private_key.sh
```

- Y sigue las instrucciones.

Los siguientes pasos se ejecutarán en el servidor.

### Actualizar el sistema

```bash
# Debian, Ubuntu
sudo apt -y update
sudo apt -y upgrade
```

```bash
# RHEL, Centos, Fedora
sudo yum -y update
sudo yum -y upgrade
```

### Instalar Git

```bash
# Debian, Ubuntu
sudo apt install -y git
```

```bash
# RHEL, Centos, Fedora
sudo yum install -y git
```

### Clonar el repositorio GenericSuite GitOps

```bash
cd ~
git clone https://github.com/tomkat-cr/genericsuite-gitops.git
cd ~/genericsuite-gitops
```

### Instalar requisitos del sistema

```bash
# Crear usuarios y grupos del servidor
sh vps/create_server_users_and_groups.sh
```

### Instalar Docker

Docker le permite ejecutar contenedores en tu servidor.

[Sitio web de Docker](https://www.docker.com/)

```bash
sudo sh docker/install_docker_service.sh
```

Después de la instalación, necesitarás reiniciar el servidor.

```bash
sudo reboot
```

### Instalar Minikube (opcional)

Minikube es una herramienta de código abierto que permite configurar un clúster de Kubernetes de un solo nodo en tu máquina local. El clúster se ejecuta dentro de una máquina virtual e incluye Docker, lo que te permite ejecutar contenedores dentro del nod.

[ Sitio oficial de Minikube](https://minikube.sigs.k8s.io/)

```bash
sh k8/k8_install_minikube.sh
```

```bash
sh k8/k8_start_minikube.sh
```

### Instalar Kubernetes (opcional)

Si quieres algo más complejo, puedes instalar Kubernetes en tu servidor.

Kubernetes es un sistema de código abierto para automatizar la implementación, el escalado y la gestión de aplicaciones en contenedores.

[Sitio oficial de Kubernetes](https://kubernetes.io/)

```bash
sudo sh k8/k8_install_kubernetes.sh
```

### Instalar Ollama

Ollama te permite ponerse en marcha con modelos de lenguaje grandes localmente.
Ejecuta Meta Llama, Microsoft Phi 3, Mistral, Google Gemma y otros modelos. Personaliza y crea tus propios modelos.

[Sitio web de Ollama](https://ollama.com/)

```bash
sudo sh ollama/install_ollama_service.sh
```

### Hacer que el servicio de Ollama esté disponible en la LAN

```bash
sudo sh ollama/open_ollama_port_to_lan.sh
```

### Instalar Stable Diffusion

Stable Diffusion es un modelo de texto a imagen que puede generar fotografías a partir de descripciones de texto.

[Sitio oficial de Stable Diffusion](https://stability.ai/stable-image)

```bash
sudo sh ollama/install_stable_diffusion.sh
```

## Uso

### Ejecutar el contenedor Docker de Open WebUI

Open WebUI es una interfaz autocontenida y extensible para IA (como [ChatGPT](https://chatgpt.com/)) que se adapta a tu flujo de trabajo, y funciona completamente sin conexión.

[Sitio web de Open WebUI](https://openwebui.com/)

```bash
sh ~/genericsuite-gitops/ollama/run_webui.sh
```

### Ejecutar Stable Diffusion WebUi

```bash
sh ~/genericsuite-gitops/ollama/run_stable_diffusion.sh
```

### Monitorear el rendimiento de la GPU

Para supervisar el estado de la GPU, su rendimiento, usa porcentajes y temperaturas:

```bash
sh ~/genericsuite-gitops/ollama/watch_gpu.sh
```

### Ejecutar n8n

n8n es una plataforma de automatización de flujos de trabajo y colaboración para equipos.

[n8n](https://n8n.io/)

- Cambia al directorio de n8n
```bash
cd ~/genericsuite-gitops/n8n
```

- Copiar la plantilla [.env.example](https://github.com/tomkat-cr/genericsuite-gitops/blob/main/n8n/.env.example) a tu archivo `.env`:
```bash
cp .env.example .env
```

- Establece las variables de entorno
```bash
vi .env
# Asigna las variables necesarias
```

- Ejecuta n8n en modo desacoplado
```bash
make run
```

- Detiene n8n
```bash
make stop
```

- Detiene y elimina los contenedores de n8n
```bash
make down
```

- Muestra los logs de n8n y postgres
```bash
make logs
```

- Actualiza n8n, Postgres y pg_admin
```bash
make update
```

- Reinicia los contenedores de Docker
```bash
make restart
```

- Abre el puerto de n8n (Linux)
```bash
make open
```

- Cierra el puerto de n8n (Linux)
```bash
make close
```

- Ejecuta n8n con force-recreate
```bash
make force-recreate
```

- Accede al contenedor n8n-postgres
```bash
make enter_pg
```

- Accede al contenedor n8n
```bash
make enter_n8n
```

## Licencia

GenericSuite es software de código abierto con licencia ISC.

## Créditos

Este proyecto es desarrollado y mantenido por Carlos Ramirez. Para obtener más información o para contribuir al proyecto, visita [El GitOps de GenericSuite en GitHub](https://github.com/tomkat-cr/genericsuite-gitops).

¡Feliz codificación!