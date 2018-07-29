# Stubs for django.contrib.messages.middleware (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.deprecation import MiddlewareMixin
from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
class MessageMiddleware(MiddlewareMixin):
    def process_request(self, request: WSGIRequest) -> None: ...
    def process_response(self, request: HttpRequest, response: HttpResponseBase) -> HttpResponseBase: ...
