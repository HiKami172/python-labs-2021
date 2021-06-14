#!/usr/bin/env python

from lib.factory import serializer

types = {
    "json": serializer.get_parser("json"),
    "yaml": serializer.get_parser("yaml")
}


def dump(in_file, out_file):
    ifile = open(in_file, "r")
    ofile = open(out_file, "w")
    obj = types[in_file.split(".")[-1].lower()].unpack(ifile)
    types[out_file.split(".")[-1].lower()].pack(obj, ofile)
    ifile.close()
    ofile.close()
