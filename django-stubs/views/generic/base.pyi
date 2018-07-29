# Stubs for django.views.generic.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseRedirectBase
from django.template.response import TemplateResponse
from typing import Any, Callable, Dict, List, Union
logger: Any

class ContextMixin:
    extra_context: Any = ...
    def get_context_data(self, **kwargs: Any) -> Dict[str, object]: ...

class View:
    http_method_names: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    head: Any = ...
    request: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def as_view(cls, **initkwargs: Any) -> Callable: ...
    def dispatch(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> Union[View, HttpResponse]: ...
    def http_method_not_allowed(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseNotAllowed: ...
    def options(self, request: Any, *args: Any, **kwargs: Any): ...
    def _allowed_methods(self) -> List[str]: ...

class TemplateResponseMixin:
    template_name: Any = ...
    template_engine: Any = ...
    response_class: Any = ...
    content_type: Any = ...
    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> TemplateResponse: ...
    def get_template_names(self) -> List[str]: ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> TemplateResponse: ...

class RedirectView(View):
    permanent: bool = ...
    url: Any = ...
    pattern_name: Any = ...
    query_string: bool = ...
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str: ...
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirectBase: ...
    def head(self, request: Any, *args: Any, **kwargs: Any): ...
    def post(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirect: ...
    def options(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirect: ...
    def delete(self, request: Any, *args: Any, **kwargs: Any): ...
    def put(self, request: Any, *args: Any, **kwargs: Any): ...
    def patch(self, request: Any, *args: Any, **kwargs: Any): ...
