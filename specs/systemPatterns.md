# System Patterns - GenericSuite Basecamp

## System Architecture

### Overall Architecture Pattern

GenericSuite Basecamp follows a **Documentation-as-Code** architecture pattern, where documentation is treated as a first-class citizen alongside code, with automated publishing, version control, and testing.

```
┌──────────────────────────────────────────────────────┐
│               GenericSuite Basecamp                  │
├──────────────────────────────────────────────────────┤
│  Documentation Layer (MkDocs + Material Theme)       │
│  ├── Configuration Guides                            │
│  ├── API Documentation                               │
│  ├── Tutorial Content                                │
│  └── Release Notes                                   │
├──────────────────────────────────────────────────────┤
│  Example Applications Layer                          │
│  ├── ExampleApp Monorepo (TurboRepo + pnpm)          │
│  │   ├── Frontend (React + Vite/Webpack)             │
│  │   ├── Backend Options (FastAPI/Flask/Chalice/MCP) │
│  │   ├── Database Configs (MongoDB/DynamoDB)         │
│  │   └── Shared Packages                             │
│  ├── FastAPITemplate Monorepo (npm workspace)        │
│  │   ├── Frontend (React + Vite/Webpack)             │
│  │   ├── Backend Options (FastAPI)                   │
│  │   └── Database Configs (MongoDB/DynamoDB)         │
│  ├── AWS and other cloud deployment templates        │
│  ├── Configuration Guide Assets                      │
│  └── Configuration Templates                         │
├──────────────────────────────────────────────────────┤
│  Publishing Layer                                    │
│  ├── Website FTP (Primary)                           │
│  └── ReadTheDocs (Mirror, automatically updated)     │
└──────────────────────────────────────────────────────┘
```

### Component Relationships

#### Documentation Ecosystem
- **MkDocs Core**: Static site generator with Python-based configuration
- **Material Theme**: Provides modern UI/UX with search, navigation, and responsive design
- **Content Sources**: Markdown files organized by feature area and audience
- **Asset Management**: Images, PDFs, and other media assets organized by context

#### Example Application Architecture
- **Monorepo Structure**: Single repository containing multiple related applications
- **Package Management**: pnpm for efficient dependency management and workspace support
- **Build Orchestration**: TurboRepo for coordinated builds and caching
- **Framework Flexibility**: Multiple backend implementations demonstrating GenericSuite patterns

## Key Technical Decisions

### Documentation Technology Stack

#### MkDocs + Material Theme
- **Decision**: Use MkDocs with Material theme for documentation site
- **Rationale**: 
  - Python-based (aligns with GenericSuite backend)
  - Excellent search capabilities
  - Mobile-responsive design
  - Strong plugin ecosystem
  - Easy customization
- **Trade-offs**: Less flexibility than custom solutions, but much faster to implement
- **Alternatives Considered**: GitBook, Docusaurus, custom React app

#### Dual Publishing Strategy
- **Decision**: Publish to both FTP and ReadTheDocs
- **Rationale**:
  - FTP: Direct integration with GenericSuite website, custom domain support
  - ReadTheDocs: Better SEO, established documentation platform, backup availability
- **Trade-offs**: Requires manual deployment triggering to FTP
- **Implementation**: Once a new release is created from the "main" branch of the GitHub repo, the documentation is automatically published to ReadTheDocs

#### Markdown-First Content
- **Decision**: All documentation written in Markdown with minimal HTML
- **Rationale**:
  - Version control friendly
  - Easy for contributors to edit
  - Portable across different documentation systems
  - Good tooling support
- **Extensions**: Use pymdown-extensions for enhanced Markdown features

### Example Application Architecture

#### ExampleApp

##### Monorepo with TurboRepo
- **Decision**: Use TurboRepo for monorepo management in ExampleApp
- **Rationale**:
  - Efficient build caching and parallelization
  - Clear dependency management between packages
  - Demonstrates modern development practices
  - Scales well as example grows
- **Trade-offs**: More complex initial setup, learning curve for contributors
- **Alternative**: Lerna, Nx, or separate repositories

##### Multiple Backend Implementations
- **Decision**: Provide FastAPI, Flask, Chalice, and MCP Server implementations
- **Rationale**:
  - Demonstrates GenericSuite framework abstraction
  - Shows real-world deployment flexibility
  - Provides options for different use cases
  - Validates GenericSuite design across frameworks
- **Trade-offs**: Increased maintenance overhead, more complex testing
- **Pattern**: Shared business logic, framework-specific adapters

##### Environment-Based Configuration
- **Decision**: Use .env files with comprehensive .env.example templates
- **Rationale**:
  - Clear separation of configuration from code
  - Easy local development setup
  - Secure handling of sensitive information
  - Consistent across all backend implementations
- **Implementation**: Detailed .env.example files with inline documentation

#### FastAPITemplate

##### Monorepo with npm workspace
- **Decision**: Use npm workspace for monorepo management in FastAPITemplate
- **Rationale**:
  - Efficient build caching and parallelization
  - Clear dependency management between packages
  - Demonstrates modern development practices
  - Scales well as example grows
- **Trade-offs**: Learning curve for contributors
- **Alternative**: Lerna, Nx, or separate repositories

##### Modern Backend Implementation
- **Decision**: Provide FastAPI implementation templete to be used as a base for new projects
- **Rationale**:
  - Demonstrates GenericSuite framework abstraction
  - Shows real-world deployment flexibility
  - Provides options for different use cases
  - Validates GenericSuite design with a modern backend implementation
- **Trade-offs**: there's no flask and/or chalice implementation, only FastAPI. No database or application specific example like the ExampleApp that has a Calorie Counter application
- **Pattern**: framework-specific adapters. Empty endpoints, menu, forms, etc. can be generated by the `config-builder` skill

##### Environment-Based Configuration
- **Decision**: Use a single .env file with a comprehensive .env.example template for both frontend and backend
- **Rationale**:
  - Clear separation of configuration from code
  - Easy local development setup
  - Secure handling of sensitive information
  - Consistent across frontend and backend
  - The run script `make dev` handle the root .env file copy to the frontend and backend before executing the `dev` command
- **Trade-offs**: if the root .env file changes, the user must run `make dev` again to update the frontend and backend .env files
- **Implementation**: Detailed .env.example file with inline documentation

## Design Patterns in Use

### Documentation Patterns

#### Progressive Disclosure
- **Pattern**: Start with overview, drill down to specifics
- **Implementation**: 
  - Main index provides high-level overview
  - Section indices provide feature summaries
  - Individual pages provide detailed implementation
- **Benefits**: Reduces cognitive load, supports different user needs

#### Working Examples First
- **Pattern**: Lead with functional code, explain concepts after
- **Implementation**:
  - Every feature has a working example in ExampleApp
  - Code snippets are tested and functional
  - Configuration examples are complete and accurate
- **Benefits**: Faster time-to-value, builds confidence

#### Cross-Reference Architecture
- **Pattern**: Extensive linking between related concepts
- **Implementation**:
  - Internal links between documentation sections
  - Links to relevant GitHub repositories
  - Links to published packages
  - Links to external resources
- **Benefits**: Helps users discover related functionality

### Code Organization Patterns

#### Framework Abstraction Layer
- **Pattern**: Common interface across different backend frameworks
- **Implementation**:
  - Shared business logic in lib/ directories
  - Framework-specific adapters in framework directories
  - Common configuration patterns across implementations
- **Benefits**: Demonstrates GenericSuite value proposition

#### Configuration as Code
- **Pattern**: All configuration managed through version-controlled files
- **Implementation**:
  - .env.example files with comprehensive documentation
  - JSON configuration files for database schemas
  - YAML files for deployment configurations
- **Benefits**: Reproducible setups, clear change tracking

#### Layered Architecture
- **Pattern**: Clear separation between presentation, business logic, and data layers
- **Implementation**:
  - Frontend components separate from business logic
  - Backend endpoints separate from data access
  - Database abstraction layer for multiple database types
- **Benefits**: Maintainable code, easier testing, clear responsibilities

### Publishing Patterns

#### Script-Driven Pipeline
- **Pattern**: Make-based script automation for consistent manual deployments
- **Implementation**:
  - Developers run explicit commands (`make build`, `make transfer`) to trigger documentation builds
  - Shell scripts handle the complexity of FTP transfers and temporary file management
  - GitHub releases trigger ReadTheDocs updates
- **Benefits**: Reliable deployment process that avoids raw manual file copying

#### Future-Ready Structure
- **Pattern**: Structured commands that can easily transition to CI/CD
- **Implementation**:
  - All complex logic is mapped to Make targets
  - Scripts are environment-variable driven
- **Benefits**: Prepares the repository for fully automated pipelines in the future


## Component Relationships

### Documentation Components

#### Content Hierarchy
```
docs/en/
├── index.md (Main entry point)
├── Frontend-Development/ (Frontend-specific guides)
├── Backend-Development/ (Backend-specific guides)
├── Configuration-Guide/ (Setup and configuration)
├── Sample-Code/ (Working examples)
├── Releases/ (Version history and changelogs)
└── Other/ (Supplementary content)
```

#### Navigation Structure
- **Top-level navigation**: Major functional areas
- **Section navigation**: Features within each area
- **Page navigation**: Sections within each page
- **Cross-references**: Related content across sections

#### Asset Organization
- **Images**: Organized by feature area, optimized for web
- **Documents**: PDFs and presentations in dedicated directory
- **Code samples**: Embedded in documentation, tested separately

### Example Application Components

#### Frontend Architecture
```
apps/ui/
├── src/
│   ├── components/ (React components)
│   ├── constants/ (Configuration constants)
│   └── images/ (UI assets)
├── public/ (Static assets)
└── build/ (Generated output)
```

#### Backend Architecture (per framework)
```
apps/api-{framework}/
├── lib/ (Business logic)
├── chalicelib/ or routers/ (Framework-specific code)
├── tests/ (Test suites)
└── scripts/ (Deployment and utility scripts)
```

#### Shared Components
```
packages/
├── eslint-config/ (Shared linting rules)
├── typescript-config/ (Shared TypeScript configuration)
└── ui/ (Shared UI components)
```

## Critical Implementation Paths

### Documentation Publishing Flow

1. **Content Creation**: Markdown files created/updated in docs/ directory
2. **Local Testing**: `make serve` runs local MkDocs server for preview
3. **Build Process**: `make build` generates static site in site/ directory
4. **Deployment**: `make transfer` publishes to GitHub Pages and ReadTheDocs
5. **Validation**: Automated checks verify links and content integrity

### Example Application Development Flow

1. **Environment Setup**: Copy .env.example files, configure variables
2. **Dependency Installation**: `make exampleapp-install` sets up all dependencies
3. **Development**: `make exampleapp-run` starts all services in development mode
4. **Testing**: Individual backend tests validate functionality
5. **Documentation**: Changes reflected in documentation automatically

### Release Management Flow

1. **Version Planning**: Coordinate with GenericSuite package releases
2. **Documentation Updates**: Update guides for new features/changes
3. **Example Updates**: Modify ExampleApp to demonstrate new capabilities
4. **Testing**: Validate all examples work with new versions
5. **Publishing**: Release documentation and update package references

### Community Contribution Flow

1. **Issue Creation**: Contributors identify documentation gaps or errors
2. **Fork and Branch**: Standard GitHub fork/branch workflow
3. **Local Development**: Contributors can run full documentation site locally
4. **Pull Request**: Changes submitted with clear description
5. **Review and Merge**: Maintainer review, automated testing, merge
6. **Deployment**: Automatic publication of approved changes

## Integration Points

### External Systems
- **GitHub**: Source control, issue tracking, automated workflows
- **ReadTheDocs**: Mirror documentation hosting with webhook integration
- **NPM/PyPI**: Package registries for GenericSuite components
- **AWS/MongoDB**: Cloud services demonstrated in examples

### Internal Systems
- **MkDocs Plugins**: Search, navigation, git integration, print support
- **Build Tools**: TurboRepo, pnpm, Python packaging tools
- **Testing Frameworks**: pytest for Python, Jest for JavaScript
- **Linting Tools**: ESLint, Prettier, Black, flake8

### Data Flow
- **Documentation**: Markdown → MkDocs → Static HTML → Web hosting
- **Examples**: Source code → Build tools → Running applications
- **Configuration**: Templates → User customization → Working applications
- **Feedback**: User issues → Documentation updates → Improved experience