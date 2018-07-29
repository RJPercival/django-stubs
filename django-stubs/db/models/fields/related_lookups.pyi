# Stubs for django.db.models.fields.related_lookups (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.models.lookups import Exact, GreaterThan, GreaterThanOrEqual, In, IsNull, LessThan, LessThanOrEqual
from typing import Any

from collections import OrderedDict
from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.expressions import Col
from django.db.models.fields import AutoField, IntegerField
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
from typing import Any, List, Tuple, Type, Union
from uuid import UUID
class MultiColSource:
    contains_aggregate: bool = ...
    output_field: Any = ...
    def __init__(self, alias: str, targets: Union[Tuple[IntegerField, related.ForeignKey], Tuple[IntegerField, IntegerField]], sources: Union[Tuple[IntegerField, AutoField], Tuple[AutoField, IntegerField]], field: related.ForeignObject) -> None: ...
    def __repr__(self): ...
    def relabeled_clone(self, relabels: OrderedDict) -> MultiColSource: ...
    def get_lookup(self, lookup: str) -> Type[Union[RelatedExact, RelatedIn]]: ...

def get_normalized_value(value: Any, lhs: Union[MultiColSource, Col]) -> Any: ...

class RelatedIn(In):
    rhs: Any = ...
    def get_prep_lookup(self) -> Union[Query, List[int], List[UUID], List[str]]: ...
    def as_sql(self, compiler: SQLCompiler, connection: DatabaseWrapper) -> Union[Tuple[str, List[int]], Tuple[str, List[str]], Tuple[str, List[Any]]]: ...

class RelatedLookupMixin:
    rhs: Any = ...
    def get_prep_lookup(self) -> Any: ...
    def as_sql(self, compiler: SQLCompiler, connection: DatabaseWrapper) -> Union[Tuple[str, List[int]], Tuple[str, List[str]], Tuple[str, List[Any]]]: ...

class RelatedExact(RelatedLookupMixin, Exact): ...
class RelatedLessThan(RelatedLookupMixin, LessThan): ...
class RelatedGreaterThan(RelatedLookupMixin, GreaterThan): ...
class RelatedGreaterThanOrEqual(RelatedLookupMixin, GreaterThanOrEqual): ...
class RelatedLessThanOrEqual(RelatedLookupMixin, LessThanOrEqual): ...
class RelatedIsNull(RelatedLookupMixin, IsNull): ...
