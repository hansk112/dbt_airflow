from _typeshed import StrOrBytesPath
from typing import Generic, TypeVar
from contextlib import AbstractContextManager

_T_fd_or_any_path = TypeVar("_T_fd_or_any_path", bound=int | StrOrBytesPath)

class chdir(AbstractContextManager[None], Generic[_T_fd_or_any_path]):
    path: _T_fd_or_any_path
    def __init__(self, path: _T_fd_or_any_path) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *excinfo: object) -> None: ...
