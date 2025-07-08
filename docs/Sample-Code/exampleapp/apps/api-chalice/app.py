"""
Chalice ExampleApp main file.
"""
from genericsuite.chalicelib.util.create_app import create_app

# Temporal - BEGIN
from genericsuite_ai.chalicelib.endpoints import ai_conversations_conversion
# Temporal - END

from lib.config.config import Config

from chalicelib.endpoints import food_moments
from chalicelib.endpoints import fda_food_endpoint
from chalicelib.endpoints import ai_exampleapp_bot as ai_chatbot_endpoint

settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
                 settings=settings)

# Register application specific endpoints
app.register_blueprint(food_moments.bp, url_prefix='/food_moments')
app.register_blueprint(
    fda_food_endpoint.bp, url_prefix='/fda_food_query'
)

# Register AI endpoints
app.register_blueprint(ai_chatbot_endpoint.bp, url_prefix='/ai')

# Temporal - BEGIN
app.register_blueprint(ai_conversations_conversion.bp, url_prefix='/ai_temp')
# Temporal - END
