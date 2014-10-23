
from pprint import pformat


class Verbatim(object):
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        if isinstance(self.obj, list):
            return "[" + ", ".join(self.obj) + "]"
        else:
            return self.obj


def vformat(obj):
    if isinstance(obj, Verbatim):
        return str(obj)
    else:
        return pformat(obj)


def stringify_declaration(decname, args, kwargs, varname=None):
    s = ""
    nind = 0
    if varname is not None:
        nind += len(varname) + 3
        s += varname + " = "
    nind += len(decname) + 1
    s += decname + '('
    indent = " " * nind
    first = True
    for arg in args:
        if first:
            first = False
        else:
            s += ",\n" + indent
        s += vformat(arg)
    for name, value in kwargs:
        if first:
            first = False
        else:
            s += ",\n" + indent
        s += name + '=' + vformat(value)
    s += ')'
    return s


if __name__ == '__main__':
    print stringify_declaration('Reaction', ['rxn1'], [('pairs', Verbatim(['SP_0001', 'SP_0002']))])


