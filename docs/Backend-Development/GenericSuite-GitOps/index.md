# The GenericSuite GitOps

[GenericSuite GitOps](https://github.com/tomkat-cr/genericsuite-gitops) provides the scripts and configurations needed to deploy on various platforms (local development servers, VPS) using orchestration technologies like Kubernetes, and manage artifacts and repositories with Docker and GitHub.

## Features

- **VPS Deployment**: Prepare a VPS server with a fully configured environment to run your App.
- **K8**: Deploy your App on a Kubernetes cluster.
- **Docker**: Build and push your App to a Docker registry.
- **Olama**: install and configure a local OLLAMA service.
- **WebUI**: Run the local WebUI service.
- **Stable Diffusion**: install and configure a local Stable Diffusion service, annd run its WebUi.
- **N8n**: install and configure a local N8n service.

## Pre-requisites

- Linux server (Debian, Ubuntu, RHEL, Centos, Fedora) with root access.

## Getting Started

### Generate private key access to the server

If you haven't done this yet, generate private key access to the server:

* Copy the script [vps/generate_client_private_key.sh](https://github.com/tomkat-cr/genericsuite-gitops/blob/main/vps/generate_client_private_key.sh) on your local PC

* Run the script:<BR/>
IMPORTANT: This script must be executed on the local PC, not on the Server.

```bash
sh generate_client_private_key.sh
```

* And follow the instructions.

The next steps will be executed on the server.

### Update OS

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

### Install Git

```bash
# Debian, Ubuntu
sudo apt install -y git
```

```bash
# RHEL, Centos, Fedora
sudo yum install -y git
```

### Clone the GenericSuite GitOps repository

```bash
cd ~
git clone https://github.com/tomkat-cr/genericsuite-gitops.git
cd ~/genericsuite-gitops
```

### Install OS requirements

```bash
# Create server users and groups
sh vps/create_server_users_and_groups.sh
```

### Install Docker

Docker allows you to run containers on your server.

[https://www.docker.com/](https://www.docker.com/)

```bash
sudo sh docker/install_docker_service.sh
```

After the installation, you'll need to restart the server.

```bash
sudo reboot
```

### Install Minikube (optional)

Minikube is an open source tool that allows you to set up a single-node Kubernetes cluster on your local machine. The cluster is run inside a virtual machine and includes Docker, allowing you to run containers inside the node.

This is an excellent way to test in a Kubernetes environment locally, without using up too much resources.

[https://minikube.sigs.k8s.io/](https://minikube.sigs.k8s.io/)

```bash
sh k8/k8_install_minikube.sh
```

```bash
sh k8/k8_start_minikube.sh
```

### Install Kubernetes (optional)

If you want something more complex, you can install Kubernetes on your server.

Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

[https://kubernetes.io/](https://kubernetes.io/)

```bash
sudo sh k8/k8_install_kubernetes.sh
```

### Install Ollama

Ollama allows to get up and running with large language models locally.
Run Meta Llama, Microsoft Phi 3, Mistral, Google Gemma, and other models. Customize and create your own.

[https://ollama.com/](https://ollama.com/)

```bash
sudo sh ollama/install_ollama_service.sh
```

### Make the Ollama service available to the LAN servers

```bash
sudo sh ollama/open_ollama_port_to_lan.sh
```

### Install Stable Diffusion

Stable Diffusion is a text-to-image model that can generate photos from text descriptions.

[https://stability.ai/stable-image](https://stability.ai/stable-image)

```bash
sudo sh ollama/install_stable_diffusion.sh
```

## Usage

### Run Open WebUi Docker Container

Open WebUI is an extensible, self-hosted interface for AI (like [ChatGPT](https://chatgpt.com/)) that adapts to your workflow, all while operating entirely offline.

[https://openwebui.com/](https://openwebui.com/)

```bash
sh ~/genericsuite-gitops/ollama/run_webui.sh
```

### Run Stable Diffusion WebUi

```bash
sh ~/genericsuite-gitops/ollama/run_stable_diffusion.sh
```

### Watch GPU Performance

To watch the GPU status, performance, use percentages and temperatures:

```bash
sh ~/genericsuite-gitops/ollama/watch_gpu.sh
```

### Run n8n

n8n is a workflow automation and collaboration platform for teams.

[https://n8n.com/](https://n8n.io/)

* Change to the n8n directory
    ```bash
    cd ~/genericsuite-gitops/n8n
    ```

* Set the environment variables
    ```bash
    cp .env.example .env
    vi .env
    # Assign the necessary variables
    ```

* Runs n8n in detached mode
    ```bash
    make run
    ```

* Stops n8n
    ```bash
    make stop
    ```

* Stops and removes n8n containers
    ```bash
    make down
    ```

* Shows n8n and postgres logs
    ```bash
    make logs
    ```

* Upgrade n8n, postgress and pg_admin
    ```bash
    make update
    ```

* Restart docker containers
    ```bash
    make restart
    ```

* Open n8n port (linux)
    ```bash
    make open
    ```

* Close n8n port (linux)
    ```bash
    make close
    ```

* Run n8n with force-recreate
    ```bash
    make force-recreate
    ```

* Enter to the n8n-postgres container
    ```bash
    make enter_pg
    ```

* Enter to the n8n container
    ```bash
    make enter_n8n
    ```

## License

GenericSuite is open-sourced software licensed under the ISC license.

## Credits

This project is developed and maintained by Carlos Ramirez. For more information or to contribute to the project, visit [The GenericSuite GitOps on GitHub](https://github.com/tomkat-cr/genericsuite-gitops).

Happy Coding!