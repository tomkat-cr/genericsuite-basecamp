# Historia

![gs_logo_circle.png](../assets/images/gs_logo_circle.png)

A mediados de la década de 1980 experimenté el editor CRUD genérico y otros elementos generados con programación genérica que funcionaban para una empresa que desarrollaba software siguiendo estos conceptos, con las configuraciones generadas por un sistema llamado **System Maker** y almacenadas en la base de datos, utilizando lenguajes de programación y bases de datos de última generación para esa época ([Clipper](https://en.wikipedia.org/wiki/Clipper_(programming_language)) y [dBase III](https://en.wikipedia.org/wiki/DBase)). Esos conceptos, en mi opinión, estaban muy por delante de su tiempo.

Entre 1999 y 2000 hice mi propia versión del editor CRUD genérico en [Microsoft ASP](https://en.wikipedia.org/wiki/Active_Server_Pages) (Active Server Pages) para un [CMS](https://en.wikipedia.org/wiki/Content_management_system) (Content Management System), algo parecido a lo que hace WordPress.

Recientemente me di cuenta de que esto se llama **DRY**. DRY es un acrónimo de "Don't Repeat Yourself" y es un principio de desarrollo de software que busca reducir la repetición de código. El código DRY utiliza abstracciones que tienen menos probabilidades de cambiar, la parametrización y la normalización de datos para evitar la redundancia. El código DRY busca reducir patrones repetitivos y código y lógica duplicados, a favor de un código modular y referenciable.

En 2020 (durante la pandemia), concebí la idea de una nueva aplicación llamada [FynApp](https://www.carlosjramirez.com/en/fynapp-an-app-to-achieve-calorie-deficit/). Empecé a desarrollar un editor CRUD genérico con un frontend [React.js](https://react.dev/) basado en [Componentes Funcionales y Hooks] ([repositorio original aquí](https://github.com/tomkat-cr/fynapp_frontend)) y un backend en [Python](https://www.python.org/) ([repositorio original aquí](https://github.com/tomkat-cr/fynapp_backend)). En ese momento, todas las configuraciones estaban codificadas en la estructura de la aplicación.

Al comienzo de 2023 comencé a convertir el editor genérico a [React.js](https://react.dev/) basado en [Componentes funcionales y hooks] y las configuraciones en archivos JSON.

Durante [PyCon Colombia](https://2023.pycon.co/) en junio de 2023, se me ocurrió otra idea: llevar la programación genérica al backend. Empecé a codificar los manejadores CRUD y la generación automática del Menú y de Endpoints a partir de las mismas configuraciones utilizadas por el editor CRUD genérico del frontend, usando archivos JSON almacenados en un repositorio común para frontend y backend.

Las noticias sobre [ChatGPT](https://chat.openai.com/) a finales de 2022 y el auge de la IA (Inteligencia Artificial) me volvieron muy curioso y con ganas de incluir algo de eso en [FynApp](https://www.carlosjramirez.com/en/fynapp-an-app-to-achieve-calorie-deficit/).

En julio de 2023 participé en el [Hackathon de lablab.ai Google Vertex AI](https://lablab.ai/event/google-vertex-ai-hackathon) y eso me dio las ideas para crear **FynBot**: el asistente de inteligencia artificial para [FynApp](https://app-demo.fynapp.com), basado en [APIs de OpenAI](https://platform.openai.com/docs/api-reference) y más tarde [GPT Functions](https://platform.openai.com/docs/guides/function-calling).

![gs_ai_logo_circle.png](../assets/images/gs_ai_logo_circle.png)

Entre agosto y noviembre de 2023 exploré e incluí generación de imágenes y audio con IA en la App.

En diciembre de 2023 decidí implementar la programación genérica utilizando [Langchain para Python](https://python.langchain.com/), para usar cualquier [LLM](https://en.wikipedia.org/wiki/Large_language_model) / [NLP](https://en.wikipedia.org/wiki/Natural_language_processing) / [Modelos de embeddings](https://en.wikipedia.org/wiki/Word_embedding) y evitar depender de un único proveedor de IA.

El 18 de febrero de 2024, [The Generic Suite](https://genericsuite.carlosjramirez.com) nació extrayendo toda la programación genérica de [FynApp](https://www.carlosjramirez.com/en/fynapp-an-app-to-achieve-calorie-deficit/). La primera versión se publicó a principios de marzo de 2024 y los primeros paquetes se publicaron en NPMJS y PyPI a principios de abril de 2024.

Esta es mi primera contribución a la comunidad de código abierto.