from typing import Any

from django.forms.renderers import BaseRenderer
from django.forms.widgets import Media, Widget
from django.utils.safestring import SafeString
from django_jsonform.utils import ErrorMap, RootSchema
from typing_extensions import Optional

class JSONFormWidget(Widget):
    template_name: str
    schema: RootSchema
    model_name: str
    file_handler: str
    validate_on_submit: bool

    def __init__(
        self,
        schema: RootSchema,
        model_name: str = ...,
        file_handler: str = ...,
        validate_on_submit: bool = ...,
        attrs: Optional[dict[str, Any]] = ...,
    ) -> None: ...
    def get_schema(self) -> RootSchema: ...
    def render(
        self,
        name: str,
        value: Any,
        attrs: Optional[dict[str, Any]] = ...,
        renderer: Optional[BaseRenderer] = ...,
    ) -> SafeString: ...
    def add_error(self, error_map: ErrorMap) -> None: ...
    @property
    def media(self) -> Media: ...
