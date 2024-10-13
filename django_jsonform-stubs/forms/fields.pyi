from json import JSONDecoder, JSONEncoder
from tkinter import Widget
from typing import Any, Optional

from django.contrib.postgres.forms import SimpleArrayField
from django.db import models as models
from django.forms import Field
from django_jsonform.forms.compat import JSONFormField as DjangoJSONFormField
from django_jsonform.utils import ErrorMap, RootSchema
from django_jsonform.widgets import JSONFormWidget

django_major: int
django_minor: int

try:
    from django.contrib.postgres.forms import SimpleArrayField
except ImportError:
    class SimpleArrayField:
        mock_field: bool

class JSONFormField(DjangoJSONFormField):
    file_handler: str
    widget: JSONFormWidget
    def __init__(
        self,
        *,
        schema: Optional[RootSchema] = ...,
        encoder: Optional[JSONEncoder] = ...,
        decoder: Optional[JSONDecoder] = ...,
        model_name: str = ...,
        file_handler: str = ...,
        **kwargs: Any,
    ) -> None: ...
    def validate(self, value: Any) -> None: ...
    def run_validators(self, value: Any) -> None: ...
    def add_error(self, error_map: ErrorMap) -> None: ...

class ArrayFormField(SimpleArrayField):
    base_field: Field
    max_items: int
    min_items: int
    nested: bool
    schema: RootSchema
    widget: Widget
    def __init__(self, base_field: Field, **kwargs: Any) -> None: ...
    def prepare_value(self, value: Any) -> Any: ...
    def to_python(self, value: Any) -> Any: ...
    def get_schema(self): ...
