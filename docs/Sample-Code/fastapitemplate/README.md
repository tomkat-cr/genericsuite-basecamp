# FastAPITemplate

![FastAPITemplate Logo](./ui/src/_images/app_logo_horizontal.svg)
![FastAPITemplate Bots Logo](./ui/src/_images/hack_team_logo_horizontal.svg)

**FastAPITemplate** is a full-stack application that allows you to have a template to start your FastAPI application based on GenericSuite.

## Directory Structure

```
fastapitemplate/
├── config_dbdef/                 # Configuration database definitions
├── server/                       # Server application
├── ui/                           # User interface
├── mcp-server/                   # MCP server
```

## Installation

```bash
git clone https://github.com/tomkat-cr/genericsuite-basecamp.git
cd genericsuite-basecamp/docs/Sample-Code/fastapitemplate
```

## Configuration

Run the following command to copy the example environment files to the appropriate locations:

```bash
make init-app-environment
```

Or manually copy:

```bash
cp server/.env.example server/.env
cp ui/.env.example ui/.env
```

## Running the application without Docker

```bash
# With a remote MongoDB database
make dev
```

## Running the application with Docker

Start the application and its docker containers:

```bash
# With a local MongoDB database
make run

# With a remote MongoDB database
APP_STAGE=qa make run
```

Terminate the application and its docker containers:

```bash
make down
```

Soft restart (only docker compose restart):

```bash
make restart
```

Hard restart (down and up):

```bash
make hard-restart
```

Run the local MongoDB database only:

```bash
make run-db-only
```
