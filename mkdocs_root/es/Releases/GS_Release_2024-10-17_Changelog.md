# 20241017 - Asistente de IA mejorado, Modelos de preámbulo y OpenAI o1

![GS_Release_2025-07-05_Image_1.png](./images/GS_Release_2025-07-05_Image_1.png)

Fecha de lanzamiento: 2024-10-17

## Resumen

El equipo de GenericSuite continúa innovando con su última versión el 17 de octubre de 2024. Esta versión introduce características nuevas y emocionantes que mejorarán la forma en que los desarrolladores trabajan con la IA.

Una de las principales novedades es la implementación de un modelo de preámbulo para ejecutar los modelos OpenAI o1-mini/o1-preview con herramientas y mensajes del sistema. Esto ofrece mayor flexibilidad al trabajar con estos modelos. Además, se han añadido nuevas configuraciones para personalizar el modelo de preámbulo, permitiendo a los usuarios adaptar su comportamiento a sus necesidades específicas.

La actualización también introduce la integración con el servidor Ollama, abriendo nuevas posibilidades para gestionar modelos como Ollama "llava", que no aceptan mensajes de herramientas. Ahora, los modelos pueden configurarse para funcionar de manera óptima en estos escenarios.

Finalmente, se abordó un problema clave en el que los agentes devolvían respuestas vacías en cadenas LCEL. Los agentes devolverán ahora resultados correctamente cuando ya no haya más herramientas que llamar.

¡No te pierdas esta actualización, que eleva la gestión de IA al siguiente nivel!

## Núcleo Frontend de GenericSuite:

### Paquete, pull request y etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite/v/1.0.23](https://www.npmjs.com/package/genericsuite/v/1.0.23)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.23](https://www.github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.23)
* PR: [https://github.com/tomkat-cr/genericsuite-fe/pull/5](https://www.github.com/tomkat-cr/genericsuite-fe/pull/5)

### Registro de cambios

#### 1.0.23 (2024-10-25)
---

##### Nuevo
- Agregar el parámetro "closeHandler" a errorAndReEnter().

##### Correcciones
- Corregir el formato Markdown en la conversación de AI Assistant [GS-145].
- Corregir el botón de copiar en la conexión http no segura [GS-144].

## Frontend IA de GenericSuite:

### Paquete, pull request y etiqueta

* Paquete: [https://www.npmjs.com/package/genericsuite-ai/v/1.0.21](https://www.npmjs.com/package/genericsuite-ai/v/1.0.21)
* Etiqueta: [https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.21](https://www.github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.21) 
* PR: [https://github.com/tomkat-cr/genericsuite-fe-ai/pull/5](https://www.github.com/tomkat-cr/genericsuite-fe-ai/pull/5)

### Registro de cambios

#### 1.0.21 (2024-10-25)
---

##### Cambios
- El núcleo frontend de GenericSuite se actualizó a la versión v1.0.23.

##### Correcciones
- Corregir el formato Markdown en la conversación de AI Assistant [GS-145].
- Corregir el botón de copiar en la conexión http no segura [GS-144].
- Corregir la recarga de la lista de conversaciones cuando ocurre cualquier error.
- Corregir la barra de desplazamiento vertical en el área de entrada del chatbot cuando el contenido es demasiado largo.
- Corregir AI Assistant en dispositivos móviles.

## Backend IA de GenericSuite:

### Paquete, pull request y etiqueta

* Etiqueta: [https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.11](https://www.github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.11)
* PR: [https://github.com/tomkat-cr/genericsuite-be-ai/pull/7](https://www.github.com/tomkat-cr/genericsuite-be-ai/pull/7)
* Paquete: [https://pypi.org/project/genericsuite-ai/0.1.11/](https://pypi.org/project/genericsuite-ai/0.1.11/)

### Registro de cambios

#### 0.1.11 (2024-10-17)
---

##### Nuevo
- Implementar modelo de preámbulo para ejecutar modelos OpenAI o1-mini/o1-preview con Tools y mensajes del Sistema [GS-140].
- Agregar AI_PREAMBLE_MODEL_DEFAULT_TYPE, AI_PREAMBLE_MODEL_DEFAULT_MODEL, AI_PREAMBLE_MODEL_BASE_CONF, AI_PREAMBLE_MODEL_CUSTOM_CONF para personalizar el modelo de preámbulo [GS-140].
- Implementar servidor Ollama [GS-139].
- Agregar AI_MODEL_ALLOW_SYSTEM_MSG, AI_MODEL_ALLOW_TOOLS y AI_MODEL_NEED_PREAMBLE para gestionar modelos como Ollama "llava" que no aceptan Tools [GS-140].

##### Cambios
- Actualizar ChatOllama añadiendo la dependencia "langchain-ollama" [GS-139].

##### Correcciones
- Corregir que Tools hagan que el Agente devuelva respuestas vacías en cadenas LCEL. Ahora el Agente devuelve el resultado cuando ya no quedan más Tools por llamar [GS-143].