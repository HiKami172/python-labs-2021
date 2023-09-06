from .jsondecode import JsonDecoder
from .jsonencode import JsonEncoder


def dumps(obj):
    return JsonEncoder().json_encode(obj)


def loads(obj):
    return JsonDecoder().json_decode(obj)
