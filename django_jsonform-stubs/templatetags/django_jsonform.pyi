from datetime import datetime, time

from django.template import Library

register: Library

def parse_datetime(value: str) -> datetime: ...
def parse_time(value: str) -> time: ...
