from _typeshed import Incomplete
from django.contrib.postgres.fields import ArrayField as DjangoArrayField
from django_jsonform.forms.fields import ArrayFormField as ArrayFormField, JSONFormField as JSONFormField
from django_jsonform.models.compat import JSONField as DjangoJSONField

django_major: Incomplete
django_minor: Incomplete

class DjangoArrayField:
    mock_field: bool

class JSONField(DjangoJSONField):
    schema: Incomplete
    pre_save_hook: Incomplete
    file_handler: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def formfield(self, **kwargs): ...
    def pre_save(self, model_instance, add): ...

class ArrayField(DjangoArrayField):
    nested: Incomplete
    schema: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def formfield(self, **kwargs): ...
