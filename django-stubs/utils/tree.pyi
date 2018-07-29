# Stubs for django.utils.tree (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.db.models.query_utils import Q
from django.db.models.sql.where import WhereNode
from typing import Any, Dict, Optional, Tuple
class Node:
    default: str = ...
    children: Any = ...
    connector: Any = ...
    negated: Any = ...
    def __init__(self, children: Any = ..., connector: Optional[str] = ..., negated: bool = ...) -> None: ...
    @classmethod
    def _new_instance(cls, children: Any = ..., connector: str = ..., negated: bool = ...) -> WhereNode: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __deepcopy__(self, memodict: Dict[Any, Any]) -> Q: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __contains__(self, other: Tuple[str, int]) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def add(self, data: Any, conn_type: str, squash: bool = ...) -> Any: ...
    def negate(self) -> None: ...
