# Stubs for django.db.migrations.optimizer (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class MigrationOptimizer:
    _iterations: int = ...
    def optimize(self, operations: Any, app_label: Optional[str] = ...) -> Any: ...
    def optimize_inner(self, operations: Any, app_label: Optional[str] = ...) -> Any: ...
