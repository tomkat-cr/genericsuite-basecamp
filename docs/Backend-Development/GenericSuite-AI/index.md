# The GenericSuite AI for Python
<img 
    align="right"
    width="100"
    height="100"
    src="../../images/gs_ai_logo_circle.svg"
    title="GenericSuite AI logo by Carlos J. Ramirez"
/>

[GenericSuite AI (backend version)](https://github.com/tomkat-cr/genericsuite-be-ai) is a versatile backend solution, designed to provide a comprehensive suite of features, tools and functionalities for AI oriented Python APIs.

It's bassed on [The Generic Suite (backend version)](../GenericSuite-Core/index.md).

The perfect companion for this backend solution is [The GenericSuite AI (frontend version)](../../Frontend-Development/GenericSuite-AI/index.md)

## Pre-requisites

- [Python](https://www.python.org/downloads/) >= 3.9 and < 4.0
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Node version 20+, installed via [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) or [NPM and Node](https://nodejs.org/en/download) install.
* [Docker and Docker Composer](https://www.docker.com/products/docker-desktop)

### AWS account and credentials

* AWS account, see [free tier](https://aws.amazon.com/free).
* AWS Token, see [Access Keys](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* AWS Command-line interface, see [awscli](https://formulae.brew.sh/formula/awscli).
* API Framework and Serverless Deployment, see [Chalice](https://github.com/aws/chalice).

## Installation

First check the [Getting Started](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md#getting-started) section in the [GenericSuite backend version documentation](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md#getting-started).

To use GenericSuite AI in your project, install it with the following command(s):

### From PyPi

Pip
```bash
pip install genericsuite genericsuite-ai
```

Pipenv
```bash
pipenv install genericsuite genericsuite-ai
```

Poetry
```bash
poetry add genericsuite genericsuite-ai
```

**NOTE**: in the following instructions we'll only show `pip install ...`.<BR/>
If you'll use `Pipenv`, change it with `pipenv install ...`.<BR/>
If you'll use `Poetry`, change it with `poetry add ...`.<BR/>

### From Git or Local Directory

Check [this documentation](../../Other/special-installs.md) to install from a Git repository/branch or a Local Directory.

### Test dependencies

To execute the unit and integration test, install `pytest` and `coverage`:

```bash
pip install pytest coverage
```

### Development scripts installation

[The GenericSuite backend development scripts](../GenericSuite-Scripts/index.md) contains utilities to build and deploy APIs made by The GenericSuite.

```bash
npm install -D genericsuite-be-scripts
```

## Features

* AI Agent endpoint to implement NLP Chatbot-like conversations.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX, and many other models handling.
* OpenAI API, Google API, Anthropic API, Hugging Face, Together AI, OpenRuter, AI/ML API, Ollama, Clarifai and other LLM providers.
* Computer vision (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Speech-to-text processing (OpenAI Whisper, Clarifai Audio Models).
* Text-to-speech (OpenAI TTS-1, Clarifai Audio Models).
* Image generator (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Vector indexers (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Web search tool.
* Webpage scrapping and analyzing tool.
* JSON, PDF, Git and YouTube readers.
* Language translation tools.
* Chats stored in the Database.
* User Plan, OpenAI API key and model name attributes in the user profile, to allow free plan users to use Models at their own expense.

## Configuration

Configure your application by setting up the necessary environment variables. Refer to the [.env.example](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/.env.example) and [config.py](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/genericsuite_ai/config/config.py) files for the available options.

Please check the [GenericSuite backend version configuration section](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md#configuration) for more details about general environment variables.

For GenericSuite AI, there are these additional environment variables:

* Chabot configuration
```
# Aplicacion AI assistant name
AI_ASSISTANT_NAME=ExampleBot
```

* Google configuration<BR/>
[https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
```
GOOGLE_API_KEY=google_console_api_key
```
[https://programmablesearchengine.google.com/](https://programmablesearchengine.google.com/)<BR/>
```
GOOGLE_CSE_ID=google_console_cse_key
```

* OpenAI configuration<BR/>
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
```
OPENAI_API_KEY=openai_api_key
OPENAI_MODEL=gpt-4o-mini
OPENAI_TEMPERATURE=0.5
```

* Langchain/LangSmith configuration<BR/>
[https://smith.langchain.com/settings](https://smith.langchain.com/settings)
```
# LANGCHAIN_API_KEY=langchain_api_key
# LANGCHAIN_PROJECT=langchain_project
```

**NOTE**: Langchain/LangSmith configuration is optional. If you don't have a Langchain/LangSmith account, leave the variables commented.

* Hugging Face credentials<BR/>
[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
```
HUGGINGFACE_API_KEY=huggingface_api_key
```

* Hugging Face chat model
```
HUGGINGFACE_DEFAULT_CHAT_MODEL=huggingface_default_chat_model

# Tested models:
# HUGGINGFACE_DEFAULT_CHAT_MODEL=mistralai/Mistral-7B-Instruct-v0.2
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Llama-2-7b-chat-hf

# NOTE: Big models work with huggingface_pipeline only
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Meta-Llama-3.1-405B-Instruct
# HUGGINGFACE_DEFAULT_CHAT_MODEL=tiiuae/falcon-mamba-7b
```

* Hugging Face image generation model
```
HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=huggingface_default_img_gen_model

# Tested models:
# HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=black-forest-labs/FLUX.1-dev
# HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=black-forest-labs/FLUX.1-schnell
```

* AWS Configuration<BR/>
[https://console.aws.amazon.com](https://console.aws.amazon.com)
```
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_DEV=exampleapp-chatbot-attachments-dev
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_QA=exampleapp-chatbot-attachments-qa
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_STAGING=exampleapp-chatbot-attachments-staging
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_PROD=exampleapp-chatbot-attachments-prod
```

Dynamic AI configurations<br/>

Configurable via frontend `Admin > Configuration Parameters` menu option, because they're not included as AWS Lambda environment variables in the deployment scripts.

* General AI Engine configurations

```
LANGCHAIN_DEFAULT_MODEL=chat_openai
# LANGCHAIN_DEFAULT_MODEL=anthropic
# LANGCHAIN_DEFAULT_MODEL=groq
# LANGCHAIN_DEFAULT_MODEL=gemini
# LANGCHAIN_DEFAULT_MODEL=clarifai
# LANGCHAIN_DEFAULT_MODEL=gs_huggingface
#                      or huggingface_remote | Genericsuite's Hugging Face lightweight Inference API
# LANGCHAIN_DEFAULT_MODEL=huggingface
# LANGCHAIN_DEFAULT_MODEL=huggingface_pipeline
```

IMPORTANT: The model_types "huggingface" and "huggingface_pipeline" use the "langchain_hugginface" dependency that required "sentence-transformers", making imposible to deploy the project AWS Lambda Functions. The alternative is the GS Huggingface lightweight identified by model_types "huggingface_remote" or "gs_huggingface".

```
# AI response method:
#
# Wait-until-finished response method (default)
AI_STREAMING=0
# Streaming response method
# AI_STREAMING=1
```

```
AI_VISION_TECHNOLOGY=openai
# AI_VISION_TECHNOLOGY=gemini
# AI_VISION_TECHNOLOGY=clarifai
```
```
AI_IMG_GEN_TECHNOLOGY=openai
# AI_IMG_GEN_TECHNOLOGY=huggingface
# AI_IMG_GEN_TECHNOLOGY=gemini
# AI_IMG_GEN_TECHNOLOGY=clarifai
```
```
AI_AUDIO_TO_TEXT_TECHNOLOGY=openai
# AI_AUDIO_TO_TEXT_TECHNOLOGY=google
# AI_AUDIO_TO_TEXT_TECHNOLOGY=clarifai
```
```
AI_TEXT_TO_AUDIO_TECHNOLOGY=openai
# AI_TEXT_TO_AUDIO_TECHNOLOGY=clarifai
```
```
EMBEDDINGS_ENGINE=openai
# EMBEDDINGS_ENGINE=clarifai
```
```
VECTOR_STORE_ENGINE=FAISS
# VECTOR_STORE_ENGINE=clarifai
# VECTOR_STORE_ENGINE=mongo
# VECTOR_STORE_ENGINE=vectara
```
```
# Add aditional models to the LLM
AI_ADDITIONAL_MODELS=0
# AI_ADDITIONAL_MODELS=1
```

* Langchain credentials and other parameters

```
# Langsmith
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_TRACING_V2=true
```
```
# Agent configuration
LANGCHAIN_AGENT_TYPE=react_chat_agent
# LANGCHAIN_AGENT_TYPE=react_agent
# LANGCHAIN_AGENT_TYPE=structured_chat_agent
# LANGCHAIN_AGENT_TYPE=LLMSingleActionAgent
```
```
LANGCHAIN_MAX_ITERATIONS=8
LANGCHAIN_EARLY_STOPPING_METHOD=force
# LANGCHAIN_EARLY_STOPPING_METHOD=generate
LANGCHAIN_HANDLE_PARSING_ERR=1
```
```
# Translate final Chatbot response to the user in case user's language is not english
LANGCHAIN_TRANSLATE_USING=google_translate
# LANGCHAIN_TRANSLATE_USING=initial_prompt
# LANGCHAIN_TRANSLATE_USING=same_model
# LANGCHAIN_TRANSLATE_USING=
```
```
LANGCHAIN_USE_LANGSMITH_HUB=0
# LANGCHAIN_USE_LANGSMITH_HUB=1
```

* Google other parameters

```
GOOGLE_MODEL=gemini-pro
```
```
GOOGLE_VISION_MODEL=gemini-pro-vision
```
```
# GOOGLE_IMG_GEN_MODEL=gemini-pro-vision
GOOGLE_IMG_GEN_MODEL=imagegeneration@005
```

* OpenAI other parameters
```
# OPENAI_MAX_TOKENS=""
# OPENAI_TOP_P="1"
```
```
# Addicional NLP model
OPENAI_MODEL_PREMIUM=gpt-4-turbo-preview
OPENAI_MODEL_INSTRUCT=gpt-3.5-turbo-instruct
```
```
# Computer Vision model
OPENAI_VISION_MODEL=gpt-4-vision-preview
```
```
# Image generation model
OPENAI_IMAGE_GEN_MODEL=dall-e-3
```
```
# Speech-to-text model
OPENAI_VOICE_MODEL=whisper-1
# Text-to-speech model
OPENAI_TEXT_TO_AUDIO_MODEL=tts-1
OPENAI_TEXT_TO_AUDIO_VOICE=onyx
# OPENAI_TEXT_TO_AUDIO_VOICE=alloy
# OPENAI_TEXT_TO_AUDIO_VOICE=echo
# OPENAI_TEXT_TO_AUDIO_VOICE=fable
# OPENAI_TEXT_TO_AUDIO_VOICE=nova
# OPENAI_TEXT_TO_AUDIO_VOICE=shimmer
```
```
# Embeddings model
OPENAI_EMBEDDINGS_MODEL=text-embedding-ada-002
# OPENAI_EMBEDDINGS_MODEL=text-embedding-3-small
# Embeddings premium model
OPENAI_EMBEDDINGS_MODEL_PREMIUM=text-embedding-3-large'
```

* Anthropic credentials and other parameters<BR/>
[https://console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

```
ANTHROPIC_API_KEY=
ANTHROPIC_MODEL=claude-3-5-sonnet-20240620
```

* Groq credentials and other parameters<BR/>
[https://console.groq.com/keys](https://console.groq.com/keys)<BR/>
[https://console.groq.com/docs/models](https://console.groq.com/docs/models)

```
GROQ_API_KEY=groq_api_key
#
# https://console.groq.com/docs/models
GROQ_MODEL=mixtral-8x7b-32768
```

* AWS Amazon Bedrock credentials and other parameters<BR/>
[https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock)

```
AWS_BEDROCK_MODEL_ID=amazon.titan-text-premier-v1:0
# AWS_BEDROCK_MODEL_ID=amazon.titan-text-express-v1
# AWS_BEDROCK_MODEL_ID=ai21.jamba-instruct-v1:0
# AWS_BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
# AWS_BEDROCK_MODEL_ID=anthropic.claude-3-opus-20240229-v1:0
# AWS_BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
# AWS_BEDROCK_MODEL_ID=anthropic.claude-3-5-sonnet-20240229-v1:0
#
AWS_BEDROCK_IMAGE_GEN_MODEL_ID=stability.stable-diffusion-xl-v1
#
AWS_BEDROCK_CREDENTIALS_PROFILE=
# AWS_BEDROCK_CREDENTIALS_PROFILE=bedrock-admin
#
AWS_BEDROCK_GUARDRAIL_ID=
AWS_BEDROCK_GUARDRAIL_VERSION=
AWS_BEDROCK_GUARDRAIL_TRACE=1
#
AWS_BEDROCK_EMBEDDINGS_MODEL_ID=amazon.titan-embed-text-v1
AWS_BEDROCK_EMBEDDINGS_PROFILE=
# AWS_BEDROCK_EMBEDDINGS_PROFILE=bedrock-admin
```

* AI/ML API platform (one API, 200+ AI Models)<BR/>
[https://aimlapi.com/app/keys](https://aimlapi.com/app/keys)

```
AIMLAPI_API_KEY=aimlapi_api_key

# AIMLAPI_MODEL_NAME=o1-mini
# AIMLAPI_MODEL_NAME=o1-preview

# AIMLAPI_TEMPERATURE=1
# AIMLAPI_MAX_TOKENS=""
# AIMLAPI_TOP_P="1"
```

* Together.ai<BR/>
  [https://api.together.xyz/settings/api-keys](https://api.together.xyz/settings/api-keys)

```
TOGETHER_API_KEY=together_api_key
# TOGETHER_MODEL_NAME="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
```

* xAI (Grok)<BR/>
  [https://console.x.ai](https://console.x.ai)

```
XAI_API_KEY=xai_api_key
# XAI_MODEL_NAME=grok-2
```

* Nvidia NIMs<BR/>
  [https://www.nvidia.com/en-us/account/](https://www.nvidia.com/en-us/account/)

```
NVIDIA_API_KEY=nvidia_api_key
#
# NVIDIA_MODEL_NAME=nvidia/llama-3.1-nemotron-70b-instruct
#
# NVIDIA_TEMPERATURE=0.5
# NVIDIA_MAX_TOKENS=
# NVIDIA_TOP_P=1
```

* Rhymes.ai<BR/>
  [https://rhymes.ai](https://rhymes.ai)

```
RHYMES_CHAT_API_KEY=rhymes_chat_api_key
RHYMES_VIDEO_API_KEY=rhymes_video_api_key
#
# https://rhymes.ai/blog-details/aria-first-open-multimodal-native-moe-model
# RHYMES_CHAT_MODEL_NAME=aria
# RHYMES_CHAT_TEMPERATURE=0.5
# RHYMES_CHAT_MAX_TOKENS=
# RHYMES_CHAT_TOP_P=1
#
# https://rhymes.ai/blog-details/allegro-advanced-video-generation-model
# RHYMES_VIDEO_MODEL_NAME=allegro
# RHYMES_VIDEO_NUM_STEP=50
# RHYMES_VIDEO_CFG_SCALE=7.5
```

* IBM watsonx<BR/>
  [https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-credentials.html?context=wx&audience=wdp](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-credentials.html?context=wx&audience=wdp)<BR/>
  [https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey#iamtoken_from_apikey](https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey#iamtoken_from_apikey)

```
# IBM_WATSONX_MODEL_NAME="meta-llama/llama-3-1-70b-instruct"
# IBM_WATSONX_MODEL_NAME="ibm/granite-13b-chat-v2"
# IBM_WATSONX_MODEL_NAME="google/flan-t5-xxl"
#
IBM_WATSONX_PROJECT_ID=ibm_watsonx_project_id
IBM_WATSONX_API_KEY=ibm_watsonx_api_key
```

* HuggingFace other parameters<BR/>
[https://huggingface.co](https://huggingface.co)

```
HUGGINGFACE_MAX_NEW_TOKENS=512
HUGGINGFACE_TOP_K=50
HUGGINGFACE_TEMPERATURE=1
HUGGINGFACE_REPETITION_PENALTY=03
#
# For "huggingface_pipeline" model_type:
# device (`int` or `str` or `torch.device`):
#   Defines the device (*e.g.*, `"cpu"`, `"cuda:1"`, `"mps"`, or a GPU
#   ordinal rank like `1`) on which this pipeline will be allocated.
# HUGGINGFACE_PIPELINE_DEVICE=0
# HUGGINGFACE_PIPELINE_DEVICE=cuda
```

```
# IMPORTANT: about "sentence-transformers" lib. Be careful, because
# when it's included, the package size increase by 5 Gb. and if the
# app runs in a AWS Lambda Function, it overpass the package size
# deployment limit.

HUGGINGFACE_EMBEDDINGS_MODEL="BAAI/bge-base-en-v1.5"
# HUGGINGFACE_EMBEDDINGS_MODEL="sentence-transformers/all-mpnet-base-v2"

HUGGINGFACE_EMBEDDINGS_MODEL_KWARGS='{"device":"cpu"}'
HUGGINGFACE_EMBEDDINGS_ENCODE_KWARGS='{"normalize_embeddings": true}'
```

* Clarifai credentials and other parameters<BR/>
[https://clarifai.com](https://clarifai.com) > UserId > ProjectId > Settings

```
# PAT (Personal API Token): https://clarifai.com/settings/security
CLARIFAI_PAT=
CLARIFAI_USER_ID=
CLARIFAI_APP_ID=
```

```
AI_CLARIFAI_DEFAULT_CHAT_MODEL=GPT-4
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=claude-v2
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=mixtral-8x7B-Instruct-v0_1
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=llama2-70b-chat
```

```
AI_CLARIFAI_DEFAULT_TEXT_EMBEDDING_MODEL==text-embedding-ada
# AI_CLARIFAI_DEFAULT_TEXT_EMBEDDING_MODEL==BAAI-bge-base-en-v15
```

```
AI_CLARIFAI_DEFAULT_TEXT_TO_AUDIO_MODEL=speech-synthesis
```

```
AI_CLARIFAI_DEFAULT_AUDIO_TO_TEXT_MODEL=whisper
# AI_CLARIFAI_DEFAULT_AUDIO_TO_TEXT_MODEL=whisper-large-v2

AI_CLARIFAI_AUDIO_TO_TEXT_SDK_TYPE=python_sdk
# AI_CLARIFAI_AUDIO_TO_TEXT_SDK_TYPE=clarifai_grpc
```

```
AI_CLARIFAI_DEFAULT_IMG_GEN_MODEL=stable-diffusion-xl
# AI_CLARIFAI_DEFAULT_IMG_GEN_MODEL=dall-e-3
```

```
AI_CLARIFAI_DEFAULT_VISION_MODEL=openai-gpt-4-vision
# AI_CLARIFAI_DEFAULT_VISION_MODEL=food-item-recognition
```

* ElevenLabs<BR/>
[https://elevenlabs.io/app/subscription](https://elevenlabs.io/app/subscription)

```
ELEVENLABS_API_KEY=
```
```
# Sarah
ELEVENLABS_VOICE_ID_FEMALE=EXAVITQu4vr4xnSDxMaL
# Drew
ELEVENLABS_VOICE_ID_MALE=29vD33N1CtxCmqQRPOHJ
```
```
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_STABILITY=0.5
ELEVENLABS_SIMILARITY_BOOST=0.5
ELEVENLABS_STYLE=0
ELEVENLABS_USE_SPEAKER_BOOST=1
```

* Cohere credentials and other parameters<BR/>
[https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)

```
COHERE_API_KEY=
```
```
COHERE_EMBEDDINGS_MODEL=embed-english-light-v3.0
```

* Ollama parameters

```
OLLAMA_MODEL=llama:7b
```
```
OLLAMA_EMBEDDINGS_MODEL=llama:7b
```

* MongoDB embeddings<BR/>
[https://www.mongodb.com](https://www.mongodb.com)

```
MONGODB_VS_COLLECTION=
MONGODB_VS_INDEX_NAME=
```

* Pinecone credentials and other parameters<BR/>
[https://app.pinecone.io/keys](https://app.pinecone.io/keys)

```
# PINECONE_API_KEY=
# PINECONE_ENV=
```

* Vectara credentials and other parameters<BR/>
[https://console.vectara.com/console/apiAccess/personalApiKey](https://console.vectara.com/console/apiAccess/personalApiKey)

```
VECTARA_CUSTOMER_ID=
VECTARA_CORPUS_ID=
VECTARA_API_KEY=
```

* Weaviate credentials and other parameters<BR/>
[https://console.weaviate.cloud/dashboard](https://console.weaviate.cloud/dashboard)

```
WEAVIATE_URL=
WEAVIATE_API_KEY=
```

* Websearch Provider

```env
# WebSearch tool: Provider
# * Default: First DDG, if error, Google
# WEBSEARCH_DEFAULT_PROVIDER=''
# * DuckDuckGo only
# WEBSEARCH_DEFAULT_PROVIDER='ddg'
# * Google only
# WEBSEARCH_DEFAULT_PROVIDER='google'
```

* Websearch DuckDuckGo (ddg) method

```env
# WebSearch tool: DuckDuckGo settings
# * Default: DDGS (Dux Distributed Global Search)
WEBSEARCH_DUCKDUCKGO_METHOD='ddg'
# * Langchain DuckDuckGo wrapper
# WEBSEARCH_DUCKDUCKGO_METHOD='ddg_lc'
```

## Code examples and JSON configuration files

The main menu, API endpoints and CRUD editor configurations are defined in the JSON configuration files.

You can find examples about configurations and how to code an App in the [GenericSuite App Creation and Configuration guide](../../Configuration-Guide/index.md).

## Usage

Check the [The GenericSuite backend development scripts](https://github.com/tomkat-cr/genericsuite-be-scripts?tab=readme-ov-file#the-genericsuite-scripts-backend-version) for more details.

## License

This project is licensed under the ISC License - see the [LICENSE](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/LICENSE) file for details.

## Credits

This project is developed and maintained by Carlos J. Ramirez. For more information or to contribute to the project, visit [GenericSuite AI on GitHub](https://github.com/tomkat-cr/genericsuite-be-ai).

Happy Coding!
