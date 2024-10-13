from typing import Union

from django.urls import URLPattern, URLResolver

app_name: str
urlpatterns: list[Union[URLPattern, URLResolver]]
