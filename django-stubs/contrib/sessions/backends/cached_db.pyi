# Stubs for django.contrib.sessions.backends.cached_db (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.sessions.backends.db import SessionStore as DBStore
from typing import Any, Optional

from typing import Any, Dict, Optional
KEY_PREFIX: str

class SessionStore(DBStore):
    cache_key_prefix: Any = ...
    _cache: Any = ...
    def __init__(self, session_key: Optional[str] = ...) -> None: ...
    @property
    def cache_key(self) -> str: ...
    def load(self) -> Dict[Any, Any]: ...
    def exists(self, session_key: str) -> bool: ...
    def save(self, must_create: bool = ...) -> None: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    _session_key: Any = ...
    def flush(self) -> None: ...
