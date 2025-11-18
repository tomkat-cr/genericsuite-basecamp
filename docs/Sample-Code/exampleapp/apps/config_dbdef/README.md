# exampleapp_configs

Exampleapp frontend/backend configurations and data structures.

## Directory Structure

```
exampleapp/apps/config_dbdef/
├── backend/
|   ├── ai_chatbot_conversations.json           # AI Chatbot conversations for the Chatbot UI
|   ├── app_main_menu.json                      # App main menu configuration
|   ├── clarifai_models.json                    # Clarifai AI models
|   ├── daily_meal_ingredients.json             # User's daily meal ingredients
|   ├── daily_meals.json                        # User's daily meal list
|   ├── dish_ingredients.json                   # User's dish ingredients
|   ├── dishes.json                             # User's dishes list
|   ├── endpoints.json                          # App backend API endpoints configuration
|   ├── food_moments.json                       # General food types (or moments) list
|   ├── general_config.json                     # App dynamic configuration parameters
|   ├── general_ingredients.json                # Global ingredients
|   ├── user_ingredients_all.json               # All user's ingredients
|   ├── user_ingredients.json                   # User's ingredients
|   ├── user_api_keys.json                      # User's API keys
|   ├── users_config.json                       # User's configuration parameters
|   ├── users_food_times.json                   # User's typical meal ingestion times
|   ├── users_profile.json                      # User's profile page
|   ├── users_user_history.json                 # User's data history (goals, weight, etc.)
|   ├── users.json                              # Users
├── frontend/
|   ├── ai_chatbot_conversations_complete.json  # AI Chatbot conversations for a CRUD editor
|   ├── ai_chatbot_conversations.json           # AI Chatbot conversations for the Chatbot UI
|   ├── app_constants.json                      # App general constants (billing plans, units, types, codes, gender, emails, urls, etc.)
|   ├── clarifai_models.json                    # Clarifai AI models
|   ├── daily_meal_ingredients.json             # User's daily meal ingredients
|   ├── daily_meals.json                        # User's daily meal list
|   ├── dish_ingredients.json                   # User's dish ingredients
|   ├── dishes.json                             # User's dishes list
|   ├── food_moments.json                       # General food types (or moments) list
|   ├── general_config.json                     # App dynamic configuration parameters
|   ├── general_constants.json                  # App general constants (true/false, yes/no, languages, genders, etc.)
|   ├── general_ingredients.json                # Global ingredients
|   ├── user_ingredients_all.json               # All user's ingredients
|   ├── user_ingredients.json                   # User's ingredients
|   ├── user_api_keys.json                      # User's API keys
|   ├── users_config.json                       # User's configuration parameters
|   ├── users_food_times.json                   # User's typical meal ingestion times
|   ├── users_profile.json                      # User's profile page
|   ├── users_user_history.json                 # User's data history (goals, weight, etc.)
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

## Example App

The [ExampleApp](../../README.md) is a full-stack example application demonstrating how to create an App using GenericSuite. It is a web application architecture with a React-based frontend and backend services implemented in FastAPI, Flask and Chalice.

Click [here](../../README.md) to know more about it.