from datetime import datetime, timezone
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from core.logger import api_logger


class LogMiddleware:
    def __init__(
        self,
        get_response: Callable[[WSGIRequest], HttpResponse],
    ) -> None:
        self.get_response = get_response

    def __call__(
        self,
        request: WSGIRequest,
    ) -> HttpResponse:
        api_logger.info(f'New request: {datetime.now(timezone.utc)} - {request.method} {request.path}')

        return self.get_response(request)
