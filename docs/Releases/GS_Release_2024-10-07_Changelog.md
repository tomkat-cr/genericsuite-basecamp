# 20241007 - GenericSuite debut presentation at the UPB Medellin

![GS_Release_2024-10-07_Image_4 - The FynBots.jpg](./images/GS_Release_2024-10-07_Image_4%20-%20The%20FynBots.jpg)

Release Date: 2024-10-07

## Summary

October 7th, 2024, marks a milestone with the release of the latest version of GenericSuite, an advanced software library designed for both backend and frontend app development using Python and React.js. This update brings a variety of enhancements and new features that promise to increase efficiency and boost developers' workflows.

Among the highlights is the addition of DynamoDB abstraction, Flux.1, Groq, Amazon Bedrock interfaces, Claude 3.5 Sonnet, 100% #Tailwind, dark mode and a configurable sidebar menu, allowing for a more personalized user experience. We've also introduced the "GsIcons" library, replacing FontAwesome, to offer a more modern and coherent aesthetic.

In the frontend realm, we've fully embraced Tailwind CSS, eliminating the dependency on react-bootstrap, which optimizes performance and user interface customization. Additionally, significant improvements have been made to chatbot responsiveness, ensuring smoother and more effective interactions.

On the backend, DynamoDb database abstraction capabilities have been enhanced, and new AI functionalities have been introduced, including image generators and advanced chat models: Flux.1 image generator, Groq and Amazon Bedrock platform interfaces, and the most recent Claude 3.5 Sonnet model implementation.

GenericSuite continues to evolve, providing tools that facilitate agile and effective application development, adapting to the ever-changing needs of the tech market. Explore all the new capabilities and transform your application development approach today.

## GenericSuite Frontend Core

### Package, pull request and tag

* Tag: https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.22
* PR: https://github.com/tomkat-cr/genericsuite-fe/pull/4
* Package: https://www.npmjs.com/package/genericsuite/v/1.0.22

### Changelog

#### 1.0.22 (2024-10-07)
---

##### New
Add Darkmode [GS-63].
Add Configurable sidebar menu [GS-114].
Add localstorage generic functions [GS-112].
Add Save darkmode and side menu set to localstorage [GS-112].
New "GsIcons" library replaces FontAwesome [GS-115].
Add landscape logo to the App header [GS-63].
Add the optional "template" attribute to app_main_menu.json entries to customize the menu option design [GS-112] [GS-129].
Add the <NoDesignComponent>> to have menu options with no GS FE Core design [GS-112] [GS-129].
Add testHelpersMocks export [GS-129].

##### Changes
Replace react-bootstrap entirely and use only Tailwind CSS [GS-63].
Delete local storage PII [GS-2]
Change the behavior of actions so that they appear when clicking on the line in the GCE_RFC (generic CRUD editor) listing page [GS-112].
Change the color when hovering over the line in the GCE_RFC listing page [GS-112].
Change lines with different colors if they are even/odd in the GCE_RFC listing page [GS-112].
Improve data page layout by implementing Tailwind constants in the GCE_RFC [GS-112].
Change Search input box size too small in the GCE_RFC listing page [GS-112].
<HashRouter> was replaced by <RouterProvider> and createBrowserRouter() [GS-112].
"/login" replaced by "/logout" in the Log Out option [GS-112].
Add "openai_api_key" and "openai_model" fields  to user and user_profile json default configs [FA-200] [FA-201].
<PrivateRoute/> avoid use getPrefix(true) [GS-112].
Rename "test-helpers/mock-fetch.ts" to "test-helpers/mocks.js" to make it more generic and change the ".ts" extension by ".js" to fix the "Parameter 'data' implicitly has an 'any' type | export function mockFetch(data)..." error during the "make publish" [GS-129].

##### Fixes
Fix missing classes in the new output.css of Tailwind v3.4.9 [GS-63].
Fix the row values in index page not shown issue [GS-108].
Fix the %PUBLIC_URL% issue in public/index.html file running the app with webpack [GS-116].
Fix show WaitAnimation() in iterateChildComponents() and EditFormFormik() to make the data loading evident in the User Profile menu option [GS-112].

##### Breaks
Bootstrap CSS is not longer used [GS-63].
FontAwesome is not longer used [GS-115].
SVG images removed and included in the "GsIcons" library [GS-115].
Get rid of eval() in the GS FrontEnd [GS-127].


## GenericSuite Frontend AI

### Package, pull request and tag

* Tag: https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.20
* PR: https://github.com/tomkat-cr/genericsuite-fe-ai/pull/4
* Package: https://www.npmjs.com/package/genericsuite-ai/v/1.0.20

### Changelog

#### 1.0.20 (2024-10-07)
---

##### New
New "GsIcons" library replaces FontAwesome [GS-115].

##### Changes
Update GS FE AI with GS FE Core Tailwind conversion and new contexts [GS-129].
<HashRouter> was replaced by <RouterProvider> and createBrowserRouter() [GS-112].
Chatbot camera, voice and clip icons changed to "m" size [GS-129].
Chatbot design enhanced and responsive behavior fixed [GS-129].
Delete button in the Chatbot conversation list shows only when the mouse pointer is over the conversation [GS-129].

##### Fixes
Fix missing classes in the new output.css of Tailwind v3.4.9 [GS-63].
Fix the %PUBLIC_URL% issue in public/index.html file running the app with webpack [GS-116].
Fix when Chatbot send an error and Close button is clicked, no further info is displayed in the message area [GS-129].
Fix click in Chatbot conversation list item only works if the text is clicked, not the padding area [GS-129].
Fix Chatbot <UserInput> location is wrong with the new GS FE Core and pure Tailwind, also should work when the <NoDesignComponent> template is used [GS-129].
Fix all test to be compatible with new GS FE Core contexts and constants [GS-112] [GS-129].
Remove all links references to "/#" [GS-112].
Restrict the source code exported to dist in "make publish".
Formik version fixed to 2.4.5 in package.json to avoid GCE_RFC warning when the +New button is clicked [GS-112].

##### Breaks
Bootstrap CSS is not longer used [GS-63].
FontAwesome is not longer used [GS-115].
SVG images removed and included in the "GsIcons" library [GS-115].


## GenericSuite Backend Core

### Package, pull request and tag

* Tag: https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.9
* PR: https://github.com/tomkat-cr/genericsuite-be/pull/7
* Package: https://pypi.org/project/genericsuite/0.1.9/

### Changelog

#### 0.1.9 (2024-10-07)
---

##### New
Add "/users/current_user_d" endpoint [GS-2].
Add GS_LOCAL_ENVIR envvar to detect a local database running in a docker container [GS-102].

##### Changes
Make DynamoDb tables with prefix work with the GS DB Abstraction [GS-102].
Add error handling to all GenericDbHelper methods [GS-102].
DynamoDB abstraction "update_one()" method handles update_one, replace_one, $addToSet and $pull operations [GS-102].
App logger shows LOCAL condition and database engine.
Botocore upgraded to "^1.35.20" [GS-128].
S3transfer upgraded to "^0.10.0" [GS-128].

## GenericSuite Backend AI

### Package, pull request and tag

* Tag: https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.10
* PR: https://github.com/tomkat-cr/genericsuite-be-ai/pull/6
* Package: https://pypi.org/project/genericsuite-ai/0.1.10/

### Changelog

#### 0.1.10 (2024-10-07)
---

##### New
Implement HF (HuggingFace) local pipelines [GS-59].
Implement HF (HuggingFace) image generator [GS-117].
Implement Flux.1 image generator [GS-117].
Implement Anthropic Claude 3.5 Sonnet [GS-33].
Implement Groq chat model [GS-92].
Implement Amazon Bedrock chat and image generator [GS-131].
Add HUGGINGFACE_PIPELINE_DEVICE to configure the "device" pipeline() parameter [FA-233].
Implement o1-mini/o1-preview models use through AI/ML API aimlapi.com [GS-138].
Implement GS Huggingface lightweight model, identified by model_types "huggingface_remote" or "8s_huggingface". The model_types "huggingface" and "huggingface_pipeline" use the "langchain_hugginface" dependency that required "sentence-transformers", making imposible to deploy the project AWS Lambda Functions [GS-136].
Implement Falcon Mamba with HF [GS-118].
Implement Meta Llama 3.1 with HF [GS-119].

##### Changes
Langchain upgraded to "^0.3.0" [GS-131].
Replace "gpt-3.5-turbo" with "gpt-4o-mini" as default OpenAI model [GS-109].
HUGGINGFACE_ENDPOINT_URL replaced by HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
Config class accepts both OPENAI_MODEL_NAME and OPENAI_MODEL envvars [GS-128].
get_model() "billing" verification logic moved to get_model_middleware() [GS-128].
The user with free plan can only use the "gpt-4o-mini" model with their own API Key, regardless of what is configured in LANGCHAIN_DEFAULT_MODEL [FA-233].

##### Fixes
Fix Anthropic Claude2 API Error since large prompt change, replacing Claude2 with Claude 3.5 Sonnet [GS-33].
Fix the "Warning: deprecated HuggingFaceTextGenInference-use HuggingFaceEnpoint instead" [GS-59].
Fix dependency incompatibility between GS BE Core and GS BE AI fixing the "urllib3" version to "1.26" (and clarifai to "^10.1.0" in consecuence) because GS BE Core's Boto3 use "urllib3" versions less then "<2" [GS-128].

##### Breaks
The "langchain_hugginface" dependency is not longer included in this package. It must be imported in the App's project [GS-136].


## GS BE Scripts

### Package, pull reuest and tag

* Tag: https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.12
* PR: https://github.com/tomkat-cr/genericsuite-be-scripts/pull/3/files
* Package: https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.12

### Changelog

#### 1.0.12 (2024-10-07)
---

##### New
Add ".nvmrc" file to set the repo default node version.
Add DynamoDB database running along with MongoDB in a docker container when running the App in the "dev" stage [GS-102].
Add local DynamoDB tables generation in "generate_dynamodb_cf.py" [GS-102].
Add DynamoDB docker container to "mongodb_stack_for_test.yml" [GS-102].
Add DynamoDB local workbench manager (taydy/dynamodb-manager) to the "mongodb_stack_for_test.yml" [GS-102].
Add DYNAMDB_PREFIX envvar to the "run_aws.sh" script with the value "${APP_NAME_LOWERCASE}_${STAGE}_" [GS-102].
Add GS_LOCAL_ENVIR envvar to detect a local database running in a docker container [GS-102].
Add "run_mongo_docker.sh" runs "generate_dynamodb_cf.sh create_tables dev" to create the DynamoDB tables in the local Docker container [GS-102].
Add "/users/current_user_d" endpoint [GS-2].

##### Changes
Make DynamoDb tables with prefix work with the GS DB Abstraction [GS-102].
Makefile "mongo_docker" runs the MongoDB and DynamoDB docker containers without calling "make run" by default [GS-102].

##### Fixes
Fix error in "run_mongo_docker.sh" starting containers when Docker Desktop is not running [GS-102].


## GenericSuite Basecamp

### Pull request and tag

* Tag: https://github.com/tomkat-cr/genericsuite-basecamp/releases/tag/0.0.12
* PR: https://github.com/tomkat-cr/genericsuite-basecamp/pull/4

### Changelog

#### 0.0.12 (2024-10-07)
---

##### New
Make DynamoDb tables with prefix work with the GS DB Abstraction [GS-102].
Implement HF (HuggingFace) local pipelines [GS-59].
Implement Falcon Mamba with HF [GS-118].
Implement Meta Llama 3.1 with HF [GS-119].
Implement HF (HuggingFace) image generator [GS-117].
Implement Flux.1 image generator [GS-117].
Implement Anthropic Claude 3.5 Sonnet [GS-33].
Implement Groq chat model [GS-92].
Add LOCALSTACK_AUTH_TOKEN documentation [GS-97].
Implement Amazon Bedrock chat and image generator [GS-131].
Add HUGGINGFACE_PIPELINE_DEVICE to configure the "device" pipeline() parameter [FA-233].
Implement o1-mini/o1-preview models use through AI/ML API aimlapi.com [GS-138].
Implement GS Huggingface lightweight model, identified by model_types "huggingface_remote" or "gs_huggingface" [GS-136].

##### Changes
Replace react-bootstrap entirely and use only Tailwind CSS [GS-63].
"index-template.html" is not longer required because the %PUBLIC_URL% issue in public/index.html file running the app with webpack was fixed [GS-116].
Replace GPT-3.5 with gpt-4o-mini as default OpenAI model [GS-109].
HUGGINGFACE_ENDPOINT_URL replaced by HUGGINGFACE_DEFAULT_CHAT_MODEL [GS-59].
<HashRouter> was replaced by <RouterProvider> and createBrowserRouter() [GS-112].

##### Fixes
Fix the %PUBLIC_URL% issue in public/index.html file running the app with webpack [GS-116].

##### Breaks
Bootstrap CSS is not longer used [GS-63].
FontAwesome is not longer used [GS-115].
SVG images removed and included in the "GsIcons" library [GS-115].
Get rid of eval() in the GS FrontEnd [GS-127].
