# Stubs for django.contrib.sites.managers (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db import models
from typing import Any, Optional

from django.core.checks.messages import Error
from django.db.models.query import QuerySet
from typing import List
class CurrentSiteManager(models.Manager):
    use_in_migrations: bool = ...
    __field_name: Any = ...
    def __init__(self, field_name: None = ...) -> None: ...
    def check(self, **kwargs: Any) -> List[Error]: ...
    def _check_field_name(self) -> List[Error]: ...
    def _get_field_name(self) -> str: ...
    def get_queryset(self) -> QuerySet: ...
