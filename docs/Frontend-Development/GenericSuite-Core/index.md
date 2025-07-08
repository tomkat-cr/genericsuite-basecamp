# GenericSuite for ReactJS

<img 
    align="right"
    width="100"
    height="100"
    src="../../images/gs_logo_circle.svg"
    title="GenericSuite logo by Carlos J. Ramirez"
/>

The GenericSuite (frontend version) has a customizable CRUD editor, menu generator, login interface, API secure communication and a suite of tools to kickstart your development process.

## Features

- **Customizable CRUD editor:** core CRUD (Create-Read-Update-Delete) code that can be parametrized and extended by JSON configuration files. There's no need to rewrite code for each table editor.
- **Customizable menu:** menu and endpoints can be parametrized and extended by JSON configuration files in the backend side. The API will supply the menu estructure and security check based on the user's security group, and GenericSuite will draw the menu and available options.
- **Customizable Login Interface:** Easily adapt the login page to match your brand identity with the App logo.
- **Development and Production Scripts:** Quick commands to start development or build your application for QA, staging production environments on AWS.
- **Testing with Jest:** Comes pre-configured with Jest for running tests, including an initial test for the `<App />` component.

The perfect companion for this frontend solution is the [backend version of The GenericSuite](https://github.com/tomkat-cr/genericsuite-be).

There's a version of this library with AI features: [The GenericSuite AI](https://github.com/tomkat-cr/genericsuite-fe-ai).

## Pre-requisites

You need to install these tools:

- Node version 18+, installed via [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) or [NPM and Node](https://nodejs.org/en/download) install.
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)

## Getting Started

To get started with GenericSuite, follow these steps:

### Create the git repositories

Create the git repositories in your favorite Git Platform ([Github](https://github.com/), [Gitlab](https://gitlab.com/), [Bitbucket](https://bitbucket.org/)).

One repository is for the frontend App, and the other for the configs (JSON configuration files) to be shared between the frontend and backend repos as a Git sub-module.

Once created, open a Terminal window and change to your repositories' root directory.

Clone the repos.

E.g. for a repo called `exampleapp_frontend` created in Github:

```bash
git clone https://github.com/tomkat-cr/exampleapp_frontend.git
```

And for the configs repo called `exampleapp_configs` created in Github:

```bash
git clone https://github.com/tomkat-cr/exampleapp_configs.git
```

### Build tools

Genericsuite supports the following build tools:

* **Vite**<br/>
  Vite is a build tool that aims to provide a faster and leaner development experience for modern web projects. For more information check [Vite documentation](https://vite.dev).<br/><br/>

* **Webpack**<br/>
  At its core, Webpack is a static module bundler for modern JavaScript applications. For more information check the [Webpack documentation](https://webpack.js.org).<br/><br/>

* **Create React App**<br/>
  Create React App (CRA) is a tool that allows you to create React applications. Its development and maintenance is abandoned so we recommend use "Vite" or "Webpack". For more information check [Create React App documentation](https://create-react-app.dev).<br/><br/>

* **React-app-rewired**<br/>
  React-app-rewired is an alternative to the default Create React App. We recommend use "Vite" or "Webpack" because nowadays it's "lightly" maintained mostly by the community. For more information check [react-app-rewired documentation](https://github.com/timarney/react-app-rewired).<br/><br/>

### Initiate your project

Create the ReactJs App. E.g. `exampleapp_frontend`:

* **Vite**<br/>

```bash
npm create vite@latest exampleapp_frontend -- --template react
```

It automatically performs the `npm init` and `git init`, adds the ReactJS dependencies, and creates a default ReactJS project structure.

* **Webpack**<br/>

```bash
npm create webpack@latest exampleapp_frontend -- --template react
```

It automatically performs the `npm init` and `git init`, adds the ReactJS dependencies, and creates a default ReactJS project structure.

* **Create React App**<br/>

```bash
npx create-react-app exampleapp_frontend
```

NOTE: Check the documentation [here](https://react.dev/learn/start-a-new-react-project) for CRA (`create-react-app`) alternatives.

* **React-app-rewired**<br/>

Change to your frontend local development directory.<br/>
```bash
cd exampleapp_frontend
```

CRA (`create-react-app`) is outdated, so we use [react-app-rewired](https://www.npmjs.com/package/react-app-rewired) to customize CRA configuration with no need to eject:

```bash
npm install --save-dev react-app-rewired
```

### Install the GenericSuite package

```bash
npm install genericsuite
```

### Install additional development dependencies

```bash
npm install --save-dev \
   @babel/cli \
   @babel/core \
   @babel/plugin-proposal-class-properties \
   @babel/plugin-proposal-private-property-in-object \
   @babel/plugin-syntax-jsx \
   @babel/preset-env \
   @babel/preset-react \
   @babel/preset-stage-0 \
   @babel/preset-typescript \
   @testing-library/jest-dom \
   @testing-library/react \
   @testing-library/user-event \
   @types/jest \
   @types/react \
   babel-jest \
   babel-loader \
   babel-plugin-css-modules-transform \
   css-loader \
   file-loader \
   interpolate-html-plugin \
   jest \
   jest-environment-jsdom \
   path \
   postcss \
   postcss-loader \
   react-test-renderer \
   style-loader \
   tailwindcss \
   url-loader \
   whatwg-fetch
```

### Uninstall not required dependencies

Uninstall not required dependencies installed by CRA and included in the GenericSuite library:

```bash
npm uninstall react react-dom react-scripts web-vitals
```

### Install the build tools alone

If you have your project already initialized, e.g. with CRA, you can install the alternative build tools alone:

* **Vite**<br/>

```bash
npm install --save-dev vite @vitejs/plugin-react 
```
<!--
npm install --save-peer --strict-peer-deps vite @vitejs/plugin-react 
-->

* **Webpack**<br/>

```bash
npm install --save-dev webpack webpack-cli webpack-dev-server html-webpack-plugin interpolate-html-plugin
```
<!--
npm install --save-peer --strict-peer-deps webpack webpack-cli webpack-dev-server html-webpack-plugin interpolate-html-plugin
-->

### Prepare the Configuration Files

Copy the `.env` file template from `node_modules/genericsuite`:

```bash
cp node_modules/genericsuite/.env.example ./.env
```

And configure the variables according your needs:

* Assign `REACT_APP_APP_NAME` with your App's name.

* Assign `APP_LOCAL_DOMAIN_NAME` with the local development environment backend API domain name. E.g. app.exampleapp.local or localhost.<BR/>
Defaults to app.${REACT_APP_APP_NAME}.local (the REACT_APP_APP_NAME will be converted to all lowercase).

* Assign `FRONTEND_LOCAL_PORT` with the local development frontend port number. Defaults to 3000.

* Assign `BACKEND_LOCAL_PORT` with the local development backend API port number. Defaults to 5001.

* Assign `APP_API_URL_QA`, `APP_API_URL_STAGING`, `APP_API_URL_PROD`, and `APP_API_URL_DEMO` with the corresponding public backend API domain names for your App environments.

* Assign `APP_FE_URL_QA`, `APP_FE_URL_STAGING`, `APP_FE_URL_PROD`, and `APP_FE_URL_DEMO` with the corresponding public frontend domain names for your App environments.

* Assign `REACT_APP_URI_PREFIX` with the App URI prefix. This will be used in all environments after the domain name. E.g. https://app.exampleapp.com/exampleapp_frontend

* Configure your desired `RUN_METHOD`. Available options are "vite", "webpack" and "react-scripts". Defaults to "vite".

* Configure `RUN_PROTOCOL` with the protocol for your local development environment. Available options are "http" and "https". Defaults to "" meaning that the user must manually set the protocol when the local dev environment run starts.

* Configure `BACKEND_PATH` with the path for your backend API local development repo.

* Configure `GIT_SUBMODULE_LOCAL_PATH` and `GIT_SUBMODULE_URL` with the JSON files submodule parameters to stablish a common configuration place for both frontend and backend (used by add_github_submodules.sh).<BR/>For example files, visit: [Generic Suite Configuration Guide](https://github.com/tomkat-cr/genericsuite-fe/tree/main/src/configs)

* Configure the `AWS_*` parameters with your AWS data (used by aws_deploy_to_s3.sh and change_env_be_endpoint.sh). You'll need an AWS account.

For more information, check the comments for each variable in the [.env.example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/.env.example) file.

#### Other parameters

* `REACT_APP_X_TOKEN=1` to use 'x-access-tokens' instead of 'Authorization: Bearer'. Defaults to "0"


### Prepare the Makefile

Copy the `Makefile` template from `node_modules/genericsuite`:

```bash
cp node_modules/genericsuite/Makefile ./Makefile
```


### Change Scripts in Package.json

Open the `package.json`:

```bash
vi ./package.json
# or
# code ./package.json
```

If you want to host your frontend on **github.io**, add the homepage parameter:

```package.json
"homepage": "https://your-github-username.github.io/your-github-repository/",
```
```
NOTE: replace `your-github-username` and `your-github-repository` with your owns.
```

Add the following scripts:

```package.json
   "scripts": {
      "start": "node server.js",
      "start-build": "./node_modules/react-app-rewired/bin/react-app-rewired.js build && node server.js",
      "start-debug": "ls -lah && node server.js",
      "start-dev": "react-app-rewired start",
      "start-dev-webpack": "npx webpack-dev-server --config webpack.config.js",
      "build-prod": "webpack --mode production",
      "build-dev": "react-app-rewired build",
      "build": "react-app-rewired build",
      "eject-dev": "react-scripts eject",
      "test-dev": "react-app-rewired test",
      "test": "jest",
      "predeploy": "npm run build",
      "deploy": "gh-pages -d build"
   },
```

## App structure

This is a suggested App development repository structure:

```
.
├── .babelrc
├── .env
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── index.html
├── LICENSE
├── Makefile
├── README.md
├── babel.config.js
├── config-overrides.js
├── jest.config.cjs
├── package-lock.json
├── package.json
├── public
├── server.js
├── src
│   ├── components
│   │   ├── About
│   │   │   └── About.jsx
│   │   ├── App
│   │   │   ├── App.jsx
│   │   │   └── App.test.tsx
│   │   ├── HomePage
│   │   │   ├── HomePage.jsx
│   │   ├── ExampleMenu
│   │   │   ├── ExampleMainElement.jsx
│   │   │   └── ExampleChildElement.jsx
│   ├── constants
│   │   └── app_constants.jsx
│   ├── images
│   │   ├── app_logo_circle.svg
│   │   └── madeby_logo_square.svg
│   ├── configs
│   │   ├── CHANGELOG.md
│   │   ├── README.md
│   │   ├── backend
│   │   │   ├── app_main_menu.json
│   │   │   ├── endpoints.json
│   │   │   ├── general_config.json
│   │   │   ├── example_main_element.json
│   │   │   └── example_child_element.json
│   │   └── frontend
│   │       ├── app_constants.json
│   │       ├── general_constants.json
│   │       ├── users_profile.json
│   │       ├── example_main_element.json
│   │       └── example_child_element.json
│   ├── d.ts
│   ├── index.jsx
│   ├── input.css
│   └── setupTests.js
├── tailwind.config.js
├── tsconfig.json
├── version.txt
├── vite.config.mjs
└── webpack.config.js
```

## Configure the project

In the project's directory:

- `.babelrc` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/.babelrc))<br/><br/>

- `babel.config.js` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/babel.config.cjs))<br/>
Babel transpiler configuration. Check the [documentation here](https://babeljs.io/docs/configuration).<br/><br/>

- `CHANGELOG` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/CHANGELOG.md))<br/>
Changes documentation to this project.<br/><br/>

- `config-overrides.js` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/config-overrides.js))<br/>
React-app-rewired configuration. For more information check [react-app-rewired documentation](https://github.com/timarney/react-app-rewired).<br/><br/>

- `jest.config.cjs` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/jest.config.cjs))<br/>
JEST test configuration.<br/><br/>

- `server.js` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/server.js))<br/>
Node server, to test and debug your App in a production-like environment.<br/><br/>

- `tailwind.config.js`<br/>
Install and initialize Tailwind with [instructions here](https://tailwindcss.com/docs/installation).<br/>
For additional Tailwind configuration check the [documentation here](https://tailwindcss.com/docs/configuration).<br/><br/>

Suggested Tailwind configuration:

```js
const { relative } = require('path');

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: {
    relative: true,
    files: [
      "./node_modules/genericsuite/src/lib/**/*.{html,js,jsx}",
      "./src/lib/components/**/*.{html,js,jsx}",
      "./src/lib/constants/**/*.{html,js,jsx}",
                .
                .
      "./src/index.{tsx,jsx,cjs}",
      './public/index.html',
    ],
  },
  theme: {
    extend: {},
  },
  plugins: [
  ],
}
```

- `vite.config.mjs` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/vite.config.mjs))<br/>
Vite configuration. For more information check [Vite documentation](https://vite.dev/guide).<br/><br/>

**IMPORTANT**: if you have a `vite.config.js` file, rename it to `vite.config.mjs`. If you don't do it, Vite will not work giving errors like:
```
ERROR: [plugin: externalize-deps] Failed to resolve "@tailwindcss/vite". This package is ESM only but it was tried to load by `require`.
```

- `webpack.config.js` ([example](https://github.com/tomkat-cr/genericsuite-fe/blob/main/webpack.config.js))<br/>
To configure Webpack as an alternative to CRA / `react-app-rewired`.<br/>
**IMPORTANT**: Make sure to replace `entry: './src/index.tsx'` by `entry: './src/index.jsx'`.<br/>
Check the [documentation here](https://webpack.js.org/configuration).<br/>
<br/>

- `tsconfig.json`<br/>

To configure TypeScript. e.g.

```json
{
  "compilerOptions": {
    "outDir": "./dist",
    "module": "ESNext",
    "moduleResolution": "node",
    "target": "es5",
    "lib": [
      "es6",
      "dom"
    ],
    "sourceMap": true,
    "allowJs": true,
    "checkJs": false,
    "jsx": "react",
    "baseUrl": "./src",
    "rootDirs": [
      "src"
    ],
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "skipLibCheck": true,
    "declaration": true,
    "declarationDir": "types",
    "emitDeclarationOnly": true,
    "paths": {
      "src/*": ["./src/*"],
    }
  },
  "include": [
    "src/**/*",
  ]
}
```

## Customize index.html

### Option 1

If you don't have a customized `public/index.html` (just the default one created by CRA):

Create the `public/index.html` file:

```bash
vi public/index.html
```

Copy and paste this content:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!-- Tailwind -->
    <link href="%PUBLIC_URL%/output.css" rel="stylesheet">
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>exampleapp.com</title>
    <style>
        a { cursor: pointer; }
    </style>
    <base href="/">
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>
```

### Option 2

If you already have a `public/index.html` file customized:

Edit the `public/index.html` file:

```bash
vi public/index.html
```

Make sure to add `%PUBLIC_URL%` to these lines:

```html
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
```
```html
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
```
```html
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
```

After this line:

```html
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
```

... add this line:

```html
    <link href="%PUBLIC_URL%/output.css" rel="stylesheet">
```

Remove the footer and credits:

```html
    <!-- credits -->
    <div class="text-center">
      <p>
          <a href="https://exampleapp.com" target="_blank" rel="noreferrer">exampleapp.com</a>
      </p>
    </div>
```

### Final step for any option

Finally run this command to create the `src/output.css` file:

```bash
npx tailwindcss -i ./src/input.css -o ./src/output.css
```

And copy the file generated to the `public` directory:

```bash
cp src/output.css public/
```

To keep the `src/output.css` file updated, during the development cycle open a new terminal and run:

```bash
make tailwind
```

## Code examples and JSON configuration files

The main menu, API endpoints and CRUD editor configurations are defined in the JSON configuration files.

You can find examples about configurations and how to code an App in the [GenericSuite App Creation and Configuration guide](../../Configuration-Guide/index.md).

## Usage

## Do the first build

```bash
make build
```

### Start Development Server

To start the development server:

```bash
make run
```

### Deploy QA

Check the [Deployment Guide](../deployment.md) for details.
