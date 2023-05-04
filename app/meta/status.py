from enum import Enum

class Status(Enum):
    Ok = "ok"
    Error = "error"
    Failed = "failed"
    Unauthenticated = "unauthenticated"