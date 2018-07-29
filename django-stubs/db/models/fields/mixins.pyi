# Stubs for django.db.models.fields.mixins (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from django.db.models.base import Model
from typing import Optional
NOT_PROVIDED: Any

class FieldCacheMixin:
    def get_cache_name(self) -> None: ...
    def get_cached_value(self, instance: Model, default: object = ...) -> Optional[Model]: ...
    def is_cached(self, instance: Model) -> bool: ...
    def set_cached_value(self, instance: Model, value: Optional[Model]) -> None: ...
    def delete_cached_value(self, instance: Model) -> None: ...
