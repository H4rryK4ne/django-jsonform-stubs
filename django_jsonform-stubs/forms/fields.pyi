from _typeshed import Incomplete
from django.contrib.postgres.forms import SimpleArrayField
from django.db import models as models
from django_jsonform.exceptions import JSONSchemaValidationError as JSONSchemaValidationError
from django_jsonform.forms.compat import JSONFormField as DjangoJSONFormField
from django_jsonform.validators import JSONSchemaValidator as JSONSchemaValidator
from django_jsonform.widgets import JSONFormWidget as JSONFormWidget

django_major: Incomplete
django_minor: Incomplete

class SimpleArrayField:
    mock_field: bool

class JSONFormField(DjangoJSONFormField):
    file_handler: Incomplete
    widget: Incomplete
    def __init__(self, *, schema: Incomplete | None = ..., encoder: Incomplete | None = ..., decoder: Incomplete | None = ..., model_name: str = ..., file_handler: str = ..., **kwargs) -> None: ...
    def validate(self, value) -> None: ...
    def run_validators(self, value) -> None: ...
    def add_error(self, error_map) -> None: ...

class ArrayFormField(SimpleArrayField):
    base_field: Incomplete
    max_items: Incomplete
    min_items: Incomplete
    nested: Incomplete
    schema: Incomplete
    widget: Incomplete
    def __init__(self, base_field, **kwargs) -> None: ...
    def prepare_value(self, value): ...
    def to_python(self, value): ...
    def get_schema(self): ...
