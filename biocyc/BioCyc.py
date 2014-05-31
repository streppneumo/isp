
from pprint import pprint
import re
import keyword

from parsing import load_dat_file


def is_unsafe_name(s):
    try:
        eval(s + " = 1")
    except:
        return False
    return True


def to_safe_name(s, prefix='x'):
    s = s.replace(' ', '_')
    s = s.replace('-', '_')
    for ch in '!@#$%^&*()`~"\'[]{};:<>,.?/+=|':
        s = s.replace(ch, '')
    if not s[0].isalpha() or keyword.iskeyword(s):
        s = prefix + s
    if is_unsafe_name(s):
        raise Exception("UNSAFE NAME '{name}'".format(name=s))
    else:
        return s.lower()


class CycObject(object):
    def __init__(self, fields):
        safe_fields = dict([(to_safe_name(k), v) for k, v in fields.items()])
        self.__dict__.update(safe_fields)
        self.fields = fields


class CycGene(CycObject):
    pass


class CycCompound(CycObject):
    pass


class CycReaction(CycObject):
    pass


# =================== file parsing primitives ====================
def load_genes_dat(filename):
    return [CycGene(fields) for fields in load_dat_file(filename)]


def load_compounds_dat(filename):
    return [CycCompound(fields) for fields in load_dat_file(filename)]


def load_reactions_dat(filename):
    return [CycReaction(fields) for fields in load_dat_file(filename)]


if __name__ == '__main__':
    #pprint([x.__dict__ for x in load_genes_dat("spne170187cyc/genes.dat")[0:3]])
    #pprint([x.__dict__ for x in load_compounds_dat("spne170187cyc/compounds.dat")[0:3]])
    rxns = load_reactions_dat("spne170187cyc/reactions.dat")
    pprint([x.__dict__ for x in rxns[0:3]])
    print rxns[2].right[1].attributes['COEFFICIENT'].value