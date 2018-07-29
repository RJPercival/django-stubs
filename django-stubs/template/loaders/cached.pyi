# Stubs for django.template.loaders.cached (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .base import Loader as BaseLoader
from typing import Any, Optional

from django.template.base import Origin, Template
from django.template.engine import Engine
from typing import Dict, List, Optional, Tuple, Union
class Loader(BaseLoader):
    template_cache: Any = ...
    get_template_cache: Any = ...
    loaders: Any = ...
    def __init__(self, engine: Engine, loaders: Union[List[Tuple[str, Dict[str, str]]], List[str]]) -> None: ...
    def get_contents(self, origin: Origin) -> str: ...
    def get_template(self, template_name: str, skip: Optional[List[Origin]] = ...) -> Template: ...
    def get_template_sources(self, template_name: str) -> None: ...
    def cache_key(self, template_name: str, skip: Optional[List[Origin]] = ...) -> str: ...
    def generate_hash(self, values: List[str]) -> str: ...
    def reset(self) -> None: ...
