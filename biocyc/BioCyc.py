
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
        if 'UNIQUE-ID' in fields:
            self.unique_id = fields['UNIQUE-ID'].value


class CycGene(CycObject):
    def __init__(self, fields):
        super(CycGene, self).__init__(fields)
        self.common_name = fields['COMMON-NAME'].value
        accs = [v for k, v in fields.items() if k.startswith('ACCESSION-')]
        self.names = set([a.value for a in accs] + [self.common_name])


class CycCompound(CycObject):
    pass


class CycReaction(CycObject):
    def __init__(self, fields):
        super(CycReaction, self).__init__(fields)
        if 'EC-NUMBER' in fields:
            self.ec_numbers = fields['EC-NUMBER'].values
        else:
            self.ec_numbers = []
        if 'LEFT' in fields:
            self.left = fields['LEFT'].values
        else:
            self.left = []
        if 'RIGHT' in fields:
            self.right = fields['RIGHT'].values
        else:
            self.right = []

    def __repr__(self):
        return " + ".join(self.left) + " <-> " + " + ".join(self.right)


class CycModel(object):
    def __init__(self, directory):
        self.directory = directory

        def fullname(filename):
            return directory + "/" + filename

        self.genes = load_genes_dat(fullname("genes.dat"))
        self.compounds = load_compounds_dat(fullname("compounds.dat"))
        self.reactions = load_reactions_dat(fullname("reactions.dat"))

    def get_reactions_by_ec(self, ec):
        return [r for r in self.reactions.values() if ec in r.ec_numbers]


def load_tigr4():
    return CycModel("spne170187cyc")


def load_d39():
    return CycModel("spne373153cyc")


def load_19f():
    return CycModel("spne487213cyc")


# =================== file parsing primitives ====================
def load_genes_dat(filename):
    genes = [CycGene(fields) for fields in load_dat_file(filename)]
    return {g.unique_id: g for g in genes}


def load_compounds_dat(filename):
    compounds = [CycCompound(fields) for fields in load_dat_file(filename)]
    return {c.unique_id: c for c in compounds}


def load_reactions_dat(filename):
    reactions = [CycReaction(fields) for fields in load_dat_file(filename)]
    return {r.unique_id: r for r in reactions}


if __name__ == '__main__':
    pass
    #genes = load_genes_dat("spne170187cyc/genes.dat")
    #compounds = load_compounds_dat("spne170187cyc/compounds.dat")
    #reactions = load_reactions_dat("spne170187cyc/reactions.dat")
    #pprint(reactions)

    #pprint([x.__dict__ for x in load_compounds_dat("spne170187cyc/compounds.dat")[0:3]])
    #rxns = load_reactions_dat("spne170187cyc/reactions.dat")
    #pprint([x.__dict__ for x in rxns[0:3]])
    #print rxns[2].right[1].attributes['COEFFICIENT'].value
    # common = dict()
    # genes = load_genes_dat("spne170187cyc/genes.dat")
    # for gene in genes:
    #     if "accession_1" in gene.__dict__:
    #         common[gene.common_name.value] = gene.accession_1.value
    #     else:
    #         common[gene.common_name.value] = gene.common_name.value
    # with open("names.txt") as f:
    #     with open("equiv.txt", "w") as out:
    #         for line in f.readlines():
    #             out.write(common[line.rstrip()] + "\n")
    #             #f.write(gene.common_name.value + "\t" + gene.accession_1.value + "\n")

    dats = load_dat_file("spne487213cyc/reactions.dat")

    models = dict()
    models["tigr4"] = load_tigr4()
    models["19f"] = load_19f()
    models["d39"] = load_d39()

    def query_ecs(ec):
        for name, model in models.items():
            print name
            for r in model.get_reactions_by_ec("EC-" + ec):
                print "  ", r

    input = "not none"
    while input.rstrip() != "none":
        input = raw_input("EC number: ").rstrip()
        query_ecs(input)


