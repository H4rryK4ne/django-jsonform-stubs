from collections.abc import Callable
from typing import Optional, Union

from django.http import HttpRequest, HttpResponseNotAllowed, JsonResponse

module_path: str
handler_func: str
FILE_UPLOAD_HANDLER: Optional[Callable[[HttpRequest], JsonResponse]]

def upload_handler(
    request: HttpRequest,
) -> Union[JsonResponse, HttpResponseNotAllowed]: ...
