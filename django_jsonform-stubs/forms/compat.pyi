from json import JSONDecoder, JSONEncoder
from typing import Any, Optional
from django.utils.functional import _StrOrPromise

from django import forms

class JSONFormField(forms.CharField):
    default_error_messages: dict[str, _StrOrPromise]
    encoder: Optional[JSONEncoder]
    decoder: Optional[JSONDecoder]
    def __init__(
        self,
        encoder: Optional[JSONEncoder] = ...,
        decoder: Optional[JSONDecoder] = ...,
        **kwargs: Any,
    ) -> None: ...
    def to_python(self, value: Any) -> Any: ...
    def bound_data(self, data: Any, initial: Any) -> Any: ...
    def prepare_value(self, value: Any) -> str: ...
    def has_changed(self, initial: Any, data: Any) -> bool: ...

class InvalidJSONInput(str): ...
class JSONString(str): ...
