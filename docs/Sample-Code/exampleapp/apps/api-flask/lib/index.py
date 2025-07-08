"""
Flask ExampleApp main
"""
from genericsuite.flasklib.util.create_app import create_app
# from genericsuite.util.app_logger import log_debug

from lib.config.config import Config
from lib.routers import ai_assistant as ai_chatbot_endpoint
from lib.routers import food_moments
from lib.routers import fda_food_endpoint

settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
                 settings=settings)

# Register application specific endpoints
app.register_blueprint(food_moments.bp)
app.register_blueprint(fda_food_endpoint.bp)

# Register AI endpoints
app.register_blueprint(ai_chatbot_endpoint.bp)
