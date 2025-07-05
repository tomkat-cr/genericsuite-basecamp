"""
FastAPI ExampleApp main
"""
# import os
from mangum import Mangum

from genericsuite.fastapilib.util.create_app import create_app
# from genericsuite.util.app_logger import log_debug

from lib.config.config import Config

from lib.routers import ai_assistant as ai_chatbot_endpoint
from lib.routers import food_moments
from lib.routers import fda_food_endpoint

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
app.include_router(food_moments.router, prefix='/food_moments')
app.include_router(
    fda_food_endpoint.router, prefix='/fda_food_query'
)

# Register AI endpoints
app.include_router(ai_chatbot_endpoint.router, prefix='/ai')


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

handler = create_handler(app)
