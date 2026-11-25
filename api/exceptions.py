import logging

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class DomainError(Exception):
    status_code = status.HTTP_400_BAD_REQUEST
    code = "BAD_REQUEST"

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ConflictError(DomainError):
    status_code = status.HTTP_409_CONFLICT
    code = "CONFLICT"


def handle_exception(exc, context):
    if isinstance(exc, DomainError):
        logger.warning("%s: %s", exc.code, exc.message)
        return Response({"error": exc.message, "code": exc.code}, status=exc.status_code)
    if isinstance(exc, ValidationError):
        return Response(
            {"error": "Invalid request data", "code": "VALIDATION_ERROR", "details": exc.detail},
            status=status.HTTP_400_BAD_REQUEST,
        )
    logger.exception("Unexpected error")
    return Response(
        {"error": "Internal server error", "code": "SERVER_ERROR"},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
