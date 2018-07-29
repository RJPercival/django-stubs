# Stubs for django.core.checks.urls (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.core.checks.messages import Error, Warning
from django.urls.resolvers import URLPattern, URLResolver
from typing import Any, Callable, List, Tuple, Union
def check_url_config(app_configs: None, **kwargs: Any) -> List[Warning]: ...
def check_resolver(resolver: Union[URLPattern, URLResolver]) -> Union[List[Warning], List[Error]]: ...
def check_url_namespaces_unique(app_configs: None, **kwargs: Any) -> List[Any]: ...
def _load_all_namespaces(resolver: URLResolver, parents: Tuple = ...) -> List[str]: ...
def get_warning_for_invalid_pattern(pattern: Tuple[str, Callable]) -> List[Error]: ...
def check_url_settings(app_configs: None, **kwargs: Any) -> List[Error]: ...
def E006(name: str) -> Error: ...
