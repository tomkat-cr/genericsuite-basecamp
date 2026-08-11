# Suite de Seguridad GenericSuite (`gs-security-suite`)

**`genericsuite-security`** es una suite de auditoría de seguridad y preparación para producción para repositorios de software y entornos de desarrollo. Proporciona **5 habilidades especializadas de agentes de IA** respaldadas por scripts de la biblioteca estándar de Python 3 sin dependencias.

Ya sea utilizado de forma interactiva a través de asistentes de código IA (**Claude Code**, **Google Antigravity**, **Cursor**, **Windsurf**, etc.) o directamente como herramientas CLI independientes en pipelines de CI/CD, este paquete ayuda a los desarrolladores a auditar dependencias de la cadena de suministro, fijar referencias de contenedores, eliminar acciones de GitHub sin fijar y verificar la preparación del proyecto antes del despliegue en producción.

---

## Tabla de Contenidos

- [- Visión general y Arquitectura](#vision-general-y-arquitectura)
- [- Habilidades incluidas](#habilidades-incluidas)
- [- Guía de instalación de agentes de IA](#guia-de-instalacion-de-agentes-de-ia)
  - [Claude Code](#claude-code)
  - [CLI de Habilidades](#cli-de-habilidades)
  - [Antigravity de Google (AGY)](#antigravity-de-google-agy)
  - [Cursor](#cursor)
  - [Windsurf y otros agentes de habilidades abiertas](#windsurf-y-otros-agentes-de-habilidades-abiertas)
- [- Referencia de Habilidades y Uso](#referencias-de-habilidades-y-uso)
  - [1. Escaneo IOC de la Cadena de Suministro](#1-escaneo-ioc-de-la-cadena-de-suministro)
  - [2. Corpus de Repos](#2-corpus-de-repos)
  - [3. Analizador de Docker de Repos](#3-analizador-de-docker-de-repos)
  - [4. Analizador de Paquetes de Repos](#4-analizador-de-paquetes-de-repos)
  - [5. Análisis de Debilidades del Proyecto](#5-analisis-de-debilidades-del-proyecto)
- [- Uso de CLI independiente (Sin IA Requerido)](#uso-de-cli-independiente-sin-ia-requerido)
- [- Verificación y Autoevaluación](#verificacion-y-autoevaluacion)
- [- Licencia y Soporte](#licencia-y-soporte)

---

## Visión general y Arquitectura

La suite se basa en principios centrales de ingeniería de seguridad:

1. **Sin dependencias externas**: Los escáneres están escritos con la biblioteca estándar de Python 3 (`python3`). No se requiere `pip install`, entornos virtuales ni toolchains nativos para ejecutar los escaneos.
2. **Dos ejes de detección independientes**: la detección de compromiso valida tanto el eje de dependencias (¿resolvimos una versión de paquete maliciosa?) como el eje de artefactos (¿se ejecutó o persistió el payload?). Un veredicto requiere acuerdo en ambos.
3. **Análisis estático impulsado por corpus**: Los escáneres separan la enumeración de repositorios (`repo-corpus`) de la lógica de detección. Los repositorios se clonan en directorios seguros e aislados con mecanismos de ejecución desactivados.
4. **Verificación de auto-prueba**: Cada escáner incluye una suite de pruebas sintéticas (`tests/selftest.py`). Un resultado de escaneo "limpio" solo se considera confiable si el escáner primero aprueba su auto-prueba contra indicadores sintéticos conocidos.

---

## Habilidades incluidas

| Habilidad | Directorio | Descripción | Disparadores / Indicaciones |
|---|---|---|---|
| **`supply-chain-ioc-scan`** | [`skills/supply-chain-ioc-scan`](skills/supply-chain-ioc-scan) | Triage de ataques divulgados de la cadena de suministro y gusanos npm/PyPI (p. ej., Shai-Hulud) en disco local y cachés. | *"¿Estamos afectados por [campaña]?"*, *"Verificar dependencias comprometidas"*, *"¿Instalamos la versión dañina?"* |
| **`repo-corpus`** | [`skills/repo-corpus`](skills/repo-corpus) | Enumerar y clonar una organización, usuario de GitHub o directorio local en checks seguros con un manifiesto `corpus.json`. | *"Clonar todas las repos de mi organización"*, *"Auditar cada repositorio"*, *"Construir un corpus de repos"*

| **`repo-docker-scanner`** | [`skills/repo-docker-scanner`](skills/repo-docker-scanner) | Escanear referencias de contenedores para etiquetas mutables (`:latest`, etiquetas flotantes) clasificado por contexto de ejecución (P0/P1/P2). | *"¿Nuestras imágenes de Docker están fijadas?"*, *"Buscar etiquetas :latest"*, *"Fijación de digest de imágenes"* |
| **`repo-packages-scanner`** | [`skills/repo-packages-scanner`](skills/repo-packages-scanner) | Escanear GitHub Actions (`uses:`) y archivos de bloqueo de paquetes para versiones no fijadas, rangos flotantes y `curl | bash`. | *"¿Nuestras GitHub Actions están fijadas?"*, *"Dependencias sin fijar"*, *"Falta de lockfile"*, *"curl pipe bash"* |
| **`project-weakness-analysis`** | [`skills/project-weakness-analysis`](skills/project-weakness-analysis) | Calcular la preparación para producción y el riesgo de seguridad por proyecto en ejes independientes, sin promediar. | *"¿Está esto listo para producción?"*, *"Auditar mis proyectos"*, *"Revisión de preparación para producción"* |

---

## Guía de instalación de agentes de IA

Las habilidades siguen el formato estándar **Agent Skills / Open Skill Specification** (`SKILL.md` con frontmatter YAML). A continuación se presentan instrucciones para instalar y habilitar el complemento en diferentes agentes de IA.

### Claude Code

Usando el marketplace de plugins de Claude Code:

```bash
claude

/plugin marketplace add tomkat-cr/genericsuite-security

/plugin install gs-security-suite@genericsuite-security
```

### CLI de Habilidades

Usando el **Vercel Skills CLI ([skills.sh](https://skills.sh))**:

```bash
npx skills add tomkat-cr/genericsuite-security
```

---

### Antigravity de Google (AGY)

Google Antigravity descubre habilidades ubicadas dentro de rutas de habilidades estándar o configuraciones de plugins.

#### Opción A: Instalación Global de Habilidades (Nivel de usuario)
Enlaza o copia el directorio `skills` en la ruta de habilidades de Antigravity:
```bash
# Crear la carpeta global de habilidades si no existe
mkdir -p ~/.gemini/antigravity/skills

# Enlaza todas las habilidades de este repositorio
ln -s /ruta/al/genericsuite-security/skills/* ~/.gemini/antigravity/skills/
```

#### Opción B: Instalación Específica de Espacio de Trabajo
Para habilitar las habilidades de seguridad en un solo espacio de trabajo de Antigravity:
```bash
mkdir -p .gemini/skills
cp -r /ruta/al/genericsuite-security/skills/* .gemini/skills/
```

#### Opción C: Gestor de Plugins de Antigravity
Coloca o enlaza el repositorio bajo el directorio de plugins de Antigravity:
```bash
mkdir -p ~/.gemini/config/plugins/
ln -s /ruta/al/genericsuite-security ~/.gemini/config/plugins/genericsuite-security
```

Una vez instalado, solicita a Antigravity que ejecute cualquier tarea de seguridad (p. ej., *"Antigravity, audita todas las GitHub Actions en mi repositorio para confirmar commits sin fijar"*).

---

### Cursor

Cursor usa `.cursor/rules/` o archivos de contexto del proyecto (`.cursorrules`) para guiar el comportamiento de IA.

#### Opción A: Reglas del Proyecto (`.cursor/rules/`)
Vincula o copia los archivos `SKILL.md` de las habilidades en el directorio `.cursor/rules/` de tu proyecto:
```bash
mkdir -p .cursor/rules

# Ejemplo: habilitar la habilidad de Análisis de Debilidades del Proyecto en Cursor
cp /ruta/al/genericsuite-security/skills/project-weakness-analysis/SKILL.md .cursor/rules/project-weakness-analysis.mdc
cp /ruta/al/genericsuite-security/skills/repo-packages-scanner/SKILL.md .cursor/rules/repo-packages-scanner.mdc
```

#### Opción B: Referencia de Archivos Directos en Cursor Chat
En la conversación de Cursor (`Cmd+L` o `Ctrl+L`), referencia el archivo deseado `SKILL.md` usando `@`:
```text
@skills/supply-chain-ioc-scan/SKILL.md Por favor verifica si nuestro repositorio está afectado por la reciente divulgación de la cadena de suministro npm.
```

---

### Windsurf y otros agentes de habilidades abiertas

Cualquier agente de IA que siga el formato estándar de Agent Skills puede usar estas habilidades directamente.

1. **Agregar Ruta de Habilidades**: Apunta la configuración de habilidades personalizadas de tu agente o las instrucciones de espacio de trabajo a la carpeta `skills/` de este repositorio.
2. **Disparo de Contexto Directo**: Adjunta `skills/<skill-name>/SKILL.md` a tu sesión de agente.

---

## Referencia de Habilidades y Uso

### 1. Escaneo IOC de la Cadena de Suministro

- **Directorio**: [`skills/supply-chain-ioc-scan`](skills/supply-chain-ioc-scan)
- **Propósito**: Triagem rápida de incidentes cuando se disclose una cadena de suministro de npm, PyPI u otra fuente de suministro de software (p. ej., Keyv / Cacheable Shai-Hulud).
- **Características clave**:
  - Escanea tanto el eje de dependencias (archivos de bloqueo, `~/.npm/_cacache`, `node_modules`) como el eje de artefactos (hashes SHA-1/256 del payload, dominios C2, hooks de IDE, procesos).
  - Fusiona feeds de indicadores de proveedores (Socket.dev, Wiz, Datadog) con una alternativa sin conexión.
  - Genera veredictos respaldados por evidencia (`CONFIRMED` vs `REVIEW`).

#### Invocación vía Agente de IA
> *"Escanea mi máquina en busca de exposición al reciente gusano de la cadena de suministro npm Shai-Hulud."*

#### Ejecución de CLI Independiente
```bash
cd skills/supply-chain-ioc-scan

# Ejecutar escaneo completo (escanea $HOME por defecto)
./scripts/run_scan.sh

# Escanear directorios específicos
./scripts/run_scan.sh ~/proyectos/app1 ~/proyectos/app2

# Escanear con un perfil IOC personalizado
PROFILE=iocs/custom-campaign.json ./scripts/run_scan.sh ~/projets
```
- **Códigos de salida**: `0` Limpio, `1` Hallazgos detectados, `2` Error.
- **Salida**: Informes guardados en `$TMPDIR/ioc-scan-<timestamp>/`.

---

### 2. Corpus de Repos

- **Directorio**: [`skills/repo-corpus`](skills/repo-corpus)
- **Propósito**: Base de la fase 1 para escaneo a nivel de organización. Clona de forma segura repositorios desde una organización o usuario de GitHub o estructura de directorios en un manifiesto `corpus.json` atribuible.
- **Características clave**:
  - Flags de clonación git de confianza cero (impide la ejecución de hooks, submódulos o código malicioso durante el clon).
  - Seguimiento explícito de árboles podados, directorios legibles o clones fallidos (sin huecos silenciosos).
  - Pinning de ramas (`--branch NAME`) para auditoría entre repos múltiples.

#### Invocación vía IA
> *"Construye un corpus de repos para la organización de GitHub `my-org`."*

#### Ejecución de CLI Independiente
```bash
cd skills/repo-corpus

# Clonar una organización completa de GitHub
./scripts/run_corpus.sh --org my-org

# Construir un corpus desde una carpeta local existente (sin clonación)
./scripts/run_corpus.sh --local ~/mis-proyectos

# Verificar alcance solo sin clonar
python3 scripts/build_corpus.py --org my-org --list-only
```
- **Códigos de salida**: `0` Corpus completo, `1` Corpus parcial (fallos registrados), `2` Error.
- **Salida**: Escribe `corpus.json` y clona repos a `corpus/`.

---

### 3. Analizador Docker de Repos

- **Directorio**: [`skills/repo-docker-scanner`](skills/repo-docker-scanner)
- **Propósito**: Escáner de fase 2 de análisis estático. Detecta referencias de contenedores mutables (`:latest`, etiquetas flotantes, digest faltante) y clasifica los hallazgos por contexto de ejecución.
- **Características clave**:
  - Jerarquía de prioridad por contexto:
    - **P0**: Implementaciones de producción, pipelines de CI de lanzamiento, plantillas IaC (Terraform, CloudFormation).
    - **P1**: CI de desarrollo, suites de pruebas, Dockerfiles de imágenes base.
    - **P2**: Ejemplos, dev-local, documentación.
  - Resolución opcional de etiqueta a digest (`--resolve`) mediante llamadas OAuth API de registro anónimas (Docker Hub, GHCR, Quay).
  - Soporte de línea base de políticas (`policy/images.json`) para riesgos aceptados.

#### Invocación vía IA
> *"Encuentra todas las imágenes de contenedor sin fijar en los repos de nuestra organización en GitHub."*

#### Ejecución de CLI Independiente
```bash
cd skills/repo-docker-scanner

# Construir corpus y escanear toda la organización
./scripts/run_docker_scan.sh --org my-org

# Modo lint CI en repositorio local (fallan si existen hallazgos P0)
./scripts/run_docker_scan.sh --local . --fail-on P0

# Escanear corpus existente con resolución de registros habilitada
./scripts/run_docker_scan.sh --corpus ../repo-corpus/corpus.json --resolve
```
- **Códigos de salida**: `0` Limpio (bajo el umbral), `1` Hallazgos por encima del umbral, `2` Error.
- **Salida**: Genera `report.md`, `findings.json` y `findings.sarif` en formato SARIF.

---

### 4. Analizador de Paquetes de Repos

- **Directorio**: [`skills/repo-packages-scanner`](skills/repo-packages-scanner)
- **Propósito**: Escáner estático de la fase 3. Audita GitHub Actions (`uses:`) y dependencias de paquetes en npm, PyPI, Go, Rust, Ruby y Poetry.
- **Características clave**:
  - Marca GitHub Actions no fijadas (debe usar hashes SHA de 40 caracteres, p. ej. `actions/checkout@a5ac7e5...`).
  - Detecta rangos de dependencias flotantes, ausencia de lockfiles y `npm install` en CI (en lugar de `npm ci`).
  - Detecta ejecución remota de código no fijado (`curl | bash`, `wget | sh`).
  - Incluye `run_gh_scan.sh` para escanear repos públicos de usuarios/organización de GitHub en busca de palabras clave de compromiso.

#### Invocación vía IA
> *"Comprueba si alguna de nuestras GitHub Actions usa etiquetas mutables o rangos de dependencias flotantes."*

#### Ejecución de CLI Independiente
```bash
cd skills/repo-packages-scanner

# Escanear una organización
./scripts/run_packages_scan.sh --org my-org

# Modo lint CI en repositorio local
./scripts/run_packages_scan.sh --local . --fail-on P0

# Escanear corpus con resolución de publisher de Actions via API de GitHub
./scripts/run_packages_scan.sh --corpus ../repo-corpus/corpus.json --resolve

# Escaneo de compromiso de usuario/organización
./scripts/run_gh_scan.sh username "malicious-keyword" 2026-01-01
```
- **Códigos de salida**: `0` Limpio, `1` Hallazgos por encima del umbral, `2` Error.
- **Salida**: Genera `report.md`, `findings.json`, y SARIF `findings.sarif`.

---

### 5. Análisis de Debilidades del Proyecto

- **Directorio**: [`skills/project-weakness-analysis`](skills/project-weakness-analysis)
- **Propósito**: Evalúa si los proyectos de software están listos y son seguros para la implementación en producción.
- **Características clave**:
  - **Dos ejes independientes (nunca promediados)**:
    - **Nivel de Preparación**: `production-ready` | `needs-work` | `not-ready` | `unknown`. Evalúa autenticación, manejo de errores, pruebas, CI, organización de código.
    - **Nivel de Riesgo de Seguridad**: `critical` | `high` | `medium` | `low` | `none`. Evalúa filtración de secretos, bypass de autenticación, exposición de datos personales, dependencias de la cadena de suministro no fijadas.
  - **5 modos de entrada flexibles**: árbol local (`--root`), lista explícita de directorios (`--projects`), corpus existente (`--corpus`), GitHub org/usuario (`--org`), o base de datos de proyectos (`--db`).
  - **Bucle de Nueva Auditoría**: segunda pasada verifica hallazgos previos (`resolved` | `partial` | `open`).

#### Invocación vía IA
> *"Realiza una revisión de preparación para producción y seguridad en todos los proyectos en ~/projects."*

#### Ejecución de CLI Independiente
```bash
cd skills/project-weakness-analysis

# Escanear árbol de proyectos local
./scripts/run_weakness_analysis.sh --root ~/projects

# Escanear lista explícita de directorios
./scripts/run_weakness_analysis.sh --projects ~/dev/app1 ~/dev/app2

# Escanear un corpus existente
./scripts/run_weakness_analysis.sh --corpus ../repo-corpus/corpus.json

# Combinar salidas de escaneo anteriores sin reescaneo
./scripts/run_weakness_analysis.sh --phase merge
```
- **Códigos de salida**: `0` Todos los proyectos pasaron las puertas, `1` Puertas fallidas / proyectos bloqueados, `2` Error.
- **Salida**: Generada en `./insights/`:
  - `WEAKNESS-REPORT.md` (Resumen legible)
  - `insights.json` y `security-audit.json`
  - `insights-table.csv` / `.json` (Exportación tabular plana)
  - `findings.sarif` (Formato SARIF para integración en IDE / GitHub Security)

---

## Uso de CLI independiente (Sin IA Requerido)

Todas las herramientas de `genericsuite-security` funcionan plenamente como comandos de shell y Python independientes. Requieren apenas **Python 3.8+** (sólo biblioteca estándar) y **git**.

```bash
# Ejemplo 1: Verificación rápida de seguridad en un repositorio local
cd skills/repo-packages-scanner
./scripts/run_packages_scan.sh --local /ruta/a-mi-proyecto

# Ejemplo 2: Auditoría de imágenes de contenedor
cd skills/repo-docker-scanner
./scripts/run_docker_scan.sh --local /ruta/a-mi-proyecto

# Ejemplo 3: Escaneo completo de IOC de la cadena de suministro
cd skills/supply-chain-ioc-scan
./scripts/run_scan.sh /ruta/a-mi-proyecto
```

---

## Verificación y Autoevaluación

Antes de confiar en la salida de cualquier escáner, ejecute su suite de autoevaluación integrada. Las autoevaluaciones crean fixtures de prueba sintéticos infectados para verificar que la lógica de detección captura todos los indicadores sintéticos y no genera falsos positivos en imitaciones benignas.

```bash
# Autoevaluación del escáner de IOC de la cadena de suministro
python3 skills/supply-chain-ioc-scan/tests/selftest.py

# Autoevaluación del constructor de corpus
python3 skills/repo-corpus/tests/selftest.py

# Autoevaluación del escáner docker
python3 skills/repo-docker-scanner/tests/selftest.py

# Autoevaluación del analizador de paquetes
python3 skills/repo-packages-scanner/tests/selftest.py

# Autoevaluación del análisis de debilidades
python3 skills/project-weakness-analysis/tests/selftest.py
```

---