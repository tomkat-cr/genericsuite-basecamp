# fastapitemplate_configs

fastapitemplate frontend/backend configurations and data structures.

## Directory Structure

```
fastapitemplate/config_dbdef/
├── backend/
|   ├── ai_chatbot_conversations.json           # AI Chatbot conversations for the Chatbot UI
|   ├── app_main_menu.json                      # App main menu configuration
|   ├── endpoints.json                          # App backend API endpoints configuration
|   ├── general_config.json                     # App dynamic configuration parameters
|   ├── users_api_keys.json                     # User's API keys
|   ├── users_config.json                       # User's configuration parameters
|   ├── users_profile.json                      # User's profile page
|   ├── users.json                              # Users
├── frontend/
|   ├── ai_chatbot_conversations_complete.json  # AI Chatbot conversations for a CRUD editor
|   ├── ai_chatbot_conversations.json           # AI Chatbot conversations for the Chatbot UI
|   ├── app_constants.json                      # App general constants (billing plans, units, types, codes, gender, emails, urls, etc.)
|   ├── general_config.json                     # App dynamic configuration parameters
|   ├── general_constants.json                  # App general constants (true/false, yes/no, languages, genders, etc.)
|   ├── users_api_keys.json                     # User's API keys
|   ├── users_config.json                       # User's configuration parameters
|   ├── users_profile.json                      # User's profile page
|   ├── users.json                              # Users
├── .gitignore
├── CHANGELOG.md
├── package.json
├── README.md
```

## Backend directory

The `backend` directory contains configurations only visible in the backend API.

## Frontend directory

The `frontend` directory contains configurations used by both the frontend App and the backend API.

## fastapitemplate

[fastapitemplate](../README.md) is a full-stack application that allows you have a template to start your FastAPI application based on GenericSuite.

Click [here](../README.md) to know more about it.