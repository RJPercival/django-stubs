# Stubs for django.db.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.apps.config import AppConfig
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.contrib.sites.models import Site
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model
from typing import Any, Callable, Dict, List, Type, Union
DEFAULT_DB_ALIAS: str
DJANGO_VERSION_PICKLE_KEY: str

class Error(Exception): ...
class InterfaceError(Error): ...
class DatabaseError(Error): ...
class DataError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...

class DatabaseErrorWrapper:
    wrapper: Any = ...
    def __init__(self, wrapper: DatabaseWrapper) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...
    def __call__(self, func: Callable) -> Callable: ...

def load_backend(backend_name: str) -> Any: ...

class ConnectionDoesNotExist(Exception): ...

class ConnectionHandler:
    _databases: Any = ...
    _connections: Any = ...
    def __init__(self, databases: Dict[str, Dict[str, str]] = ...) -> None: ...
    def databases(self) -> Dict[str, Dict[str, str]]: ...
    def ensure_defaults(self, alias: str) -> None: ...
    def prepare_test_settings(self, alias: str) -> None: ...
    def __getitem__(self, alias: str) -> BaseDatabaseWrapper: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self): ...
    def all(self) -> List[DatabaseWrapper]: ...
    def close_all(self) -> None: ...

class ConnectionRouter:
    _routers: Any = ...
    def __init__(self, routers: None = ...) -> None: ...
    def routers(self) -> List[object]: ...
    def _router_func(action: Any): ...
    db_for_read: Any = ...
    db_for_write: Any = ...
    def allow_relation(self, obj1: Model, obj2: Model, **hints: Any) -> bool: ...
    def allow_migrate(self, db: str, app_label: str, **hints: Any) -> bool: ...
    def allow_migrate_model(self, db: str, model: Type[Model]) -> bool: ...
    def get_migratable_models(self, app_config: AppConfig, db: str, include_auto_created: bool = ...) -> Union[List[Type[Model]], List[Type[Site]], List[Type[Session]], List[Type[ContentType]]]: ...
