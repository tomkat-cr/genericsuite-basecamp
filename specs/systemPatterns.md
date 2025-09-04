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
│  └── Configuration Templates                         │
├──────────────────────────────────────────────────────┤
│  Publishing Layer                                    │
│  ├── GitHub Pages (Primary)                          │
│  ├── ReadTheDocs (Mirror)                            │
│  └── Automated CI/CD Pipeline                        │
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
- **Decision**: Publish to both GitHub Pages and ReadTheDocs
- **Rationale**:
  - GitHub Pages: Direct integration with repository, custom domain support
  - ReadTheDocs: Better SEO, established documentation platform, backup availability
- **Trade-offs**: Requires maintaining two publishing pipelines
- **Implementation**: Automated scripts handle both deployments

#### Markdown-First Content
- **Decision**: All documentation written in Markdown with minimal HTML
- **Rationale**:
  - Version control friendly
  - Easy for contributors to edit
  - Portable across different documentation systems
  - Good tooling support
- **Extensions**: Use pymdown-extensions for enhanced Markdown features

### Example Application Architecture

#### Monorepo with TurboRepo
- **Decision**: Use TurboRepo for monorepo management in ExampleApp
- **Rationale**:
  - Efficient build caching and parallelization
  - Clear dependency management between packages
  - Demonstrates modern development practices
  - Scales well as example grows
- **Trade-offs**: More complex initial setup, learning curve for contributors
- **Alternative**: Lerna, Nx, or separate repositories

#### Multiple Backend Implementations
- **Decision**: Provide FastAPI, Flask, Chalice, and MCP Server implementations
- **Rationale**:
  - Demonstrates GenericSuite framework abstraction
  - Shows real-world deployment flexibility
  - Provides options for different use cases
  - Validates GenericSuite design across frameworks
- **Trade-offs**: Increased maintenance overhead, more complex testing
- **Pattern**: Shared business logic, framework-specific adapters

#### Environment-Based Configuration
- **Decision**: Use .env files with comprehensive .env.example templates
- **Rationale**:
  - Clear separation of configuration from code
  - Easy local development setup
  - Secure handling of sensitive information
  - Consistent across all backend implementations
- **Implementation**: Detailed .env.example files with inline documentation

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

#### Automated Pipeline
- **Pattern**: Fully automated build and deployment process
- **Implementation**:
  - Git hooks trigger documentation builds
  - Automated testing of example applications
  - Parallel deployment to multiple targets
- **Benefits**: Consistent releases, reduced manual errors

#### Content Validation
- **Pattern**: Automated validation of documentation content
- **Implementation**:
  - Link checking for internal and external links
  - Code example testing
  - Markdown linting and formatting
- **Benefits**: Higher quality documentation, fewer broken experiences

## Component Relationships

### Documentation Components

#### Content Hierarchy
```
docs/
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
│   ├── _components/ (React components)
│   ├── _constants/ (Configuration constants)
│   └── _images/ (UI assets)
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