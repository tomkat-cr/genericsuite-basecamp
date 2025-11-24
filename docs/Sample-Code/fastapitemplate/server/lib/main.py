"""
FastAPI main
"""
# import os
from mangum import Mangum

from genericsuite.fastapilib.util.create_app import create_app
# from genericsuite.util.app_logger import log_debug

from lib.config.config import Config

from lib.routers import ai_assistant as ai_chatbot_endpoint
from lib.routers import parameters as parameters_endpoint

# ############################

# from genericsuite.fastapilib.util.create_app import create_handler


def create_handler(app_object):
    """
    Returns the FastAPI App as a valid AWS Lambda Function handler
    """
    return Mangum(app_object, lifespan="off")

# ############################


settings = Config()
app = create_app(app_name=f'{settings.APP_NAME.lower()}-backend',
                 settings=settings)

# Register application specific endpoints
app.include_router(parameters_endpoint.router, prefix='/parameters')

# Register AI endpoints
app.include_router(ai_chatbot_endpoint.router, prefix='/ai')

handler = create_handler(app)
