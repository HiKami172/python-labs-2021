class YamlDecoder:
    int_const = tuple("1 2 3 4 5 6 7 8 9 0".split(" "))

    def __init__(self):
        self.yaml_to_true = self.yaml_to_custom("true", True);
        self.yaml_to_false = self.yaml_to_custom("false", False);
        self.yaml_to_none = self.yaml_to_custom("null", None);

        self.yaml_types = [
            ("{", self.yaml_to_dict),
            ("-", self.yaml_to_list),
            ('"', self.yaml_to_string),
            (self.int_const, self.yaml_to_numeric),
            ("false", self.yaml_to_false),
            ("true", self.yaml_to_true),
            ("null", self.yaml_to_none)
        ]

    def yaml_to_custom(self, word, value=None):
        def custom_conversion(obj):
            if obj.startswith(word):
                return value, obj[len(word):]

        custom_conversion.__name__ = "parse_%s" % word
        return custom_conversion

    def yaml_to_dict(self, objs):
        res = {}
        while True:
            (key, objs) = self.yaml_to_obj(objs)
            objs = remove_prefix(objs, ":")
            (value, objs) = self.yaml_to_obj(objs)
            res[key] = value
            objs = remove_prefix(objs, ",").lstrip()
        return res, remove_prefix(objs, "}")

    def yaml_to_list(self, objs):
        res = []
        arr = objs.split('\n')
        for obj in arr:
            tmp = obj
            obj = obj.lstrip()
            obj = remove_prefix(obj, "-").lstrip()
            item = self.yaml_to_obj(obj)
            res.append(item[0])
            objs = objs.replace(tmp, '')
            objs = remove_prefix(objs, "\n")
        return res, objs

    def yaml_to_numeric(self, obj):
        if self.check_for_dict(obj):
            return self.yaml_to_dict(obj)
        for i in range(len(obj)):
            if obj[i] not in self.int_const and obj[i] != ".":
                try:
                    return int(obj[:i]), obj[i:]
                except ValueError:
                    return float(obj[:i]), obj[i:]

        return int(obj[:i + 1]), obj[i + 1:]

    def yaml_to_string(self, obj):
        obj = remove_prefix(obj, '"')
        tmp = obj.find('"')
        obj_bound = obj[tmp + 1:]
        if self.check_for_dict(obj_bound):
            return self.yaml_to_dict(obj)
        return obj[:tmp], obj[tmp + 1:]

    def check_for_dict(self, obj) -> bool:
        for i in range(len(obj)):
            if obj[i] == ":":
                return True
        return False

    def yaml_to_obj(self, obj):
        obj = obj.lstrip()
        for (char, func) in self.yaml_types:
            if not obj:
                pass
            elif obj.startswith(char):
                return func(obj)

        raise ValueError(obj.split(",") + " is not supported!")

    def yaml_decode(self, obj):
        (item, obj) = self.yaml_to_obj(obj)
        obj = obj.lstrip()
        if obj != "":
            raise ValueError("Wrong format!")
        else:
            return item


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text
