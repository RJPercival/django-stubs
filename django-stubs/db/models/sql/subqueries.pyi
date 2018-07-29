# Stubs for django.db.models.sql.subqueries (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models.sql.query import Query
from typing import Any

from django.db.models.base import Model
from django.db.models.fields import CharField
from django.db.models.query import QuerySet
from django.db.models.sql.where import WhereNode
from typing import Any, Dict, List, Optional, Type, Union
class DeleteQuery(Query):
    compiler: str = ...
    alias_map: Any = ...
    where: Any = ...
    def do_query(self, table: str, where: WhereNode, using: str) -> int: ...
    def delete_batch(self, pk_list: Union[List[int], List[str]], using: str) -> int: ...
    def delete_qs(self, query: QuerySet, using: str) -> int: ...

class UpdateQuery(Query):
    compiler: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    values: Any = ...
    related_ids: Any = ...
    related_updates: Any = ...
    def _setup_query(self) -> None: ...
    def clone(self) -> UpdateQuery: ...
    where: Any = ...
    def update_batch(self, pk_list: List[int], values: Dict[str, Optional[int]], using: str) -> None: ...
    def add_update_values(self, values: Dict[str, Any]) -> None: ...
    def add_update_fields(self, values_seq: Any) -> None: ...
    def add_related_update(self, model: Type[Model], field: CharField, value: str) -> None: ...
    def get_related_updates(self) -> List[UpdateQuery]: ...

class InsertQuery(Query):
    compiler: str = ...
    fields: Any = ...
    objs: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    raw: Any = ...
    def insert_values(self, fields: Any, objs: Any, raw: bool = ...) -> None: ...

class AggregateQuery(Query):
    compiler: str = ...
    def add_subquery(self, query: Query, using: str) -> None: ...
