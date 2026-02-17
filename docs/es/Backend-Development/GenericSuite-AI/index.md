# GenericSuite AI para Python

![gs_ai_logo_circle.png](../../../assets/images/gs_ai_logo_circle.png)

[GenericSuite AI (backend version)](https://github.com/tomkat-cr/genericsuite-be-ai) es una solución de backend versátil, diseñada para proporcionar un conjunto completo de características, herramientas y funcionalidades para APIs de Python orientadas a IA.

Está basado en [The Generic Suite (backend version)](../GenericSuite-Core/index.md).

El compañero perfecto para esta solución de backend es [The GenericSuite AI (frontend version)](../../Frontend-Development/GenericSuite-AI/index.md)

## Requisitos

- Versión de Python >= 3.10 y < 4.0 (recomendado instalar con [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation); las versiones se especifican en los archivos `.python-version`)
- [Git](https://www.atlassian.com/git/tutorials/install-git)
- Make: [Mac](https://formulae.brew.sh/formula/make) | [Windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
- Versión de Node 20+, instalada vía [NVM (Node Package Manager)](https://nodejs.org/en/download/package-manager) o [NPM y Node](https://nodejs.org/en/download)
- [Docker y Docker Composer](https://www.docker.com/products/docker-desktop)
- [uv](https://docs.astral.sh/uv/getting-started/installation/), [pipenv](https://pipenv.pypa.io/en/latest/), o [poetry](https://python-poetry.org/docs/) (para la gestión de dependencias de Python)

### Cuenta de AWS y credenciales

* Cuenta de AWS, ver [free tier](https://aws.amazon.com/free).
* Token de AWS, ver [Access Keys](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials?section=IAM_credentials).
* Interfaz de línea de comandos de AWS, ver [awscli](https://formulae.brew.sh/formula/awscli).
* Framework de API y Despliegue sin servidor, ver [Chalice](https://github.com/aws/chalice).

## Instalación

Primero verifique la sección de [Getting Started](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md#getting-started) en la [documentación de la versión backend de GenericSuite](https://github.com/tomkat-cr/genericsuite-be/blob/main/README.md#getting-started).

Para usar GenericSuite AI en su proyecto, instálelo con el/los siguientes comandos:

### Desde PyPi

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

Uv
```bash
uv add genericsuite genericsuite-ai
```

**NOTA**: en las siguientes instrucciones solo mostraremos `pip install ...`.<br>
Si usa `pipenv`, reemplácelo por `pipenv install ...`.<br>
Si usa `poetry`, reemplácelo por `poetry add ...`.<br>
Si usa `uv`, reemplácelo por `uv add ...`.<br>

Consulte [esta documentación](../../Other/python-package-managers.md) para usar las diferentes herramientas de gestión de paquetes y dependencias de Python.

### Desde Git o Directorio Local

Consulte [esta documentación](../../Other/installation.md) para instalar desde un repositorio/ rama de Git o desde un Directorio Local.

### Dependencias de prueba

Para ejecutar las pruebas unitarias y de integración, instale `pytest` y `coverage`:

```bash
pip install pytest coverage
```

### Instalación de scripts de desarrollo

[Los scripts de desarrollo del backend de GenericSuite](../GenericSuite-Scripts/index.md) contienen utilidades para construir y desplegar APIs creadas por The GenericSuite.

```bash
npm install -D genericsuite-be-scripts
```

## Funcionalidades

* Endpoint de AI Agent para implementar conversaciones tipo chatbot NLP.
* OpenAI GPT, Google Gemini, Anthropic Claude, Meta Llama, Hugging Face, xAI, IBM WatsonX y muchos otros modelos.
* OpenAI API, Google API, Anthropic API, Hugging Face, Together AI, OpenRuter, API de IA/ML, Ollama, Clarifai y otros proveedores de LLM.
* Visión por computadora (OpenAI GPT4 Vision, Google Gemini Vision, Clarifai Vision).
* Procesamiento de voz a texto (OpenAI Whisper, Clarifai Audio Models).
* Texto a voz (OpenAI TTS-1, Clarifai Audio Models).
* Generador de imágenes (OpenAI DALL-E 3, Google Gemini Image, Clarifai Image Models).
* Indexadores vectoriales (FAISS, Chroma, Clarifai, Vectara, Weaviate, MongoDBAtlasVectorSearch).
* Embeddings (OpenAI, Hugging Face, Bedrock, Cohere, Ollama, Clarifai).
* Herramienta de búsqueda en la web.
* Raspeo y análisis de páginas web.
* Lectores de JSON, PDF, Git y YouTube.
* Herramientas de traducción de idiomas.
* Chats almacenados en la base de datos.
* Plan de usuario, clave API de OpenAI y nombre de modelo en el perfil del usuario, para permitir que usuarios con plan gratuito utilicen modelos a su propio costo.

## Configuración

Configure su aplicación configurando las variables de entorno necesarias.

Consulte los archivos [.env.example](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/.env.example) y [config.py](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/genericsuite_ai/config/config.py) para las opciones disponibles.

Primero copie la plantilla `.env.example` a su archivo `.env`:

```bash
curl https://raw.githubusercontent.com/tomkat-cr/genericsuite-be-ai/main/.env.example > .env
```

Luego, edite el archivo `.env` para establecer los valores deseados:

```bash
vi .env
```

Por favor, consulte la sección de configuración de la versión backend de GenericSuite para más detalles sobre variables de entorno generales.

Para GenericSuite AI, existen estas variables de entorno adicionales:

* Configuración de chatbot
```env
# Nombre del asistente de IA
AI_ASSISTANT_NAME=ExampleBot
```

* Configuración de Google<br>
[https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
```env
GOOGLE_API_KEY=google_console_api_key
```
[https://programmablesearchengine.google.com/](https://programmablesearchengine.google.com/)<br>
```env
GOOGLE_CSE_ID=google_console_cse_key
```

* Configuración de OpenAI<br>
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
```env
OPENAI_API_KEY=openai_api_key
OPENAI_MODEL=gpt-4o-mini  # otras opciones: gpt-5-nano, gpt-5-mini, gpt-5, gpt-4o, gpt-3.5-turbo
OPENAI_TEMPERATURE=0.5
```

* Configuración de Langchain/LangSmith<br>
[https://smith.langchain.com/settings](https://smith.langchain.com/settings)
```env
# LANGCHAIN_API_KEY=langchain_api_key
# LANGCHAIN_PROJECT=langchain_project
```

**NOTA**: La configuración de Langchain/LangSmith es opcional. Si no tiene una cuenta de Langchain/LangSmith, deje las variables comentadas.

* Credenciales de Hugging Face<br>
[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
```env
HUGGINGFACE_API_KEY=huggingface_api_key
```

* Modelo de chat de Hugging Face
```env
HUGGINGFACE_DEFAULT_CHAT_MODEL=huggingface_default_chat_model

# Modelos probados:
# HUGGINGFACE_DEFAULT_CHAT_MODEL=moonshotai/Kimi-K2-Instruct-0905
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Llama-2-7b-chat-hf

# NOTA: Modelos grandes funcionan con huggingface_pipeline solamente
# HUGGINGFACE_DEFAULT_CHAT_MODEL=meta-llama/Meta-Llama-3.1-405B-Instruct
```

* Modelo de generación de imágenes de Hugging Face
```env
HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=huggingface_default_img_gen_model

# Modelos probados:
# HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=black-forest-labs/FLUX.1-dev
# HUGGINGFACE_DEFAULT_IMG_GEN_MODEL=black-forest-labs/FLUX.1-schnell
```

* AWS Configuración<br>
[https://console.aws.amazon.com](https://console.aws.amazon.com)
```env
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_DEV=exampleapp-chatbot-attachments-dev
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_QA=exampleapp-chatbot-attachments-qa
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_STAGING=exampleapp-chatbot-attachments-staging
AWS_S3_CHATBOT_ATTACHMENTS_BUCKET_PROD=exampleapp-chatbot-attachments-prod
```

Configuraciones dinámicas de IA<br>

Configurable via frontend `Admin > Configuration Parameters` menu option, because they're not included as AWS Lambda environment variables in the deployment scripts.

* Configuraciones generales del motor de IA

```env
LANGCHAIN_DEFAULT_MODEL=chat_openai
# LANGCHAIN_DEFAULT_MODEL=anthropic
# LANGCHAIN_DEFAULT_MODEL=groq
# LANGCHAIN_DEFAULT_MODEL=gemini
# LANGCHAIN_DEFAULT_MODEL=clarifai
# LANGCHAIN_DEFAULT_MODEL=gs_huggingface
#                      o huggingface_remote | Genericsuite's Hugging Face lightweight Inference API
# LANGCHAIN_DEFAULT_MODEL=huggingface
# LANGCHAIN_DEFAULT_MODEL=huggingface_pipeline
```

**IMPORTANTE**: El tipo de modelo "huggingface_pipeline" utiliza la dependencia "langchain_hugginface" que puede requerir "sentence-transformers", haciendo imposible desplegar las funciones Lambda de AWS. La alternativa es el GS Huggingface ligero identificado por los tipos de modelo "huggingface_remote" o "gs_huggingface".

```env
# Método de respuesta de IA:
#
# Método de respuesta que espera a finalizar (predeterminado)
AI_STREAMING=0
# Método de respuesta en streaming
# AI_STREAMING=1
```

```env
AI_VISION_TECHNOLOGY=openai
# AI_VISION_TECHNOLOGY=gemini
# AI_VISION_TECHNOLOGY=clarifai
```
```env
AI_IMG_GEN_TECHNOLOGY=openai
# AI_IMG_GEN_TECHNOLOGY=huggingface
# AI_IMG_GEN_TECHNOLOGY=gemini
# AI_IMG_GEN_TECHNOLOGY=clarifai
```
```env
AI_AUDIO_TO_TEXT_TECHNOLOGY=openai
# AI_AUDIO_TO_TEXT_TECHNOLOGY=google
# AI_AUDIO_TO_TEXT_TECHNOLOGY=clarifai
```
```env
AI_TEXT_TO_AUDIO_TECHNOLOGY=openai
# AI_TEXT_TO_AUDIO_TECHNOLOGY=clarifai
```
```env
EMBEDDINGS_ENGINE=openai
# EMBEDDINGS_ENGINE=clarifai
```
```env
VECTOR_STORE_ENGINE=FAISS
# VECTOR_STORE_ENGINE=clarifai
# VECTOR_STORE_ENGINE=mongo
# VECTOR_STORE_ENGINE=vectara
```
```env
# Añadir modelos adicionales al LLM
AI_ADDITIONAL_MODELS=0
# AI_ADDITIONAL_MODELS=1
```

* Modelos de preámbulo: se usan principalmente con modelos de Thinking AI como OpenAI o1 y o3, o DeepSeek
```env
# Permitir mensaje del sistema (0/1). Por defecto 1. Ponga a 0 para la mayoría de los modelos Thinking AI
# AI_MODEL_ALLOW_SYSTEM_MSG=0

# Permitir herramientas (0/1). Por defecto 1. Ponga a 0 para la mayoría de los modelos Thinking AI
# AI_MODEL_ALLOW_TOOLS=0

# ¿Se necesita preámbulo (0/1). Por defecto 0. Ponga a 1 para la mayoría de modelos Thinking AI
# AI_MODEL_NEED_PREAMBLE=1

# Tipo de modelo de preámbulo (chat_openai, huggingface, etc.). Por defecto "chat_openai". Debe configurarse para la mayoría de modelos Thinking AI cuando AI_MODEL_NEED_PREAMBLE=1
# AI_PREAMBLE_MODEL_DEFAULT_TYPE=chat_openai

# Nombre del modelo de preámbulo. Por defecto "gpt-4o-mini". Debe configurarse para la mayoría de modelos Thinking AI cuando #AI_MODEL_NEED_PREAMBLE=1
# AI_PREAMBLE_MODEL_DEFAULT_MODEL=gpt-4o-mini

# Configuración base del modelo de preámbulo, para establecer valores por defecto para algunos modelos de Thinking AI si es necesario.
# AI_PREAMBLE_MODEL_BASE_CONF='{"o1-mini": {"model_type": "chat_openai", "model_name": "gpt-4o-mini"}, "o1-preview": {"model_type": "chat_openai", "model_name": "gpt-4o-mini"}}'

# Configuración de modelo de preámbulo personalizada, para establecer valores por defecto para algunos modelos de Thinking AI si es necesario.
# AI_PREAMBLE_MODEL_CUSTOM_CONF=''
```

Por ejemplo, para usar "DeepSeek-V3.2" alojado en Hugging Face, puede establecer las siguientes variables de entorno:
```env
LANGCHAIN_DEFAULT_MODEL=huggingface
HUGGINGFACE_API_KEY=hf_xxxxxx
HUGGINGFACE_DEFAULT_CHAT_MODEL=deepseek-ai/DeepSeek-V3.2
AI_MODEL_ALLOW_SYSTEM_MSG=0
AI_MODEL_ALLOW_TOOLS=0
AI_MODEL_NEED_PREAMBLE=1
AI_PREAMBLE_MODEL_DEFAULT_TYPE=huggingface
AI_PREAMBLE_MODEL_DEFAULT_MODEL=moonshotai/Kimi-K2-Instruct-0905
# AI_PREAMBLE_MODEL_BASE_CONF='{"o1-mini": {"model_type": "chat_openai", "model_name": "gpt-4o-mini"}, "o1-preview": {"model_type": "chat_openai", "model_name": "gpt-4o-mini"}}'
# AI_PREAMBLE_MODEL_CUSTOM_CONF=
```

* Credenciales de Langchain y otros parámetros

```env
# Langsmith
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_TRACING_V2=true
```
```env
# Configuración de Agente
LANGCHAIN_AGENT_TYPE=lcel
# LANGCHAIN_AGENT_TYPE=react_chat_agent
# LANGCHAIN_AGENT_TYPE=react_agent
# LANGCHAIN_AGENT_TYPE=structured_chat_agent
# LANGCHAIN_AGENT_TYPE=LLMSingleActionAgent
```
```env
LANGCHAIN_MAX_ITERATIONS=8
LANGCHAIN_EARLY_STOPPING_METHOD=force
# LANGCHAIN_EARLY_STOPPING_METHOD=generate
LANGCHAIN_HANDLE_PARSING_ERR=1
```
```env
# Traducir la respuesta final del chatbot al usuario en caso de que el idioma del usuario no sea inglés
LANGCHAIN_TRANSLATE_USING=google_translate
# LANGCHAIN_TRANSLATE_USING=initial_prompt
# LANGCHAIN_TRANSLATE_USING=same_model
# LANGCHAIN_TRANSLATE_USING=
```
```env
LANGCHAIN_USE_LANGSMITH_HUB=0
# LANGCHAIN_USE_LANGSMITH_HUB=1
```

* Otros parámetros de Google

```env
GOOGLE_MODEL=gemini-pro
```
```env
GOOGLE_VISION_MODEL=gemini-pro-vision
```
```env
# GOOGLE_IMG_GEN_MODEL=gemini-pro-vision
GOOGLE_IMG_GEN_MODEL=imagegeneration@005
```

* Otros parámetros de OpenAI
```env
# OPENAI_MAX_TOKENS=""
# OPENAI_TOP_P="1"
```
```env
# Modelo NLP adicional
OPENAI_MODEL_PREMIUM=gpt-4o   # otras opciones: gpt-5, o1-mini, o1-preview, gpt-4
OPENAI_MODEL_INSTRUCT=gpt-3.5-turbo-instruct
```
```env
# Modelo de visión por computadora
OPENAI_VISION_MODEL=gpt-4-vision-preview
```
```env
# Modelo de generación de imágenes
OPENAI_IMAGE_GEN_MODEL=dall-e-3
```
```env
# Modelo de voz a texto
OPENAI_VOICE_MODEL=whisper-1
# Modelo de texto a voz
OPENAI_TEXT_TO_AUDIO_MODEL=tts-1
OPENAI_TEXT_TO_AUDIO_VOICE=onyx
# OPENAI_TEXT_TO_AUDIO_VOICE=alloy
# OPENAI_TEXT_TO_AUDIO_VOICE=echo
# OPENAI_TEXT_TO_AUDIO_VOICE=fable
# OPENAI_TEXT_TO_AUDIO_VOICE=nova
# OPENAI_TEXT_TO_AUDIO_VOICE=shimmer
```
```env
# Modelo de embeddings
OPENAI_EMBEDDINGS_MODEL=text-embedding-ada-002
# OPENAI_EMBEDDINGS_MODEL=text-embedding-3-small
# Modelo de embeddings premium
OPENAI_EMBEDDINGS_MODEL_PREMIUM=text-embedding-3-large'
```

* Credenciales y otros parámetros de Anthropique<br>
[https://console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

```env
ANTHROPIC_API_KEY=
ANTHROPIC_MODEL=claude-3-5-sonnet-20240620
```

* Credenciales y otros parámetros de Groq<br>
[https://console.groq.com/keys](https://console.groq.com/keys)<br>
[https://console.groq.com/docs/models](https://console.groq.com/docs/models)

```env
GROQ_API_KEY=groq_api_key
#
# https://console.groq.com/docs/models
GROQ_MODEL=mixtral-8x7b-32768
```

* Credenciales y otros parámetros de AWS Amazon Bedrock<br>
[https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock)

```env
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

* Plataforma de API de IA/ML (una API, 200+ modelos de IA)<br>
[https://aimlapi.com/app/keys](https://aimlapi.com/app/keys)

```env
AIMLAPI_API_KEY=aimlapi_api_key

# AIMLAPI_MODEL_NAME=o1-mini
# AIMLAPI_MODEL_NAME=o1-preview

# AIMLAPI_TEMPERATURE=1
# AIMLAPI_MAX_TOKENS=""
# AIMLAPI_TOP_P="1"
```
```env
* Together.ai<br>
  [https://api.together.xyz/settings/api-keys](https://api.together.xyz/settings/api-keys)

```env
TOGETHER_API_KEY=together_api_key
# TOGETHER_MODEL_NAME="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
```

* xAI (Grok)<br>
  [https://console.x.ai](https://console.x.ai)

```env
XAI_API_KEY=xai_api_key
# XAI_MODEL_NAME=grok-2
```

* Nvidia NIMs<br>
  [https://www.nvidia.com/en-us/account/](https://www.nvidia.com/en-us/account/)

```env
NVIDIA_API_KEY=nvidia_api_key
#
# NVIDIA_MODEL_NAME=nvidia/llama-3.1-nemotron-70b-instruct
#
# NVIDIA_TEMPERATURE=0.5
# NVIDIA_MAX_TOKENS=
# NVIDIA_TOP_P=1
```

* Rhymes.ai<br>
  [https://rhymes.ai](https://rhymes.ai)

```env
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

* IBM watsonx<br>
  [https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-credentials.html?context=wx&audience=wdp](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-credentials.html?context=wx&audience=wdp)<br>
  [https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey#iamtoken_from_apikey](https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey#iamtoken_from_apikey)

```env
# IBM_WATSONX_MODEL_NAME="meta-llama/llama-3-1-70b-instruct"
# IBM_WATSONX_MODEL_NAME="ibm/granite-13b-chat-v2"
# IBM_WATSONX_MODEL_NAME="google/flan-t5-xxl"
#
IBM_WATSONX_PROJECT_ID=ibm_watsonx_project_id
IBM_WATSONX_API_KEY=ibm_watsonx_api_key
```

* Otros parámetros de HuggingFace<br>
[https://huggingface.co](https://huggingface.co)

```env
HUGGINGFACE_MAX_NEW_TOKENS=512
HUGGINGFACE_TOP_K=50
HUGGINGFACE_TEMPERATURE=1
HUGGINGFACE_REPETITION_PENALTY=03
#
# Para el tipo de modelo "huggingface_pipeline":
# dispositivo (int, str o torch.device):
#   Define el dispositivo (p. ej., `"cpu"`, `"cuda:1"`, `"mps"`, o un rango de GPU
#   como `1`) al que se asignará este pipeline.
# HUGGINGFACE_PIPELINE_DEVICE=0
# HUGGINGFACE_PIPELINE_DEVICE=cuda
```

```env
# IMPORTANTE: sobre la librería "sentence-transformers". Ten en cuenta que
# cuando está incluida, el tamaño del paquete aumenta en ~5 Gb. y si la
# aplicación se ejecuta en una función AWS Lambda, supera el límite de tamaño
# de despliegue.

HUGGINGFACE_EMBEDDINGS_MODEL="BAAI/bge-base-en-v1.5"
# HUGGINGFACE_EMBEDDINGS_MODEL="sentence-transformers/all-mpnet-base-v2"

HUGGINGFACE_EMBEDDINGS_MODEL_KWARGS='{"device":"cpu"}'
HUGGINGFACE_EMBEDDINGS_ENCODE_KWARGS='{"normalize_embeddings": true}'
```

```env
# Proveedor de inferencia de Hugging Face:
# Opciones disponibles: `auto`, `cerebras`, `groq`, `hyperbolic`, `nebius`, `together`, `hf-inference`, etc.
# Ver proveedores disponibles en: https://hf.co/settings/inference-providers
# "auto" es el proveedor predeterminado y utilizará el mejor proveedor disponible.
# HUGGINGFACE_PROVIDER=auto
# https://huggingface.co/models?inference_provider=groq
# HUGGINGFACE_PROVIDER=groq
# https://huggingface.co/models?inference_provider=cerebras
# HUGGINGFACE_PROVIDER=cerebras
# https://huggingface.co/models?inference_provider=hyperbolic
# HUGGINGFACE_PROVIDER=hyperbolic
# https://huggingface.co/models?inference_provider=nebius
# HUGGINGFACE_PROVIDER=nebius
# https://huggingface.co/models?inference_provider=together
# HUGGINGFACE_PROVIDER=together
# https://huggingface.co/models?inference_provider=hf-inference
# HUGGINGFACE_PROVIDER=hf-inference
```

* Credenciales y otros parámetros de Clarifai<br>
[https://clarifai.com](https://clarifai.com) > UserId > ProjectId > Settings

```env
# PAT (Personal API Token): https://clarifai.com/settings/security
CLARIFAI_PAT=
CLARIFAI_USER_ID=
CLARIFAI_APP_ID=
```

```env
AI_CLARIFAI_DEFAULT_CHAT_MODEL=GPT-4
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=claude-v2
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=mixtral-8x7B-Instruct-v0_1
# AI_CLARIFAI_DEFAULT_CHAT_MODEL=llama2-70b-chat
```

```env
AI_CLARIFAI_DEFAULT_TEXT_EMBEDDING_MODEL==text-embedding-ada
# AI_CLARIFAI_DEFAULT_TEXT_EMBEDDING_MODEL==BAAI-bge-base-en-v15
```

```env
AI_CLARIFAI_DEFAULT_TEXT_TO_AUDIO_MODEL=speech-synthesis
```

```env
AI_CLARIFAI_DEFAULT_AUDIO_TO_TEXT_MODEL=whisper
# AI_CLARIFAI_DEFAULT_AUDIO_TO_TEXT_MODEL=whisper-large-v2

AI_CLARIFAI_AUDIO_TO_TEXT_SDK_TYPE=python_sdk
# AI_CLARIFAI_AUDIO_TO_TEXT_SDK_TYPE=clarifai_grpc
```

```env
AI_CLARIFAI_DEFAULT_IMG_GEN_MODEL=stable-diffusion-xl
# AI_CLARIFAI_DEFAULT_IMG_GEN_MODEL=dall-e-3
```

```env
AI_CLARIFAI_DEFAULT_VISION_MODEL=openai-gpt-4-vision
# AI_CLARIFAI_DEFAULT_VISION_MODEL=food-item-recognition
```

* ElevenLabs<br>
[https://elevenlabs.io/app/subscription](https://elevenlabs.io/app/subscription)

```env
ELEVENLABS_API_KEY=
```
```env
# Sarah
ELEVENLABS_VOICE_ID_FEMALE=EXAVITQu4vr4xnSDxMaL
# Drew
ELEVENLABS_VOICE_ID_MALE=29vD33N1CtxCmqQRPOHJ
```
```env
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_STABILITY=0.5
ELEVENLABS_SIMILARITY_BOOST=0.5
ELEVENLABS_STYLE=0
ELEVENLABS_USE_SPEAKER_BOOST=1
```

* Credenciales y otros parámetros de Cohere<br>
[https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)

```env
COHERE_API_KEY=
```
```env
COHERE_EMBEDDINGS_MODEL=embed-english-light-v3.0
```

* Parámetros de Ollama

```env
OLLAMA_MODEL=llama:7b
```
```env
OLLAMA_EMBEDDINGS_MODEL=llama:7b
```

* Embeddings de MongoDB<br>
[https://www.mongodb.com](https://www.mongodb.com)

```env
MONGODB_VS_COLLECTION=
MONGODB_VS_INDEX_NAME=
```

* Credenciales y otros parámetros de Pinecone<br>
[https://app.pinecone.io/keys](https://app.pinecone.io/keys)

```env
# PINECONE_API_KEY=
# PINECONE_ENV=
```

* Credenciales y otros parámetros de Vectara<br>
[https://console.vectara.com/console/apiAccess/personalApiKey](https://console.vectara.com/console/apiAccess/personalApiKey)

```env
VECTARA_CUSTOMER_ID=
VECTARA_CORPUS_ID=
VECTARA_API_KEY=
```

* Credenciales y otros parámetros de Weaviate<br>
[https://console.weaviate.cloud/dashboard](https://console.weaviate.cloud/dashboard)

```env
WEAVIATE_URL=
WEAVIATE_API_KEY=
```

* Proveedor de WebSearch

```env
# Proveedor del WebSearch: Proveedor
# * Predeterminado: primero DDG, si hay error, Google
# WEBSEARCH_DEFAULT_PROVIDER=''
# * Solo DuckDuckGo
# WEBSEARCH_DEFAULT_PROVIDER='ddg'
# * Solo Google
# WEBSEARCH_DEFAULT_PROVIDER='google'
```

* Método DuckDuckGo (ddg) de WebSearch

```env
# WebSearch tool: DuckDuckGo settings
# * Default: DDGS (Dux Distributed Global Search)
WEBSEARCH_DUCKDUCKGO_METHOD='ddg'
# * Envoltorio de DuckDuckGo de Langchain
# WEBSEARCH_DUCKDUCKGO_METHOD='ddg_lc'
```

* Banderas de Depuración de IA

```env
# AI_AUDIO_PROCESSING_DEBUG=1
# AI_CHATBOT_COMMONS_DEBUG=1
# AI_CHATBOT_DEBUG=1
# AI_CONVERSATIONS_DEBUG=1
# AI_EMBEDDINGS_DEBUG=1
# AI_GPT_FN_CONVERSATIONS_DEBUG=1
# AI_GPT_FUNCTIONS_DEBUG=1
# AI_IMAGE_GENERATOR_DEBUG=1
# AI_MODELS_DEBUG=1
# AI_TOOLS_DEBUG=1
# AI_SUB_BOTS_DEBUG=1
# AI_UTILITIES_DEBUG=1
# AI_VISION_DEBUG=1
# AI_AMAZON_BEDROCK_DEBUG=1
# AI_CLARIFAI_DEBUG=1
# AI_HUGGINGFACE_DEBUG=1
# AI_GIT_READER_DEBUG=1
# AI_IBM_DEBUG=1
# AI_JSON_READER_DEBUG=1
# AI_TRANSLATOR_DEBUG=1
# AI_VECTOR_INDEX_DEBUG=1
# AI_WEB_SCRAPPING_DEBUG=1
# AI_WEBSEARCH_DEBUG=1
# AI_YOUTUBE_READER_DEBUG=1
# GCP_DEBUG=1
```

## Ejemplos de código y archivos de configuración JSON

El menú principal, los endpoints de la API y las configuraciones del editor CRUD se definen en los archivos de configuración JSON.

Puede encontrar ejemplos de configuraciones y cómo codificar una Aplicación en la guía [Guía de creación y configuración de Aplicaciones de GenericSuite](../../Configuration-Guide/index.md).

## Uso

Consulte [los scripts de desarrollo del backend de GenericSuite](https://github.com/tomkat-cr/genericsuite-be-scripts?tab=readme-ov-file#the-genericsuite-scripts-backend-version) para más detalles.

## Licencia

Este proyecto está licenciado bajo la ISC License; vea el archivo [LICENSE](https://github.com/tomkat-cr/genericsuite-be-ai/blob/main/LICENSE) para más detalles.

## Créditos

Este proyecto es desarrollado y mantenido por Carlos J. Ramirez. Para más información o para contribuir al proyecto, visite [GenericSuite AI en GitHub](https://github.com/tomkat-cr/genericsuite-be-ai).

¡Feliz codificación!