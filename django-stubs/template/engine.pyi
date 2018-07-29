# Stubs for django.template.engine (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Context, Template
from .context import _builtin_context_processors
from .exceptions import TemplateDoesNotExist
from .library import import_library
from typing import Any, Optional

from django.template.base import Origin, Template
from django.template.library import Library
from django.template.loaders.base import Loader
from django.template.loaders.cached import Loader
from django.template.loaders.filesystem import Loader
from django.template.loaders.locmem import Loader
from django.utils.safestring import SafeText
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
class Engine:
    default_builtins: Any = ...
    dirs: Any = ...
    app_dirs: Any = ...
    autoescape: Any = ...
    context_processors: Any = ...
    debug: Any = ...
    loaders: Any = ...
    string_if_invalid: Any = ...
    file_charset: Any = ...
    libraries: Any = ...
    template_libraries: Any = ...
    builtins: Any = ...
    template_builtins: Any = ...
    def __init__(self, dirs: Optional[List[str]] = ..., app_dirs: bool = ..., context_processors: Optional[Union[List[str], Tuple[str, str]]] = ..., debug: bool = ..., loaders: Any = ..., string_if_invalid: str = ..., file_charset: str = ..., libraries: Optional[Dict[str, str]] = ..., builtins: Optional[List[str]] = ..., autoescape: bool = ...) -> None: ...
    @staticmethod
    def get_default() -> Engine: ...
    def template_context_processors(self) -> Union[Tuple[Callable, Callable, Callable], Tuple[Callable], Tuple[Callable, Callable, Callable, Callable, Callable], Tuple[Callable, Callable]]: ...
    def get_template_builtins(self, builtins: List[str]) -> List[Library]: ...
    def get_template_libraries(self, libraries: Dict[str, str]) -> Dict[str, Library]: ...
    def template_loaders(self) -> Union[List[Loader], List[Loader], List[Loader]]: ...
    def get_template_loaders(self, template_loaders: Any) -> Any: ...
    def find_template_loader(self, loader: Union[Tuple[str, List[Tuple[str, Dict[str, str]]]], Tuple[str, List[str]], Tuple[str, Dict[str, str]], str]) -> Loader: ...
    def find_template(self, name: str, dirs: None = ..., skip: Optional[List[Origin]] = ...) -> Tuple[Template, Origin]: ...
    def from_string(self, template_code: str) -> Template: ...
    def get_template(self, template_name: str) -> Template: ...
    def render_to_string(self, template_name: str, context: Any = ...) -> SafeText: ...
    def select_template(self, template_name_list: List[str]) -> Template: ...
