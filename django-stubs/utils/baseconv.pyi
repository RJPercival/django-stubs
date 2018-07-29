# Stubs for django.utils.baseconv (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

from typing import Tuple, Union
BASE2_ALPHABET: str
BASE16_ALPHABET: str
BASE56_ALPHABET: str
BASE36_ALPHABET: str
BASE62_ALPHABET: str
BASE64_ALPHABET: Any

class BaseConverter:
    decimal_digits: str = ...
    sign: Any = ...
    digits: Any = ...
    def __init__(self, digits: Any, sign: str = ...) -> None: ...
    def __repr__(self): ...
    def encode(self, i: int) -> str: ...
    def decode(self, s: str) -> int: ...
    def convert(self, number: Union[str, int], from_digits: str, to_digits: str, sign: str) -> Tuple[int, str]: ...

base2: Any
base16: Any
base36: Any
base56: Any
base62: Any
base64: Any
