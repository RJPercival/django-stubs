# Stubs for django.templatetags.tz (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from datetime import datetime
from django.template import Node
from typing import Any

from django.template.base import FilterExpression, NodeList, Parser, Token
from django.template.context import Context
from django.utils.safestring import SafeText
from django.utils.timezone import FixedOffset
from typing import Optional, Union
register: Any

class datetimeobject(datetime): ...

def localtime(value: Optional[Union[str, datetime]]) -> Union[str, datetimeobject]: ...
def utc(value: Optional[Union[str, datetime]]) -> Union[str, datetimeobject]: ...
def do_timezone(value: datetime, arg: FixedOffset) -> datetimeobject: ...

class LocalTimeNode(Node):
    nodelist: Any = ...
    use_tz: Any = ...
    def __init__(self, nodelist: NodeList, use_tz: bool) -> None: ...
    def render(self, context: Context) -> SafeText: ...

class TimezoneNode(Node):
    nodelist: Any = ...
    tz: Any = ...
    def __init__(self, nodelist: NodeList, tz: FilterExpression) -> None: ...
    def render(self, context: Context) -> SafeText: ...

class GetCurrentTimezoneNode(Node):
    variable: Any = ...
    def __init__(self, variable: str) -> None: ...
    def render(self, context: Context) -> str: ...

def localtime_tag(parser: Parser, token: Token) -> LocalTimeNode: ...
def timezone_tag(parser: Parser, token: Token) -> TimezoneNode: ...
def get_current_timezone_tag(parser: Parser, token: Token) -> GetCurrentTimezoneNode: ...
