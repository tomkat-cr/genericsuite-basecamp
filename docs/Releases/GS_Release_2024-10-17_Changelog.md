# 20241017 - AI Assistant enhanced, Preamble Models and OpenAI o1

![GS_Release_2025-07-05_Image_1.png](./images/GS_Release_2025-07-05_Image_1.png)

Release Date: 2024-10-17

## Summary

The GenericSuite team continues to innovate with its latest release on October 17, 2024. This version introduces exciting new features that will improve how developers work with AI.

One of the main highlights is the implementation of a preamble model to run OpenAI o1-mini/o1-preview models with tools and system messages. This provides greater flexibility when working with these models. Additionally, new configurations have been added to customize the preamble model, allowing users to tailor its behavior to their specific needs.

The update also introduces Ollama server integration, opening up new possibilities for managing models like Ollama "llava," which do not accept tools messages. Now, models can be configured to function optimally in these scenarios.

Finally, a key issue has been addressed where agents were returning empty responses in LCEL chains. Agents will now return results correctly when there are no more tools to call.

Don’t miss out on this update, which takes AI management to the next level!

## GenericSuite Frontend Core:

### Package, pull reuest and tag

* Package: https://www.npmjs.com/package/genericsuite/v/1.0.23
* Tag: https://github.com/tomkat-cr/genericsuite-fe/releases/tag/1.0.23
* PR: https://github.com/tomkat-cr/genericsuite-fe/pull/5

### Changelog

#### 1.0.23 (2024-10-25)
---

##### New
Add "closeHandler" parameter to errorAndReEnter().

##### Fixes
Fix markdown formatting in AI Assistant conversation [GS-145].
Fix copy button in non-secure http connection [GS-144].

## GenericSuite Frontend AI:

### Package, pull reuest and tag

* Package: https://www.npmjs.com/package/genericsuite-ai/v/1.0.21
* Tag: https://github.com/tomkat-cr/genericsuite-fe-ai/releases/tag/1.0.21 
* PR: https://github.com/tomkat-cr/genericsuite-fe-ai/pull/5

### Changelog

#### 1.0.21 (2024-10-25)
---

##### Changes
GenericSuite FE core upgraded to v1.0.23.

##### Fixes
Fix Markdown formatting in AI Assistant conversation [GS-145].
Fix copy button in non-secure http connection [GS-144].
Fix conversation list reload when any error occurs.
Fix show vertical scroll bar in the chatbot input area when the content is too long.
Fix AI Assistant in mobile devices.

## GenericSuite Backend AI:

### Package, pull reuest and tag

* Tag: https://github.com/tomkat-cr/genericsuite-be-ai/releases/tag/0.1.11
* PR: https://github.com/tomkat-cr/genericsuite-be-ai/pull/7
* Package: https://pypi.org/project/genericsuite-ai/0.1.11/

### Changelog

#### 0.1.11 (2024-10-17)
---

##### New
Implement preamble model to run OpenAI o1-mini/o1-preview models with Tools and System messages [GS-140].
Add AI_PREAMBLE_MODEL_DEFAULT_TYPE, AI_PREAMBLE_MODEL_DEFAULT_MODEL, AI_PREAMBLE_MODEL_BASE_CONF, AI_PREAMBLE_MODEL_CUSTOM_CONF to customize the preamble model [GS-140].
Implement ollama server [GS-139].
Add AI_MODEL_ALLOW_SYSTEM_MSG, AI_MODEL_ALLOW_TOOLS, and AI_MODEL_NEED_PREAMBLE to manage models like Ollama "llava" that doesn't accept Tools [GS-140].

##### Changes
Update ChatOllama adding the "langchain-ollama" dependency [GS-139].

##### Fixes
Fix Tools make Agent returns empty responses in LCEL chains. Now Agent returns the result when there are no more Tools to call [GS-143].
