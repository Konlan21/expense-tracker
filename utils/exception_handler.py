import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    # Log full traceback to file
    logger.exception(f"Unhandled exception in {context.get('view')}")

    # DRF's default exception handler
    response = exception_handler(exc, context)

    if response is not None:
        return response

    # Generic 500 response
    return Response(
        {"detail": "Internal server error"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
