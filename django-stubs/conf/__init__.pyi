# Stubs for django.conf (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.utils.functional import LazyObject
from typing import Any, Optional

from typing import Any, List
ENVIRONMENT_VARIABLE: str
class LazySettings(LazyObject):
    _wrapped: Any = ...
    def _setup(self, name: None = ...) -> None: ...
    def __repr__(self): ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: object) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def configure(self, default_settings: Any = ..., **options: Any) -> None: ...
    @property
    def configured(self) -> bool: ...

class Settings:
    SETTINGS_MODULE: Any = ...
    _explicit_settings: Any = ...
    def __init__(self, settings_module: str) -> None: ...
    def is_overridden(self, setting: str) -> bool: ...
    def __repr__(self): ...

class UserSettingsHolder:
    SETTINGS_MODULE: Any = ...
    default_settings: Any = ...
    def __init__(self, default_settings: Any) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...
    def __dir__(self) -> List[str]: ...
    def is_overridden(self, setting: Any): ...
    def __repr__(self): ...

settings = LazySettings()
settings: Any
