from .yamldecode import YamlDecoder
from .yamlencode import YamlEncoder


def dumps(obj):
    return YamlEncoder().yaml_encode(obj)


def loads(obj):
    return YamlDecoder().yaml_decode(obj)
