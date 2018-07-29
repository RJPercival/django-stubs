# Stubs for django.utils.html (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from html.parser import HTMLParser
from typing import Any, Optional

from django.db.models.base import Model
from django.utils.safestring import SafeText
from typing import Any, Dict, List, Optional, Tuple, Union
TRAILING_PUNCTUATION_CHARS: str
WRAPPING_PUNCTUATION: Any
DOTS: Any
unencoded_ampersands_re: Any
word_split_re: Any
simple_url_re: Any
simple_url_2_re: Any
_html_escapes: Any

def escape(text: Optional[Union[Model, int, str]]) -> SafeText: ...

_js_escapes: Any

def escapejs(value: str) -> SafeText: ...

_json_script_escapes: Any

def json_script(value: Dict[str, str], element_id: SafeText) -> SafeText: ...
def conditional_escape(text: Any) -> str: ...
def format_html(format_string: str, *args: Any, **kwargs: Any) -> SafeText: ...
def format_html_join(sep: str, format_string: str, args_generator: Union[List[Tuple[str]], List[Tuple[str, str]]]) -> SafeText: ...
def linebreaks(value: str, autoescape: bool = ...) -> str: ...

class MLStripper(HTMLParser):
    fed: Any = ...
    def __init__(self) -> None: ...
    def handle_data(self, d: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def handle_charref(self, name: str) -> None: ...
    def get_data(self) -> str: ...

def _strip_once(value: str) -> str: ...
def strip_tags(value: str) -> str: ...
def strip_spaces_between_tags(value: str) -> str: ...
def smart_urlquote(url: str) -> str: ...
def urlize(text: str, trim_url_limit: Optional[int] = ..., nofollow: bool = ..., autoescape: bool = ...) -> str: ...
def avoid_wrapping(value: str) -> str: ...
def html_safe(klass: Any): ...
