# Stubs for django.forms.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import UserList
from typing import Any, Optional

from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.safestring import SafeText
from typing import Callable, Dict, List, Optional, Tuple, Type, Union
def pretty_name(name: str) -> str: ...
def flatatt(attrs: Dict[str, Optional[str]]) -> SafeText: ...

class ErrorDict(dict):
    def as_data(self) -> Dict[str, List[ValidationError]]: ...
    def get_json_data(self, escape_html: bool = ...) -> Dict[str, List[Dict[str, str]]]: ...
    def as_json(self, escape_html: bool = ...) -> str: ...
    def as_ul(self) -> SafeText: ...
    def as_text(self): ...
    def __str__(self): ...

class ErrorList(UserList, list):
    error_class: str = ...
    def __init__(self, initlist: Optional[Union[ErrorList, List[str], List[ValidationError]]] = ..., error_class: Optional[str] = ...) -> None: ...
    def as_data(self) -> List[ValidationError]: ...
    def get_json_data(self, escape_html: bool = ...) -> List[Dict[str, str]]: ...
    def as_json(self, escape_html: bool = ...): ...
    def as_ul(self) -> str: ...
    def as_text(self) -> str: ...
    def __str__(self): ...
    def __repr__(self) -> str: ...
    def __contains__(self, item: str) -> bool: ...
    def __eq__(self, other: Union[ErrorList, List[str]]) -> bool: ...
    def __getitem__(self, i: Union[str, int]) -> str: ...
    def __reduce_ex__(self, *args: Any, **kwargs: Any) -> Tuple[Callable, Tuple[Type[ErrorList]], Dict[str, Union[List[ValidationError], str]], None, None]: ...

def from_current_timezone(value: datetime) -> datetime: ...
def to_current_timezone(value: datetime) -> datetime: ...
