from typing import Any, Optional

from django.core.exceptions import ValidationError
from django.utils.functional import _StrOrPromise
from django_jsonform.utils import ErrorMap

class JSONSchemaValidationError(ValidationError):
    error_map: Optional[ErrorMap]

    def __init__(
        self,
        # Accepts arbitrarily nested data structure, mypy doesn't allow describing it accurately.
        message: _StrOrPromise | ValidationError | dict[str, Any] | list[Any],
        code: Optional[str] = ...,
        params: Optional[dict[str, Any]] = ...,
        error_map: Optional[ErrorMap] = None,
    ) -> None: ...
