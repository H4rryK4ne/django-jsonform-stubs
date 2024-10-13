from _typeshed import Incomplete
from django.core.exceptions import ValidationError

class JSONSchemaValidationError(ValidationError):
    error_map: Incomplete
    def __init__(self, message, code: Incomplete | None = ..., params: Incomplete | None = ..., error_map: Incomplete | None = ...) -> None: ...
