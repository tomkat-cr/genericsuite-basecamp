"""
Flask ExampleApp main
"""
from genericsuite.flasklib.util.create_app import create_app
# from genericsuite.util.app_logger import log_debug

from flaskr.config.config import Config
from flaskr.routers import ai_assistant as ai_chatbot_endpoint


settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
                 settings=settings)

# Register AI endpoints
app.register_blueprint(ai_chatbot_endpoint.bp)
