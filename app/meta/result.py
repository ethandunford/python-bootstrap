from enum import Enum
from typing import TypedDict
from typing import Optional
from meta.status import Status

class DbResult(TypedDict):
    status: Status
    data: Optional[dict] = None
    error: Optional[str] = None

db_result = TypedDict('dbResult', status=Status, data=dict, error=str)


class HttpResult(TypedDict):
    status: Status
    httpCode: int
    body: Optional[dict] = None
    error: Optional[str] = None


http_result = TypedDict('HttpResult', status=Status, data=dict, error=str)


class HttpResultSession(TypedDict):
    status: Status
    httpCode: int
    body: Optional[dict] = None
    error: Optional[str] = None
    session: str


http_resultSession = TypedDict('HttpResultSession', status=Status, data=dict, error=str, session=str)
