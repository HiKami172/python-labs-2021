class YamlEncoder:
    def __init__(self, tab="  ", crlf="\n"):
        self.nesting_level = -1
        self.tab = tab
        self.crlf = crlf

    def add_tab(self, level=-1):
        if level != -1:
            self.nesting_level = level
        return self.nesting_level * self.tab

    def dict_to_yaml(self, objs):
        bracket = self.yaml_brackets[type(objs)]
        if not objs:
            return bracket[0] + bracket[1]
        self.nesting_level += 1
        if self.nesting_level == 0:
            res = ""
        else:
            res = self.crlf
        return (
                res
                + self.crlf.join(
            [
                str(
                    self.add_tab()
                    + self.yaml_encode(key)
                    + ": "
                    + self.yaml_encode(value)
                )
                for key, value in objs.items()
            ]
        )
                + self.add_tab(self.nesting_level - 1)
        )

    def array_to_yaml(self, objs):
        bracket = self.yaml_brackets[type(objs)]
        if not objs:
            return bracket[0] + bracket[1]
        self.nesting_level += 1
        return (
                self.crlf
                + self.crlf.join(
            [str(self.add_tab() + "- " + self.yaml_encode(obj)) for obj in objs]
        )
                + self.add_tab(self.nesting_level - 1)
        )

    def primitive_to_yaml(self, obj):
        return str(obj)

    def bool_to_yaml(self, obj):
        return str(obj).lower()

    def none_to_yaml(self, obj):
        return "null"

    def string_to_yaml(self, obj):
        bracket = self.yaml_brackets[type(obj)]
        return bracket[0] + str(obj) + bracket[1]

    def yaml_encode(self, obj):
        if type(obj) in self.yaml_type:
            return self.yaml_type[type(obj)](self, obj)
        else:
            raise ValueError("can't encode: ", type(obj))

    yaml_brackets = {
        dict: ("{", "}"),
        list: ("[", "]"),
        tuple: ("[", "]"),
        str: ('"', '"'),
    }

    yaml_type = {
        int: primitive_to_yaml,
        float: primitive_to_yaml,
        str: string_to_yaml,
        bool: bool_to_yaml,
        dict: dict_to_yaml,
        list: array_to_yaml,
        tuple: array_to_yaml,
        type(None): none_to_yaml,
    }
