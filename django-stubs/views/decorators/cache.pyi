# Stubs for django.views.decorators.cache (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from typing import Callable
def cache_page(timeout: float, *, cache: Optional[Any] = ..., key_prefix: Optional[Any] = ...) -> Callable: ...
def cache_control(**kwargs: Any): ...
def never_cache(view_func: Callable) -> Callable: ...
