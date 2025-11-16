# Technical Context - GenericSuite Basecamp

## Technologies Used

### Documentation Stack

#### Core Documentation Framework
- **MkDocs 1.6.1**: Static site generator for project documentation
  - **Purpose**: Converts Markdown files to static HTML documentation site
  - **Configuration**: `mkdocs.yml` with Material theme and plugins
  - **Extensions**: pymdown-extensions for enhanced Markdown features

- **Material for MkDocs 9.6.16**: Modern documentation theme
  - **Features**: Responsive design, search, navigation, dark mode
  - **Customization**: Custom CSS in `docs/stylesheets/extra.css`
  - **Icons**: FontAwesome integration for consistent iconography

#### Documentation Plugins
- **mkdocs-git-committers**: Shows contributors for each page
- **mkdocs-print-site-plugin**: Generates printable PDF version
- **search plugin**: Built-in search functionality
- **pymdown-extensions**: Enhanced Markdown syntax support

#### Content Management
- **Markdown**: Primary content format with YAML frontmatter
- **YAML**: Configuration files and structured data
- **Jinja2 3.1.6**: Template engine for dynamic content generation
- **Python-Markdown 3.8.2**: Markdown processing with extensions

### Example Application Stack

#### Frontend Technologies
- **React 18+**: Modern React with hooks and functional components
- **Vite**: Primary build tool for fast development and optimized builds
- **Webpack**: Alternative build tool option for compatibility
- **TypeScript**: Type-safe JavaScript development
- **Tailwind CSS**: Utility-first CSS framework replacing Bootstrap
- **ESLint + Prettier**: Code linting and formatting

#### Backend Framework Options
- **FastAPI**: Modern Python web framework with automatic API documentation
  - **Port**: 5011 (configurable via BACKEND_LOCAL_PORT)
  - **Features**: Async support, automatic OpenAPI generation, type hints
  
- **Flask**: Lightweight Python web framework
  - **Port**: 5021 (configurable via BACKEND_LOCAL_PORT)
  - **Features**: Minimal setup, extensive ecosystem, flexible architecture
  
- **AWS Chalice**: Serverless framework for AWS Lambda
  - **Port**: 5001 (configurable via BACKEND_LOCAL_PORT)
  - **Features**: AWS integration, automatic deployment, serverless architecture
  
- **MCP Server**: Model Context Protocol server implementation
  - **Purpose**: Demonstrates modern AI integration patterns
  - **Features**: Food and nutrition management tools

#### Database Options
- **MongoDB**: Document-based NoSQL database
  - **Local**: MongoDB Community Server
  - **Cloud**: MongoDB Atlas
  - **Driver**: PyMongo for Python integration
  
- **DynamoDB**: AWS managed NoSQL database
  - **Local**: DynamoDB Local for development
  - **Cloud**: AWS DynamoDB
  - **SDK**: Boto3 for AWS integration

#### Package Management
- **pnpm 10.12.4+**: Efficient package manager for Node.js
  - **Features**: Workspace support, fast installs, disk space efficiency
  - **Configuration**: `pnpm-workspace.yaml` for monorepo management
  
- **TurboRepo**: Build system for monorepos
  - **Features**: Incremental builds, remote caching, parallel execution
  - **Configuration**: `turbo.json` for build orchestration
  
- **Pipenv**: Python dependency management
  - **Features**: Virtual environment management, lock files, security scanning
  - **Files**: `Pipfile` and `Pipfile.lock` for reproducible builds

### Development Tools

#### Version Control and CI/CD
- **Git**: Version control with conventional commit messages
- **GitHub**: Repository hosting, issue tracking, automated workflows
- **GitHub Actions**: Automated testing and deployment (implied)

#### Code Quality Tools
- **ESLint**: JavaScript/TypeScript linting with custom configurations
- **Prettier**: Code formatting for consistent style
- **Black**: Python code formatting
- **flake8**: Python linting and style checking

#### Testing Frameworks
- **pytest**: Python testing framework with fixtures and plugins
- **Jest**: JavaScript testing framework for React components
- **React Testing Library**: Testing utilities for React components

#### Development Environment
- **Node.js 20+**: JavaScript runtime (version specified in `.nvmrc`)
- **Python 3.10+**: Python runtime (version specified in `.python-version`)
- **Make**: Build automation and task runner
- **Shell Scripts**: Bash scripts for common development tasks

## Development Setup

### Prerequisites Installation

#### System Requirements
```bash
# Node.js via NVM (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 20
nvm use 20

# Python via pyenv (recommended)
curl https://pyenv.run | bash
pyenv install 3.12
pyenv global 3.12

# Package managers
npm install -g pnpm
pip install pipenv

# Build tools (macOS)
brew install make
```

#### Development Tools
```bash
# AWS CLI (if using AWS services)
brew install awscli
aws configure

# MongoDB (if using MongoDB)
brew tap mongodb/brew
brew install mongodb-community

# Docker (for containerized development)
brew install docker
```

### Repository Setup

#### Initial Setup
```bash
# Clone repository
git clone https://github.com/tomkat-cr/genericsuite-basecamp.git
cd genericsuite-basecamp

# Install documentation dependencies
make install

# Set up example application
make exampleapp-install
```

#### Environment Configuration
```bash
# Copy environment templates
cp docs/Sample-Code/exampleapp/apps/ui/.env.example docs/Sample-Code/exampleapp/apps/ui/.env
cp docs/Sample-Code/exampleapp/apps/api-fastapi/.env.example docs/Sample-Code/exampleapp/apps/api-fastapi/.env
# Repeat for other backend options as needed

# Edit environment variables
# Configure database connections, API keys, etc.
```

### Development Workflow

#### Documentation Development
```bash
# Start local documentation server
make serve
# or
make run

# Build documentation
make build

# Deploy documentation
make transfer
```

#### Example Application Development
```bash
# Start all services
make exampleapp-run

# Install/update dependencies
make exampleapp-install
make exampleapp-update

# Clean build artifacts
make exampleapp-clean

# Generate SSL certificates for HTTPS
make exampleapp-create-ssl-certs
```

## Technical Constraints

### Platform Constraints
- **Operating System**: Primarily developed on macOS, compatible with Linux
- **Node.js Version**: Requires Node.js 20+ for Tailwind CSS v4 and Shadcn v2+ compatibility
- **Python Version**: Requires Python 3.10+ and < 4.0 for GenericSuite compatibility
- **Browser Support**: Modern browsers with ES6+ support

### Performance Constraints
- **Documentation Site**: Must load quickly, optimized for mobile
- **Example Applications**: Should start in under 30 seconds on modern hardware
- **Build Times**: Documentation builds should complete in under 2 minutes
- **Memory Usage**: Development environment should work with 8GB RAM

### Security Constraints
- **Environment Variables**: Sensitive data must be in .env files, never committed
- **Dependencies**: Regular security scanning of npm and pip packages
- **HTTPS Support**: All production deployments must support HTTPS
- **API Keys**: Must be configurable per environment, with clear documentation

### Compatibility Constraints
- **GenericSuite Versions**: Must maintain compatibility with current GenericSuite packages
- **Framework Versions**: Backend examples must work with specified framework versions
- **Database Versions**: Must support current versions of MongoDB and DynamoDB
- **Browser Compatibility**: Must work in browsers from last 2 years

## Dependencies

### Documentation Dependencies
```python
# Core documentation (requirements.txt)
mkdocs==1.6.1
mkdocs-material==9.6.16
mkdocs-material-extensions==1.3.1
pymdown-extensions==10.16.1

# Plugins
mkdocs-git-committers
mkdocs-print-site-plugin

# Build tools
Jinja2==3.1.6
Markdown==3.8.2
PyYAML==6.0.2
```

### Example Application Dependencies

#### Frontend Dependencies (package.json)
```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "genericsuite": "latest",
    "genericsuite-ai": "latest"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "typescript": "^5.0.0",
    "tailwindcss": "^4.0.0",
    "eslint": "^8.0.0",
    "prettier": "^3.0.0"
  }
}
```

#### Backend Dependencies (Pipfile)
```toml
[packages]
genericsuite = "*"
genericsuite-ai = "*"
fastapi = "*"  # or flask, chalice
uvicorn = "*"  # for FastAPI
gunicorn = "*"  # for Flask
boto3 = "*"    # for AWS services
pymongo = "*"  # for MongoDB

[dev-packages]
pytest = "*"
black = "*"
flake8 = "*"
```

### External Service Dependencies
- **GitHub**: Repository hosting, issue tracking, GitHub Pages
- **ReadTheDocs**: Mirror documentation hosting
- **NPM Registry**: Frontend package distribution
- **PyPI**: Python package distribution
- **AWS Services**: DynamoDB, Lambda, S3 (optional)
- **MongoDB Atlas**: Cloud database service (optional)

## Tool Usage Patterns

### Documentation Workflow
1. **Content Creation**: Write Markdown files in `docs/` directory
2. **Local Preview**: Use `make serve` for live preview during development
3. **Build Validation**: Use `make build` to test static site generation
4. **Publishing**: Use `make transfer` for automated deployment
5. **Quality Assurance**: Automated link checking and content validation

### Example Application Workflow
1. **Environment Setup**: Copy and configure .env files
2. **Dependency Management**: Use `make exampleapp-install` for setup
3. **Development**: Use `make exampleapp-run` for live development
4. **Testing**: Run individual test suites for each backend
5. **Cleanup**: Use `make exampleapp-clean` to reset environment

### Code Quality Workflow
1. **Linting**: Automated linting on file save and pre-commit
2. **Formatting**: Automatic code formatting with Prettier/Black
3. **Type Checking**: TypeScript compilation and Python type hints
4. **Testing**: Automated test execution on code changes
5. **Security**: Regular dependency vulnerability scanning

### Release Management Workflow
1. **Version Planning**: Coordinate with GenericSuite package releases
2. **Documentation Updates**: Update all relevant documentation sections
3. **Example Updates**: Modify ExampleApp to demonstrate new features
4. **Testing**: Comprehensive testing across all supported configurations
5. **Publishing**: Automated deployment with version tagging

### Monitoring and Maintenance
1. **Link Checking**: Regular validation of internal and external links
2. **Dependency Updates**: Monthly review and update of dependencies
3. **Performance Monitoring**: Regular assessment of site performance
4. **User Feedback**: Monitor GitHub issues and community feedback
5. **Analytics**: Track documentation usage patterns and popular content

## Environment Configuration

### Development Environment Variables
```bash
# Documentation
DEBUG=true                    # Enable debug mode for local development
MKDOCS_SERVE_PORT=8000       # Port for local documentation server

# Example Application - UI
REACT_APP_API_URL=http://localhost:5011  # Backend API URL
REACT_APP_USE_HTTPS=false    # Enable HTTPS in development
RUN_METHOD=vite              # Build tool (vite or webpack)
RUN_PROTOCOL=http            # Protocol (http or https)

# Example Application - Backend
DATABASE_TYPE=mongodb        # Database type (mongodb or dynamodb)
MONGODB_URI=mongodb://localhost:27017/exampleapp
AWS_REGION=us-east-1        # AWS region for DynamoDB
DEBUG_MODE=true             # Enable debug logging
```

### Production Environment Variables
```bash
# Documentation
SITE_URL=https://genericsuite.carlosjramirez.com
GOOGLE_ANALYTICS_ID=G-HL2GMT09NW

# Example Application
REACT_APP_API_URL=https://api.example.com
DATABASE_TYPE=mongodb
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/prod
AWS_REGION=us-east-1
DEBUG_MODE=false
```

### Security Configuration
- **API Keys**: Stored in environment variables, never in code
- **Database Credentials**: Secured through environment variables or cloud secrets
- **SSL Certificates**: Generated locally for development, managed by cloud providers in production
- **CORS Settings**: Configured per environment for appropriate access control