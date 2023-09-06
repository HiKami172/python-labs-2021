import argparse

from app.dump import dump


def main():
    parser = argparse.ArgumentParser(
        prog='Serializer',
        description='Serialized file conversion (JSON/YAML)')
    parser.add_argument("in_file", type=str, help="Input file for pars")
    parser.add_argument("out_file", type=str, help="Output file to load")
    args = parser.parse_args()

    dump(args.in_file, args.out_file)

# if __name__ == "__main__":
#    main()
