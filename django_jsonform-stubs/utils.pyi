from collections.abc import Sequence
from typing import Any, Optional, TypedDict, Union, overload
from typing import Required, Literal

from django.utils.functional import _StrOrPromise

@overload
def normalize_schema(schema: list[Any]) -> list[Any]: ...
@overload
def normalize_schema(schema: dict[str, Any]) -> dict[str, Any]: ...
@overload
def normalize_schema(schema: Any) -> Union[dict[str, Any], list[Any]]: ...
def normalize_keyword(kw: Optional[str]) -> Optional[str]: ...
def get_schema_type(schema: dict[str, Any]) -> Optional[str]: ...
def get_setting(name: str, default: Optional[str] = ...) -> Optional[str]: ...
def join_coords(*coords: Union[str, int]) -> str: ...
def split_coords(coords: str) -> list[str]: ...

Coords = Sequence[Union[int, str]]
Message = Union[str, list[str]]

class ErrorMap(dict):
    def set(self, coords: Coords, msg: Message) -> None: ...
    def append(self, coords: Coords, msg: Message) -> None: ...

def _get_django_version() -> tuple[int, int]: ...

class TitledStringChoice(TypedDict):
    title: _StrOrPromise
    value: str

class TitledNumberChoice(TypedDict):
    title: _StrOrPromise
    value: float

class TitledIntegerChoice(TypedDict):
    title: _StrOrPromise
    value: int

class TitledBooleanChoice(TypedDict):
    title: _StrOrPromise
    value: bool

class LabeledStringChoice(TypedDict):
    label: _StrOrPromise
    value: str

class LabeledNumberChoice(TypedDict):
    label: _StrOrPromise
    value: float

class LabeledIntegerChoice(TypedDict):
    label: _StrOrPromise
    value: int

class LabeledBooleanChoice(TypedDict):
    label: _StrOrPromise
    value: bool

BooleanChoices = Sequence[Union[bool, TitledBooleanChoice, LabeledBooleanChoice]]
NumberChoices = Sequence[Union[float, TitledNumberChoice, LabeledNumberChoice]]
IntegerChoices = Sequence[Union[int, TitledIntegerChoice, LabeledIntegerChoice]]
StringChoices = Sequence[Union[str, TitledStringChoice, LabeledStringChoice]]
AnyChoices = Union[BooleanChoices, NumberChoices, IntegerChoices, StringChoices]

class BaseFieldSchema(TypedDict, total=False):
    title: _StrOrPromise

class ArraySchema(BaseFieldSchema, total=False):
    type: Required[Literal["array", "list"]]
    items: Required[AnySchema]
    default: Any
    minItems: int
    min_items: int
    maxItems: int
    max_items: int
    uniqueItems: bool

class ObjectSchema(BaseFieldSchema, total=False):
    type: Required[Literal["object", "dict"]]
    properties: dict[str, AnySchema]
    keys: dict[str, AnySchema]
    required: Sequence[str]
    additionalProperties: Union[bool, AnySchema]
    oneOf: list[Any]  # TODO
    anyOf: list[Any]  # TODO
    allOf: list[Any]  # TODO

class BaseInputFieldSchema(BaseFieldSchema, total=False):
    help_text: _StrOrPromise
    helpText: _StrOrPromise  # alias for help_text
    required: bool

class StringSchema(BaseInputFieldSchema, total=False):
    type: Required[Literal["string"]]
    format: Literal[
        "color",
        "date",
        "date-time",
        "datetime",  # alias date-time
        "email",
        "password",
        "time",
        "data-url",
        "file-url",
        "uri",
        "uri-reference",
    ]
    enum: StringChoices
    choices: StringChoices  # alias for enum
    widget: Literal[
        "textarea",
        "radio",
        "autocomplete",
        "multiselect",  # only valid, if hold in an array
        "multiselect-autocomplete",
        "fileinput",
        "hidden",
    ]
    default: str
    readonly: bool
    readOnly: bool  # alias for readonly
    placeholder: str
    minLength: int
    maxLength: int
    handler: str

class NumberSchema(BaseInputFieldSchema, total=False):
    type: Required[Literal["number"]]
    choices: NumberChoices
    enum: NumberChoices  # alias for choices
    widget: Literal["range"]
    default: float
    readonly: bool
    readOnly: bool  # alias for readonly
    placeholder: float
    minimum: float
    maximum: float
    exclusiveMinimum: float
    exclusiveMaximum: float

class IntegerSchema(BaseInputFieldSchema, total=False):
    type: Required[Literal["integer"]]
    choices: IntegerChoices
    enum: IntegerChoices  # alias for choices
    widget: Literal["range"]
    default: int
    readonly: bool
    readOnly: bool  # alias for readonly
    placeholder: int
    minimum: int
    maximum: int
    exclusiveMinimum: int
    exclusiveMaximum: int

class BooleanSchema(BaseInputFieldSchema, total=False):
    type: Required[Literal["boolean"]]
    choices: BooleanChoices
    enum: BooleanChoices  # alias for choices
    widget: Literal["radio", "select"]
    default: bool
    readonly: bool
    readOnly: bool  # alias for readonly

class ConstSchema(BaseFieldSchema, total=False):
    const: Required[_StrOrPromise]

InputFieldSchema = Union[
    StringSchema,
    NumberSchema,
    IntegerSchema,
    BooleanSchema,
    ConstSchema,
]
Reference = TypedDict("Reference", {"$ref": str})

class OneOfSchema(TypedDict):
    # TODO:
    pass

class AnyOfSchema(TypedDict):
    # TODO:
    pass

class AllOfSchema(TypedDict):
    # TODO:
    pass

AnySchema = Union[InputFieldSchema, ArraySchema, ObjectSchema, Reference]
RootSchema = Union[ArraySchema, ObjectSchema]
