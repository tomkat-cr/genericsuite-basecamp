## Directory Structure

```
genericsuite-basecamp/
├── docs/                            # MkDocs content (source of truth)
│   ├── en/                          # English documentation
│   ├── es/                          # Spanish documentation
│   ├── code/                        # Code examples
│   │   ├── configuration-guide/     # Configuration guide validation rules files
│   │   ├── exampleapp/              # ExampleApp monorepo
│   │   │   ├── apps/                # exampleapp turborepo apps
│   │   │   │   ├── api-fastapi/     # FastAPI backend
│   │   │   │   ├── api-flask/       # Flask backend
│   │   │   │   ├── api-chalice/     # AWS Chalice backend
│   │   │   │   ├── config_dbdef/    # GenericSuite database/forms configuration files
│   │   │   │   ├── mcp-server/      # MCP Server backend
│   │   │   │   └── ui/              # React frontend
│   │   │   ├── assets/              # exampleapp documentation assets (images)
│   │   │   ├── packages/            # exampleapp turborepo packages
│   │   │   └── scripts/             # exampleapp specific scripts
│   │   ├── fastapitemplate/         # FastAPI Template monorepo
│   │   │   ├── assets/              # fastapitemplate documentation assets (images)
│   │   │   ├── config_dbdef/        # GenericSuite database/forms configuration files
│   │   │   ├── deploy/              # Docker/Podman containerization deployment
│   │   │   ├── scripts/             # fastapitemplate specific scripts
│   │   │   ├── server/              # FastAPI backend
│   │   │   └── ui/                  # React frontend
│   │   ├── genericsuite-be-scrips/  # Backend script templates for AWS deployments
│   │   └── genericsuite-configs/    # GenericSuite configuration JSON file examples
│   └── stylesheets/                 # Custom CSS
├── docs_for_ftp/                    # Mirror copy for FTP publishing (temporary files)
├── specs/                           # Project memory bank (context docs)
├── scripts/                         # Build, deploy, translation scripts
├── mkdocs.yml                       # MkDocs configuration
└── Makefile                         # All task automation
```
