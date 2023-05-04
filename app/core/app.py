from typing import TypedDict
from meta.fields import Fields
from meta.fields import Fields
from enum import Enum
        
class FieldError(TypedDict):
    field: str
    message: str

field_error = TypedDict('FieldError', field=str, message=str)

def validate(data: dict, field: Fields, validation, error_message, errors: list) -> list:
    f = data.get(field.value, None)
    if validation(f) is False or f is None:
        errors.append(FieldError(field=field.value, message=error_message))
    return errors