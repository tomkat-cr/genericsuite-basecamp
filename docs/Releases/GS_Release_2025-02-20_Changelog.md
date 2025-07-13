# 20250220 - The 1st Anniversary Release

![GS_Release_2025-07-05_Image_3B.png](./images/GS_Release_2025-07-05_Image_3B.png)

Release Date: 2025-02-20

## Summary

We are thrilled to announce the 1st Anniversary Release of GenericSuite, a significant milestone that brings a host of powerful new features and enhancements for developers and businesses. This release underscores our commitment to providing a comprehensive and cutting-edge suite of tools for modern software development.

Key highlights of this release include:

- Enhanced AI Capabilities: We've integrated advanced AI functionalities, including image and video generation within the GenericSuite App Maker (GSAM). Our AI backend now supports a wider range of providers, such as Together AI, xAI (Grok), IBM WatsonX, and Nvidia, offering greater flexibility and power for your AI-driven applications.

- Introduction of the Agentic Software Development Team (ASDT): A groundbreaking addition, the ASDT is a team of AI agents designed to automate and streamline the software development lifecycle. From ideation and planning to coding and testing, the ASDT is set to revolutionize how you build software.

- Improved Development and Deployment: We've made significant strides in our GitOps and backend infrastructure. The introduction of an Ollama server, n8n server, and API key implementation in the GS BE Core enhances security and scalability. The Generic Endpoint Builder for Flask simplifies API creation, while fixes to our frontend and backend components ensure a more stable and robust development experience.

This anniversary release is more than just an update; it's a leap forward in our mission to empower developers with the tools they need to build the future of software. We invite you to explore the new features and see how GenericSuite can accelerate your development process.

## GSAM (GenericSuite App Maker)

### Pull Request and Tag 0.5.0

* https://github.com/tomkat-cr/genericsuite-app-maker/pull/4
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/5
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/6
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/7
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/8
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/9
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/10
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/11
* https://github.com/tomkat-cr/genericsuite-app-maker/pull/12
* https://github.com/tomkat-cr/genericsuite-app-maker/releases/tag/0.5.0

### Changelog

#### 0.5.0 (2025-02-17)
--

##### New
Add image and video generation capabilities to the Live Agent Studio-compatible GSAM Agent [GS-166].
Add "new_prompt" button and action to empty the question input field [GS-55].
Add the generic model use for the gsam_agent_lib [GS-55].

##### Changes
Ollama enabled [GS-55].
Control de generic model use for the gsam_agent_lib with the SIMPLE_PAI_AGENT constant. When True, only OpenAI or Openrouter providers are available; False (by default) offers all the providers in the "app_config.json" file [GS-55].

##### Fixes
Fix the runtime error in the Streamlit UI in production [GS-55].
Ollama runtime errors fixed and all configurations goes to the "options" sub-item [GS-55].

## ASDT (GenericSuite Agentic Software Development Team)

### Pull Request and Tag 0.1.0

* https://github.com/tomkat-cr/genericsuite-asdt-be/pull/1
* https://github.com/tomkat-cr/genericsuite-asdt-be/pull/2
* https://github.com/tomkat-cr/genericsuite-asdt-be/pull/3
* https://github.com/tomkat-cr/genericsuite-asdt-be/pull/4
* https://github.com/tomkat-cr/genericsuite-asdt-be/pull/5
* https://github.com/tomkat-cr/genericsuite-asdt-be/releases/tag/0.1.0

### Changelog

#### 0.1.0 (2025-02-17)
---

##### New
Add LLM selection and configuration using environment variables, and including OpenAI, Google, Ollama, Anthropic, Hugging Face, Groq, NVIDIA, X AI, Together AI, AI/ML API and OpenRouter [GS-128].
Add the ideation task to generate ideas for the "AIstronauts-Space Agents on a mission hackathon" from lablab.ai [GS-55].
Add different environment variables for coding, reasoning, planning and management llms and models, so normal agents, manager agent and planning agent can use them [GS-128].
Add the planning agent, so the code generation actions are fired and iterated [GS-128].
Add "openlit" monitoring tool [GS-128].
Add "agentops" monitoring tool [GS-128].
Add generate output files on each task [GS-128].
Add automatic generation of the crew, agents and tasks directly from the yaml files with no wrappers (decorated class and methods) [GS-128].
Add "allow_code_execution" to developer and automated testing agents [GS-128].
Add reading-from-file feature to `project` and `topic` inputs (content enclosed by square brackets means it's a file path) [GS-128].
Add "examples/instructions.md" to build the `project` input as a PRD file (Product Requirements Document) [GS-128].
Add Camel-AI agent society to the agent libraries.

##### Changes
Change: remove the GenericSuite dependency.

##### Fixes
Fix the agents and task prompts to effectively work as a team [GS-128].

## GenericSuite Gitops

### Pull Request and Tag 0.2.0

* https://github.com/tomkat-cr/genericsuite-gitops/pull/1
* https://github.com/tomkat-cr/genericsuite-gitops/releases/tag/0.2.0

### Changelog

#### 0.2.0 (2024-02-18)
---

##### New
Abstract and add to the Genericsuite project [GS-141].
Implement ollama server [GS-139].
Implement n8n server [GS-165]


#### 0.1.2 (2022-03-16)
---

##### Changes
FA-58: "restart: unless-stopped" to the VPS docker compose configuration, to let the containers stay active on server reboots.
FA-31: Separate databases for prod, staging and development.
Increase the VPS DKR images version.

##### New
Add Python scripts to get IP and scan the network.
Create this repo `version.tx`t, `README.md` and `CHANGELOG.md` files.


#### 0.1.11 (2022-03-10)
---

##### New
Preview version with initial deployment of BE (Backend) and FE (Frontend) of Fynapp webapp.
Release notes:
FA-3: Create a pipeline to build and deploy the backend to a docker container in a Linux VPS.
FA-13: Create a develop branch and start using it with good SDLC practices.
FA-18: Create a pipeline to build and deploy BE & FE on Heroku.
FA-21: Recover local I5 y/o Celeron server and install Centos 7.
FA-22: Install and configure Kubernetes on the local server and perform a spike the evaluate using this technology.
FA-23: Build a docker image in a Gitlab pipeline by install a Gitlab runner.


## GenericSuite Backend Scripts

### Package, Pull Request and Tag 1.0.13

* https://www.npmjs.com/package/genericsuite-be-scripts/v/1.0.13
* https://github.com/tomkat-cr/genericsuite-be-scripts/pull/4
* https://github.com/tomkat-cr/genericsuite-be-scripts/pull/5
* https://github.com/tomkat-cr/genericsuite-be-scripts/releases/tag/1.0.13

### Changelog

#### 1.0.13 (2025-02-18)
---

##### Changes
The "--loglevel debug" option were added to the gunicorn server for Generic Endpoint Builder for Flask [GS-15].

##### Fixes
Fix flask run with gunicorn when local machine is running a VPN, getting the local IP address, which is the first one reported by the "ifconfig" command [GS-15].


## GenericSuite Backend Core

### Package, Pull Request and Tag 0.1.10

* https://pypi.org/project/genericsuite/0.1.10/
* https://github.com/tomkat-cr/genericsuite-be/pull/8
* https://github.com/tomkat-cr/genericsuite-be/pull/9
* https://github.com/tomkat-cr/genericsuite-be/releases/tag/0.1.10

### Changelog

#### 0.1.10 (2025-02-19)

##### New
Implement API keys to GS BE Core [GS-159].
Implement the "CAUJF" endpoint to build all user's parameters local JSON files [GS-159].
Generic Endpoint Builder for Flask [GS-15].

##### Changes
FastAPI get_current_user() now gets the headers from the request object (required by the API keys implementation) [GS-159].
GenericDbHelperSuper class assigns None default value to Request and Blueprint, and {} to query_params and request_body properties, so it can be used by save_all_users_params_files() or other functions that does not have those objects in a given time [GS-159].
GenericDbHelperSuper class avoid call specific_func_name() when blueprint is None [GS-159].
Overall code clean up and linting changes.

##### Fixes
Fix poetry 2.x "The option --no-update does not exist" error message [FA-84].
Missing "context" and "event_dict" properties, "to_dict" and "to_original_event" events, were added to the FastAPI Request class.
Fix "'License :: OSI Approved :: ISC License' is not a valid classifier" error running "python3 -m twine upload dist/*" [FA-84].


## GenericSuite Backend AI

### Package, pull request and Tag 0.1.12

* https://pypi.org/project/genericsuite-ai/0.1.12/
* https://github.com/tomkat-cr/genericsuite-be-ai/pull/8
* https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.12

### Changelog

#### 0.1.12 (2025-02-19)
---

##### New
Implement Together AI provider and models [GS-158].
Implement xAI Grok model [GS-157].
Implement IBM watsonx provider [GS-155].
Implement generic Langchain model abstract interface [GS-155].
Implement Nvidia API / NIM / Nemotron [GS-93].
Implement Rhymes.ai Aria chat model [GS-152].
Implement Rhymes.ai Allegro video generation model (only configuration) [GS-153].
Add AI_STREAMING envvar to configure the Streaming response method [GS-32].
Add NVIDIA_API_KEY, NVIDIA_MODEL_NAME, NVIDIA_TEMPERATURE, NVIDIA_MAX_TOKENS, NVIDIA_TOP_P, and NVIDIA_BASE_URL envvars [GS-93].
Add RHYMES_CHAT_API_KEY, RHYMES_CHAT_MODEL_NAME, RHYMES_CHAT_TEMPERATURE, RHYMES_CHAT_MAX_TOKENS, RHYMES_CHAT_TOP_P, RHYMES_CHAT_BASE_URL, RHYMES_VIDEO_API_KEY, RHYMES_VIDEO_MODEL_NAME, RHYMES_VIDEO_BASE_URL, RHYMES_VIDEO_NUM_STEP, and RHYMES_VIDEO_CFG_SCALE envvars [GS-152].
Add AIMLAPI_TOP_P to configure top_p parameter in AI/ML API [GS-138].
Add OPENAI_TOP_P to configure top_p parameter in OpenAI chat model.
Add CustomLLM abstract class for LangChain to implement new LLM providers not implemented in LangChain yet [GS-155]. 

##### Changes
Change "black-forest-labs/FLUX.1-schnell" image generation model by default.
Change OPENAI_MAX_TOKENS and AIMLAPI_MAX_TOKENS to have '' by default to get the maximum tokens possible [GS-157].
Change "grok-beta" changed to "grok-2" as default model for xAI [GS-157].
Change "openai" instead of "openai_chat" to get the default OpenAI provider in the LANGCHAIN_DEFAULT_MODEL parameter.
"get_openai_api()" function was added to standardize LLM client creation for providers compatible with the OpenAI completions API [GS-157].

##### Fixes
Fix the "ValueError: invalid literal for int() with base 10: ''" error in get_vision_response() when OPENAI_MAX_TOKENS is empty [GS-152].
Fix poetry 2.x "The option --no-update does not exist" error message [FA-84].
Fix "'License :: OSI Approved :: ISC License' is not a valid classifier" error running "python3 -m twine upload dist/*" [FA-84].


## GenericSuite Frontend Core

### Package, pull request and Tag 1.0.24

* https://www.npmjs.com/package/genericsuite/v/1.0.24
* https://github.com/tomkat-cr/genericsuite-fe/pull/6
* https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.24

### Changelog

#### 1.0.24 (2025-02-19)
---

##### New
Implement API keys to GS BE Core [GS-159].
Add new features and fix things discovered during the IBM Watson X implementation [GS-155]
Add the parameter "description_fields" In selectOptions() to have a compound attribute/column name(s) for the drop-down menu descriptions. If not specified, it'll use ["name"] (as it was before) [GS-155].

##### Fixes
Fix the undefined passcode error in user update calling the backend after creating a user leaving the password empty (UsersPasswordValidations) [GS-155].
Fix a bug calling the specific functions assigning the "fieldValues" object, because genericFuncArrayDefaultValue() was assigning it an infinite recursive "resultset" attribute, preventing the default values assignment in "dbPreRead" call (creation).


## GenericSuite Frontend AI

### Package, pull request and Tag 1.0.22

* https://www.npmjs.com/package/genericsuite-ai/v/1.0.22
* https://github.com/tomkat-cr/genericsuite-fe-ai/pull/6
* https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.22

### Changelog

#### 1.0.22 (2025-02-19)
---

##### Changes
GenericSuite FE core upgraded to v1.0.24.
