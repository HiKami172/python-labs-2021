from lib.json import jsonparser
from lib.yaml import yamlparser


class Serializer:
    def __init__(self):
        self.parsers = dict()

    def add_parser(self, format, parser):
        self.parsers[format.lower()] = parser

    def get_parser(self, format):
        parser = self.parsers.get(format.lower())
        if not parser:
            raise ValueError(format)
        return parser()

    def get_formats(self):
        return list(self.parsers.keys())


serializer = Serializer()
serializer.add_parser("JSON", jsonparser.JsonParser)
serializer.add_parser("YAML", yamlparser.YamlParser)
