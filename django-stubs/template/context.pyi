# Stubs for django.template.context (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.db.models.options import Options
from django.http.request import HttpRequest
from django.template.base import Origin, Template
from django.template.defaulttags import CycleNode
from django.template.library import InclusionNode
from django.template.loader_tags import BlockContext
from itertools import cycle
from typing import Any, Callable, Dict, Iterator, List, Optional, Type, Union
_builtin_context_processors: Any

class ContextPopException(Exception): ...

class ContextDict(dict):
    context: Any = ...
    def __init__(self, context: BaseContext, *args: Any, **kwargs: Any) -> None: ...
    def __enter__(self) -> ContextDict: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...

class BaseContext:
    def __init__(self, dict_: Any = ...) -> None: ...
    dicts: Any = ...
    def _reset_dicts(self, value: Any = ...) -> None: ...
    def __copy__(self) -> BaseContext: ...
    def __repr__(self) -> str: ...
    def __iter__(self) -> None: ...
    def push(self, *args: Any, **kwargs: Any) -> ContextDict: ...
    def pop(self) -> ContextDict: ...
    def __setitem__(self, key: Union[str, CycleNode, InclusionNode], value: Any) -> None: ...
    def set_upward(self, key: str, value: Union[str, int]) -> None: ...
    def __getitem__(self, key: Union[str, int]) -> object: ...
    def __delitem__(self, key: Any) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def get(self, key: str, otherwise: Optional[int] = ...) -> Optional[Union[Options, int, str]]: ...
    def setdefault(self, key: str, default: Union[List[Origin], int] = ...) -> Union[List[Origin], int]: ...
    def new(self, values: Any = ...) -> Context: ...
    def flatten(self) -> Dict[str, Optional[Union[int, str, Dict[str, Union[Type[object], str]]]]]: ...
    def __eq__(self, other: Context) -> bool: ...

class Context(BaseContext):
    autoescape: Any = ...
    use_l10n: Any = ...
    use_tz: Any = ...
    template_name: str = ...
    render_context: Any = ...
    template: Any = ...
    def __init__(self, dict_: Any = ..., autoescape: bool = ..., use_l10n: Optional[bool] = ..., use_tz: None = ...) -> None: ...
    def bind_template(self, template: Template) -> Iterator[None]: ...
    def __copy__(self) -> Context: ...
    def update(self, other_dict: Dict[str, Any]) -> ContextDict: ...

class RenderContext(BaseContext):
    template: Any = ...
    def __iter__(self) -> None: ...
    def __contains__(self, key: Union[str, CycleNode]) -> bool: ...
    def get(self, key: Union[str, InclusionNode], otherwise: None = ...) -> Optional[Union[Template, BlockContext]]: ...
    def __getitem__(self, key: Union[str, CycleNode]) -> Union[BlockContext, List[Origin], cycle]: ...
    def push_state(self, template: Template, isolated_context: bool = ...) -> Iterator[None]: ...

class RequestContext(Context):
    request: Any = ...
    _processors: Any = ...
    _processors_index: Any = ...
    def __init__(self, request: HttpRequest, dict_: None = ..., processors: Optional[List[Callable]] = ..., use_l10n: None = ..., use_tz: None = ..., autoescape: bool = ...) -> None: ...
    template: Any = ...
    def bind_template(self, template: Template) -> Iterator[None]: ...
    def new(self, values: Any = ...) -> RequestContext: ...

def make_context(context: Any, request: Optional[WSGIRequest] = ..., **kwargs: Any) -> Context: ...
