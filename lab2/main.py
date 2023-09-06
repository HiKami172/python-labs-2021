from lib.factory import serializer


def main():
    l = [['lol', 'math', 54], ['pop', 8.46]]
    d = {
        56: "lol",
        "math": {
            "pi": 3.14,
            56.34: True,
            None: ["pop", "pip"]
        },
        21: [52, "string", False],
        True: False,
        None: 5.633
    }
    yaml_parser = serializer.get_parser("YAML")
    s = yaml_parser.dumps(d)
    m = yaml_parser.loads(s)
    print(s)
    print(m)


if __name__ == '__main__':
    main()
