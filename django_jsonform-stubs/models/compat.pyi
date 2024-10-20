from collections.abc import Sequence
from json import JSONDecoder, JSONEncoder
from typing import Any, Optional

from _typeshed import Incomplete
from django.db.models import Model, TextField
from django.forms import Field
from django.utils.functional import _StrOrPromise

class JSONField(TextField):
    encoder: JSONEncoder
    decoder: JSONDecoder

    def __init__(
        self,
        verbose_name: Optional[_StrOrPromise] = ...,
        name: Optional[str] = ...,
        encoder: Optional[JSONEncoder] = ...,
        decoder: Optional[JSONDecoder] = ...,
        **kwargs: Any,
    ) -> None: ...
    def deconstruct(self) -> tuple[str, str, Sequence[Any], dict[str, Any]]: ...
    def to_python(self, value: Any) -> Any: ...
    def from_db_value(self, value: Any, expression: Incomplete, connection: Incomplete) -> Any: ...
    def get_prep_value(self, value: Any) -> Optional[str]: ...
    def validate(self, value: Any, model_instance: Optional[Model]) -> None: ...
    def value_to_string(self, obj: Model) -> str: ...
    def formfield(self, **kwargs: Any) -> Field: ...  # type: ignore[override]
