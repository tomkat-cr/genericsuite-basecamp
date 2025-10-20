"""
Flask AI Endpoints
"""
from typing import Any

from genericsuite.util.framework_abs_layer import Response
from genericsuite.util.jwt import AuthorizedRequest
from genericsuite.util.utilities import (
    return_resultset_jsonified_or_exception,
)
# from genericsuite.util.app_logger import log_debug

from genericsuite.flasklib.util.blueprint_one import BlueprintOne
from genericsuite.flasklib.util.jwt import token_required
from genericsuite.flasklib.util.parse_multipart import download_file_flask

from genericsuite_ai.flasklib.endpoints.ai_chatbot_endpoint import (
    send_file_flask
)
from genericsuite_ai.lib.ai_chatbot_endpoint import (
    ai_chatbot_endpoint as ai_chatbot_endpoint_model,
    vision_image_analyzer_endpoint as vision_image_analyzer_endpoint_model,
    transcribe_audio_endpoint as transcribe_audio_endpoint_model,
)

from lib.models.ai_chatbot.ai_gpt_fn_index import (
    assign_app_specific_gpt_functions as assign_app_gpt_functions
)

DEBUG = False

bp = BlueprintOne('ai', __name__, url_prefix='/ai')


@bp.route('/chatbot', methods=['POST'])
@token_required
def ai_chatbot_endpoint(
    request: AuthorizedRequest,
    other_params: dict = None,
) -> Any:
    """
    This function is the endpoint for the AI chatbot.
    It takes in a request and other parameters,
    logs the request, retrieves the user data, and runs the
    conversation with the AI chatbot.
    It then returns the AI chatbot's response.

    :param request: The request from the user.
    :return: The response from the AI chatbot.
    """
    return ai_chatbot_endpoint_model(
        request=request,
        blueprint=bp,
        other_params=other_params,
        additional_callable=assign_app_gpt_functions,
        sendfile_callable=send_file_flask,
    )


@bp.route('/image_to_text', methods=['POST'])
@token_required
def vision_image_analyzer_endpoint(
    request: AuthorizedRequest,
    other_params: dict = None,
) -> Response:
    """
    This endpoint receives an image file, saves it to a temporary directory
    with a uuid4 .jpg | .png filename, calls @vision_image_analyzer with
    the file path, and returns the result.

    :param file: The image file uploaded by the user.
    :return: The text with the image analysis.
    """
    uploaded_file = download_file_flask()
    if uploaded_file['error']:
        return return_resultset_jsonified_or_exception(uploaded_file)
    return vision_image_analyzer_endpoint_model(
        request=request,
        blueprint=bp,
        other_params=other_params,
        additional_callable=assign_app_gpt_functions,
        uploaded_file_path=uploaded_file['file_path'],
    )


@bp.route('/voice_to_text', methods=['POST'])
@token_required
async def transcribe_audio_endpoint(
    request: AuthorizedRequest,
    other_params: dict = None,
) -> Response:
    """
    This endpoint receives an audio file, saves it to a temporary directory
    with a uuid4 .mp3 filename, calls @audio_to_text_transcript with
    the file path, and returns the result.

    :param request: The request containing the audio file.
    :return: The transcription result.
    """
    uploaded_file = download_file_flask()
    if uploaded_file['error']:
        return return_resultset_jsonified_or_exception(uploaded_file)
    return transcribe_audio_endpoint_model(
        request=request,
        blueprint=bp,
        other_params=other_params,
        additional_callable=assign_app_gpt_functions,
        uploaded_file_path=uploaded_file['file_path'],
    )
