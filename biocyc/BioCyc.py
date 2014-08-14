
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


def flatten(lists):
    return reduce(lambda x, y: x+y, lists)


class CycObject(object):
    def __init__(self, fields):
        safe_fields = dict([(to_safe_name(k), v) for k, v in fields.items()])
        self.__dict__.update(safe_fields)
        self.fields = fields
        if 'UNIQUE-ID' in fields:
            self.unique_id = fields['UNIQUE-ID'].value

    def get_field(self, field, default=None):
        if field in self.fields:
            return self.fields[field].values
        else:
            return default

    def matches(self, value, field='UNIQUE-ID'):
        if field is None:
            for v in self.fields.values():
                if v.matches(value):
                    return True
            return False
        else:
            if field in self.fields:
                return self.fields[field].matches(value)

    def __str__(self):
        return self.unique_id

    def __repr__(self):
        return str(self)

    def cellscribe(self):
        return '# ' + str(self)


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
        self.ec_numbers = self.get_field('EC-NUMBER', [])
        self.left = self.get_field('LEFT', [])
        self.right = self.get_field('RIGHT', [])

    def __repr__(self):
        return (self.unique_id + ": " + " + ".join(self.left) + " <-> " +
                " + ".join(self.right))

    def __str__(self):
        return repr(self)

    def cellscribe(self):
        var = to_safe_name(self.unique_id)
        reacts = ", ".join([to_safe_name(x) for x in self.left])
        prods = ", ".join([to_safe_name(x) for x in self.right])
        space = " " * (len(var) + 12)
        return ('{var} = Reaction("{var}",\n' +
                space + 'reactants=[{reacts}],\n' +
                space + 'products=[{prods}])\n'
                ).format(var=var, reacts=reacts, prods=prods)


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

    @staticmethod
    def find(mapping, value, field='UNIQUE-ID'):
        return [v for (k, v) in mapping.items()
                             if v.matches(value, field=field)]

    def findall(self, value, collapse=True, field=None):
        matches = dict(genes=self.find(self.genes, value, field),
                       compounds=[],
                       reactions=self.find(self.reactions, value, field))
        if collapse:
            return flatten(matches.values())
        else:
            return matches


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


# =================== interactive prompt ====================
def general_find(model, value):
    return model.findall(value, field=None)


def specific_find(model, value, field):
    return model.findall(value, field=field)


command_map = dict(f=general_find,
                   ff=specific_find,
                   e=lambda m, v: specific_find(m, 'EC-'+v, 'EC-NUMBER'))


def start_interactive(models):
    input = "not x"
    previous_args = []
    while input.rstrip() != "x":
        input = raw_input("> ").rstrip()
        inputs = input.split()
        cmd = inputs[0]
        args = inputs[1:]

        if len(args) == 1 and args[0] == '^':
            args = previous_args[-1]
            print ">", cmd, " ".join(args)
        else:
            previous_args.append(args)

        if cmd.startswith('$'):
            cmd = cmd[1:]
            stringifier = lambda x: x.cellscribe()
        else:
            stringifier = lambda x: "   " + str(x)

        for name, model in models.items():
            print "#", name
            for v in command_map[cmd](model, *args):
                print stringifier(v)




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

    #dats = load_dat_file("spne487213cyc/reactions.dat")

    models = dict()
    models["tigr4"] = load_tigr4()
    models["19f"] = load_19f()
    models["d39"] = load_d39()

    #tigr4 = load_tigr4()
    #r = tigr4.findall('EC-2.7.1.2')

    start_interactive(models)


