"""
FastAPI ExampleApp main
"""
# import os
from mangum import Mangum

from genericsuite.fastapilib.util.create_app import create_app
# from genericsuite.util.app_logger import log_debug

from app.config.config import Config

from app.routers import ai_assistant as ai_chatbot_endpoint

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

# Register AI endpoints
app.include_router(ai_chatbot_endpoint.router, prefix='/ai')


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

handler = create_handler(app)
