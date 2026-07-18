# GenericSuite Scripts for Frontend Development

[GenericSuite Scripts (frontend version)](https://github.com/tomkat-cr/genericsuite-fe-scripts) is a suite of features to enhance the ReactJS App development process.

This repository contains the frontend scripts necessary to build and deploy ReactJS Apps made by [GenericSuite (frontend version)](../GenericSuite-Core/index.md) and [GenericSuite AI (frontend version)](../GenericSuite-AI/index.md).

## Features

- **Development and Production Scripts:** Quick commands to start development or build your application for QA, staging production environments on AWS.
- **AWS Deployment**: Deployment to AWS as Cloudfront website with S3 bucket.
- **Local Development Environment**: running with http or https, with or without Docker.
- **Common JSON config management**: to add the Git Submodule with the common JSON config directories.

## Getting Started

To get started with GenericSuite Scripts (frontend version), follow these steps:

### Install the GenericSuite Frontend Scripts

```bash
npm init
```

```bash
npm install -D genericsuite-fe-scripts
```

### Prepare the Makefile

Copy the `Makefile` template from `node_modules/genericsuite-fe-scripts`:

```bash
cp node_modules/genericsuite-fe-scripts/Makefile ./Makefile
```

### Initiate your project

Check [The GenericSuite Getting Started guide](../GenericSuite-Core/index.md#getting-started) for more details.

## Usage

### Start Development Server

To start the development server:

```bash
make run
```

## Do the first build

```bash
make build
```

### Deploy to QA, Staging, Demo and Production environments

Check the [Deployment Guide](../deployment.md) for details.
