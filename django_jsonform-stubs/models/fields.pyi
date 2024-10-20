from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from django.db.models import Model
from django.forms import JSONField as DjangoJSONField
from django.forms import Field

if TYPE_CHECKING:
    from django_jsonform.utils import ArraySchema, RootSchema
else:
    ArraySchema = object

django_major: int
django_minor: int

try:
    from django.contrib.postgres.fields import ArrayField as DjangoArrayField
except ImportError:
    class DjangoArrayField:  # type: ignore[no-redef]
        mock_field: bool

class JSONField(DjangoJSONField):
    schema: RootSchema
    pre_save_hook: Callable[[Any], Any]
    file_handler: str
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def formfield(self, **kwargs: Any) -> Field: ...  # type: ignore[override]
    def pre_save(self, model_instance: Model, add: bool) -> Any: ...

class ArrayField(DjangoArrayField):
    nested: bool
    schema: ArraySchema
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def formfield(self, **kwargs: Any) -> Field: ...  # type: ignore[override]
