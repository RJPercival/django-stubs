# Stubs for django.contrib.staticfiles.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from collections import OrderedDict
from django.core.files.storage import DefaultStorage, FileSystemStorage
from typing import Iterator, List, Tuple, Union
def matches_patterns(path: str, patterns: Union[OrderedDict, List[str], Tuple[str]] = ...) -> bool: ...
def get_files(storage: Union[FileSystemStorage, DefaultStorage], ignore_patterns: List[str] = ..., location: str = ...) -> Iterator[str]: ...
def check_settings(base_url: str = ...) -> None: ...
