# Stubs for django.core.mail.backends.filebased (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from typing import Any, Optional

from django.core.mail.message import EmailMessage
class EmailBackend(ConsoleEmailBackend):
    _fname: Any = ...
    file_path: Any = ...
    def __init__(self, *args: Any, file_path: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def write_message(self, message: EmailMessage) -> None: ...
    def _get_filename(self) -> str: ...
    stream: Any = ...
    def open(self) -> bool: ...
    def close(self) -> None: ...
