# Suite de Seguridad GenericSuite (`gs-security-suite`)

**Genericsuite-security** es una suite de auditoría de seguridad y preparación para producción para repositorios de software y entornos de desarrollo. Proporciona **un conjunto de habilidades especializadas de agentes IA** respaldadas por scripts de la biblioteca estándar de Python 3 sin dependencias.

Ya sea utilizado de forma interactiva a través de asistentes de codificación IA (**Claude Code**, **Google Antigravity**, **Cursor**, **Windsurf**, etc.) o directamente como herramientas CLI independientes en pipelines CI/CD, este paquete ayuda a los desarrolladores a auditar dependencias de la cadena de suministro, fijar referencias de contenedores, eliminar acciones de GitHub no fijadas y verificar la preparación del proyecto antes de la implementación en producción.

## Visión general y arquitectura

La suite se construye alrededor de principios centrales de ingeniería de seguridad:

1. **Sin dependencias externas**: Los escáneres están escritos en la biblioteca estándar de Python 3 (`python3`). No se requiere `pip install`, entornos virtuales, ni herramientas nativas para ejecutar los escaneos.
2. **Dos ejes de detección independientes**: La detección de compromiso valida tanto el *eje de dependencias* ("¿resolvimos una versión de paquete maliciosa?") como el *eje de artefactos* ("¿se ejecutó o persistió la carga útil?"). Un veredicto requiere acuerdo en ambos.
3. **Análisis estático impulsado por corpus**: Los escáneres separan la enumeración de repositorios (`repo-corpus`) de la lógica de detección. Los repos se clonan en directorios seguros e aislados con mecanismos de ejecución deshabilitados.
4. **Verificación de auto-pruebas**: Cada escáner lleva un conjunto de pruebas sintéticas (`tests/selftest.py`). Un resultado de escaneo "limpio" solo es confiable si el escáner primero pasa su auto-prueba frente a indicadores sintéticos conocidos.

---

## Habilidades Incluidas

| Habilidad | Directorio | Descripción | Disparadores / Indicaciones |
|---|---|---|---|
| **`supply-chain-ioc-scan`** | [`skills/supply-chain-ioc-scan`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/supply-chain-ioc-scan) | Triaje de ataques divulgados de la cadena de suministro y gusanos npm/PyPI (p. ej. Shai-Hulud) en disco local y cachés. | *"¿Estamos afectados por [campaña]?"*, *"Verificar dependencias comprometidas"*, *"¿Instalamos la versión mala?"* |
| **`repo-corpus`** | [`skills/repo-corpus`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-corpus) | Enumerar y clonar una organización de GitHub, usuario o directorio local en checkouts seguros con un manifiesto `corpus.json`. | *"Clonar todos los repos en mi org"*, *"Auditar cada repositorio"*, *"Construir un corpus de repos"*/ |
| **`repo-docker-scanner`** | [`skills/repo-docker-scanner`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-docker-scanner) | Escanear referencias de contenedores para etiquetas mutables (`:latest`, etiquetas flotantes) segmentadas por contexto de ejecución (P0/P1/P2). | *"¿Tienen fijadas nuestras imágenes de Docker?"*, *"Encontrar etiquetas :latest"*, *"Fijación de digest de la imagen"* |
| **`repo-packages-scanner`** | [`skills/repo-packages-scanner`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-packages-scanner) | Escanear GitHub Actions (`uses:`) y archivos de bloqueo de dependencias para versiones no fijadas, rangos flotantes y `curl \| bash`. | *"¿Están fijadas nuestras acciones de GitHub?"*, *"Dependencias no fijadas"*, *"Falta lockfile"*, *"curl pipe bash"* |
| **`project-weakness-analysis`** | [`skills/project-weakness-analysis`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/project-weakness-analysis) | Calcular la preparación para producción y el riesgo de seguridad por proyecto a través de ejes independientes y no promediados. | *"¿Está esto listo para producción?"*, *"Auditar mis proyectos"*, *"Revisión de preparación para producción"* |

---

## Guía de instalación de agentes IA

Las habilidades siguen el formato estándar **Agent Skills / Open Skill Specification** (`SKILL.md` con frontmatter YAML). A continuación, instrucciones para instalar y habilitar el complemento en diferentes agentes de IA.

### Claude Code

Usando el **mercado de plugins** de Claude Code:

```bash
claude

/plugin marketplace add tomkat-cr/genericsuite-security

/plugin install gs-security-suite@genericsuite-security
```

### CLI de Habilidades

Usando la **Vercel Skills CLI ([skills.sh](https://skills.sh))**:

```bash
npx skills add tomkat-cr/genericsuite-security
```

---

### Google Antigravity (AGY)

Google Antigravity descubre habilidades ubicadas dentro de rutas de habilidades estándar o configuraciones de plugins.

#### Opción A: Instalación global de habilidades (Nivel de usuario)
Enlace simbólico o copia del directorio `skills` en la ruta de habilidades de Antigravity:
```bash
# Crea la carpeta global de habilidades si no existe
mkdir -p ~/.gemini/antigravity/skills

# Enlaza simbólicamente todas las habilidades de este repositorio
ln -s /path/to/genericsuite-security/skills/* ~/.gemini/antigravity/skills/
```

#### Opción B: Instalación específica para el workspace
Para habilitar las habilidades de seguridad en un único espacio de trabajo de Antigravity:
```bash
mkdir -p .gemini/skills
cp -r /path/to/genericsuite-security/skills/* .gemini/skills/
```

#### Opción C: Administrador de plugins de Antigravity
Coloca o enlaza el repositorio dentro del directorio de plugins de Antigravity:
```bash
mkdir -p ~/.gemini/config/plugins/
ln -s /path/to/genericsuite-security ~/.gemini/config/plugins/genericsuite-security
```

Una vez instalado, pida a Antigravity que ejecute cualquier tarea de seguridad (p. ej., *"Antigravity, audit all GitHub Actions in my repo for unpinned commits"*).

---

### Cursor

Cursor utiliza `.cursor/rules/` o archivos de contexto de proyecto (`.cursorrules`) para guiar el comportamiento de la IA.

#### Opción A: Reglas de proyecto (`.cursor/rules/`)
Enlace o copie los archivos `SKILL.md` de las habilidades en el directorio de reglas de tu proyecto:
```bash
mkdir -p .cursor/rules

# Ejemplo: habilitar la habilidad de Análisis de Debilidad del Proyecto en Cursor
cp /path/to/genericsuite-security/skills/project-weakness-analysis/SKILL.md .cursor/rules/project-weakness-analysis.mdc
cp /path/to/genericsuite-security/skills/repo-packages-scanner/SKILL.md .cursor/rules/repo-packages-scanner.mdc
```

#### Opción B: Referencia directa de archivos en el chat de Cursor
En el chat de Cursor (`Cmd+L` o `Ctrl+L`), referencia el archivo `SKILL.md` deseado usando `@`:
```text
@skills/supply-chain-ioc-scan/SKILL.md Por favor, verifica si nuestro repositorio está afectado por la reciente revelación de la cadena de suministro npm.
```

---

### Windsurf & Otros Agentes Open-Skill

Cualquier agente de IA que siga el formato estándar de habilidades de agente puede usar estas habilidades directamente.

1. **Agregar ruta de habilidades**: Apunta la configuración de habilidades personalizadas de tu agente o las instrucciones del espacio de trabajo hacia el directorio `skills/` de este repositorio.
2. **Contexto directo de prompts**: Adjunta `skills/<nombre-habilidad>/SKILL.md` a tu sesión de agente.

---

## Referencia de Habilidades y Uso

### 1. Escaneo IOC de la Cadena de Suministro

- **Directorio**: [`skills/supply-chain-ioc-scan`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/supply-chain-ioc-scan)
- **Propósito**: Triaje de incidentes rápido cuando se divulga un ataque de la cadena de suministro de npm, PyPI o un proveedor (p. ej., Keyv / Cacheable Shai-Hulud).
- **Características clave**:
  - Escanea tanto el eje de dependencias (archivos de bloqueo, `~/.npm/_cacache`, `node_modules`) como el eje de artefactos (hashes SHA-1/256 de la carga, dominios C2, hooks de IDE, procesos).
  - Fusiona feeds de indicadores de proveedores (Socket.dev, Wiz, Datadog) con una solución offline.
  - Emite veredictos respaldados por evidencia (`CONFIRMED` vs `REVIEW`).

#### Invocación a través de un Agente IA
> *"Scanea mi máquina en busca de exposición al reciente gusano de la cadena de suministro npm Shai-Hulud."*

#### Ejecución independiente desde la CLI
```bash
cd skills/supply-chain-ioc-scan

# Ejecutar escaneo completo (escanea $HOME por defecto)
./scripts/run_scan.sh

# Escanear directorios específicos
./scripts/run_scan.sh ~/projects/app1 ~/projects/app2

# Escanear con un perfil IOC personalizado
PROFILE=iocs/custom-campaign.json ./scripts/run_scan.sh ~/projects
```
- **Códigos de salida**: `0` Limpio, `1` Hallazgos detectados, `2` Error.
- **Salida**: Informes guardados en `$TMPDIR/ioc-scan-<timestamp>/`.

---

### 2. Corpus de Repos

- **Directorio**: [`skills/repo-corpus`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-corpus)
- **Propósito**: Fundamento de la fase 1 para el escaneo a nivel de organización. Clona de forma segura repos desde una organización de GitHub, un usuario o un árbol de directorios en un manifiesto `corpus.json` atribuible.
- **Características clave**:
  - Banderas de clonado git de confianza cero (previenen la ejecución de hooks, submódulos o código malicioso durante el clon).
  - Seguimiento explícito de árboles podados, directorios legibles o clones fallidos (sin huecos silenciosos).
  - Fijación de ramas (`--branch NAME`) para auditoría entre repos múltiples.

#### Invocación a través de un Agente IA
> *"Construye un corpus de repositorios para la organización de GitHub `my-org`."*

#### Ejecución independiente desde la CLI
```bash
cd skills/repo-corpus

# Clonar toda una organización de GitHub
./scripts/run_corpus.sh --org my-org

# Construir un corpus a partir de una carpeta local existente (sin clonar)
./scripts/run_corpus.sh --local ~/my-projects

# Verificar alcance sin clonar
python3 scripts/build_corpus.py --org my-org --list-only
```
- **Códigos de salida**: `0`Corpus completo, `1`Corpus parcial (fallos registrados), `2` Error.
- **Salida**: Escribe `corpus.json` y clona repos bajo `corpus/`.

---

### 3. Escáner de Docker de Repos

- **Directorio**: [`skills/repo-docker-scanner`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-docker-scanner)
- **Propósito**: Escáner de análisis estático fase 2. Detecta referencias de imágenes de contenedores mutables (`:latest`, etiquetas flotantes, digestos faltantes) y clasifica los hallazgos por contexto de ejecución.
- **Características clave**:
  - Priorización por contexto:
    - **P0**: Despliegues de producción, tuberías CI de lanzamiento, plantillas IaC (Terraform, CloudFormation).
    - **P1**: CI de desarrollo, pruebas, Dockerfiles de imágenes base.
    - **P2**: Ejemplos, dev-local con compose, documentación.
  - Resolución opcional de etiqueta a digest (`--resolve`) vía llamadas a la API OAuth de registro anónimo (Docker Hub, GHCR, Quay).
  - Soporte de línea base de políticas (`policy/images.json`) para riesgos aceptados.

#### Invocación a través de un Agente IA
> *"Encuentra todas las imágenes de contenedor sin fijar en nuestros repos de la organización de GitHub."*

#### Ejecución independiente desde la CLI
```bash
cd skills/repo-docker-scanner

# Construir corpus y escanear toda una organización
./scripts/run_docker_scan.sh --org my-org

# Modo lint de CI en repositorio local (fallará si existen hallazgos P0)
./scripts/run_docker_scan.sh --local . --fail-on P0

# Escanear corpus existente con resolución de registro habilitada
./scripts/run_docker_scan.sh --corpus ../repo-corpus/corpus.json --resolve
```
- **Códigos de salida**: `0` Limpio (por debajo del umbral), `1` Hallazgos por encima del umbral, `2` Error.
- **Salida**: Genera `report.md`, `findings.json` y formato SARIF `findings.sarif`.

---

### 4. Escáner de Paquetes de Repos

- **Directorio**: [`skills/repo-packages-scanner`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/repo-packages-scanner)
- **Propósito**: Escáner de análisis estático fase 3. Audita GitHub Actions (`uses:`) y dependencias de paquetes en npm, PyPI, Go, Rust, Ruby y Poetry.
- **Características clave**:
  - Señala GitHub Actions no fijadas (debe usar SHA de confirmación de 40 caracteres, p. ej. `actions/checkout@a5ac7e5...`).
  - Detecta rangos de dependencias flotantes, archivos de bloqueo ausentes y `npm install` en CI (en lugar de `npm ci`).
  - Detecta ejecución remota de código no fijada (`curl | bash`, `wget | sh`).
  - Incluye `run_gh_scan.sh` para escanear repos públicos de GitHub de usuario/organización en busca de palabras clave de compromiso.

#### Invocación a través de un Agente IA
> *"Comprueba si alguno de nuestros GitHub Actions usa etiquetas mutables o rangos de dependencias flotantes."*

#### Ejecución independiente desde la CLI
```bash
cd skills/repo-packages-scanner

# Escanear una organización
./scripts/run_packages_scan.sh --org my-org

# Modo lint de CI en repositorio local
./scripts/run_packages_scan.sh --local . --fail-on P0

# Escanear corpus con resolución de publicadores de Action vía API de GitHub
./scripts/run_packages_scan.sh --corpus ../repo-corpus/corpus.json --resolve

# Escaneo de compromiso de usuario/organización
./scripts/run_gh_scan.sh username "malicious-keyword" 2026-01-01
```
- **Códigos de salida**: `0` Limpio, `1` Hallazgos por encima del umbral, `2` Error.
- **Salida**: Genera `report.md`, `findings.json` y formato SARIF `findings.sarif`.

---

### 5. Análisis de Debilidad del Proyecto

- **Directorio**: [`skills/project-weakness-analysis`https://github.com/tomkat-cr/genericsuite-security/tree/main/skills/project-weakness-analysis)
- **Propósito**: Evalúa si los proyectos de software están listos y son seguros para su despliegue en producción.
- **Características clave**:
  - **Dos ejes independientes (Nunca promediados)**:
    - **Nivel de Preparación**: `production-ready` | `needs-work` | `not-ready` | `unknown`. Evalúa autenticación, manejo de errores, pruebas, CI, organización del código.
    - **Nivel de Riesgo de Seguridad**: `critical` | `high` | `medium` | `low` | `none`. Evalúa filtración de secretos, bypass de autenticación, exposición de datos personales, dependencias de la cadena de suministro sin fijar.
  - **5 modos de entrada flexibles**: árbol local (`--root`), lista explícita de directorios (`--projects`), corpus existente (`--corpus`), Organización/Usuario de GitHub (`--org`), o base de datos de proyectos (`--db`).
  - **Bucle de reauditoría**: segunda pasada verifica hallazgos previos (`resolved` | `partial` | `open`).

#### Invocación a través de un Agente IA
> *"Realiza una revisión de preparación para producción y seguridad en todos los proyectos en ~/projects."*

#### Ejecución independiente desde la CLI
```bash
cd skills/project-weakness-analysis

# Escanear árbol de proyectos local
./scripts/run_weakness_analysis.sh --root ~/projects

# Escanear lista explícita de directorios
./scripts/run_weakness_analysis.sh --projects ~/dev/app1 ~/dev/app2

# Escanear un corpus existente
./scripts/run_weakness_analysis.sh --corpus ../repo-corpus/corpus.json

# Fusionar salidas de escaneo previas sin volver a escanear
./scripts/run_weakness_analysis.sh --phase merge
```
- **Códigos de salida**: `0` Todos los proyectos pasaron las puertas, `1` Puertas fallidas / proyectos bloqueados, `2` Error.
- **Salida**: Generada en `./insights/`:
  - `WEAKNESS-REPORT.md` (Resumen legible)
  - `insights.json` y `security-audit.json`
  - `insights-table.csv` / `.json` (Exportación plana tabular)
  - `findings.sarif` (Formato SARIF para integración IDE / GitHub Security)

---

## Uso de CLI independiente (Sin IA)

Todas las herramientas en `genericsuite-security` son completamente funcionales como comandos de shell y Python independientes. Requieren solo **Python 3.8+** (biblioteca estándar) y **git**.

```bash
# Ejemplo 1: Comprobación rápida de seguridad en un repositorio local
cd skills/repo-packages-scanner
./scripts/run_packages_scan.sh --local /path/to/my/project

# Ejemplo 2: Auditoría de imágenes de contenedores
cd skills/repo-docker-scanner
./scripts/run_docker_scan.sh --local /path/to/my/project

# Ejemplo 3: Escaneo completo de la cadena de suministro IOC
cd skills/supply-chain-ioc-scan
./scripts/run_scan.sh /path/to/my/project
```

---

## Verificación y Auto-Pruebas

Antes de confiar en la salida de cualquier escáner, ejecute su suite de auto-pruebas integrada. Las auto-pruebas crean fixtures sintéticos infectados para verificar que la lógica de detección capture todos los indicadores sintéticos y no produzca falsos positivos en imitaciones benignas.

```bash
# Auto-prueba del escáner de IOC de la cadena de suministro
python3 skills/supply-chain-ioc-scan/tests/selftest.py

# Auto-prueba del generador de corpus
python3 skills/repo-corpus/tests/selftest.py

# Auto-prueba del escáner de Docker
python3 skills/repo-docker-scanner/tests/selftest.py

# Auto-prueba del escáner de paquetes
python3 skills/repo-packages-scanner/tests/selftest.py

# Auto-prueba del análisis de debilidad
python3 skills/project-weakness-analysis/tests/selftest.py
```