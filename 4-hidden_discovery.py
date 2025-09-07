#!/usr/bin/python3
"""4-hidden_discovery.py"""

import marshal
import types

def extract_names(code):
    names = set()
    if isinstance(code, types.CodeType):
        names.update(code.co_names)
        for const in code.co_consts:
            names.update(extract_names(const))
    return names

if __name__ == "__main__":
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # skip pyc header
        code_obj = marshal.load(f)
    names = [name for name in extract_names(code_obj) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
