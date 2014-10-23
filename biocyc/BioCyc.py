
from pprint import pprint
import re
import keyword

from parsing import load_dat_file, index_dat_file

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


class CycProtein(CycObject):
    def __init__(self, fields):
        super(CycProtein, self).__init__(fields)

    @property
    def is_complex(self):
        return 'COMPONENTS' in self.fields

    @property
    def components(self):
        if not self.is_complex:
            return None
        else:
            return [c.value for c in self.fields['COMPONENTS']]

    @property
    def genes(self):
        if self.is_complex:
            return None
        else:
            return [g.value for g in self.fields['GENE']]


class CycCompound(CycObject):
    pass


class CycReaction(CycObject):
    def __init__(self, fields):
        super(CycReaction, self).__init__(fields)
        self.ec_numbers = self.get_field('EC-NUMBER', [])
        self.left = self.get_field('LEFT', [])
        self.right = self.get_field('RIGHT', [])

    @property
    def direction(self):
        if 'REACTION-DIRECTION' in self.fields:
            return self.fields['REACTION-DIRECTION'].value
        else:
            return 'UNKNOWN'

    @property
    def reversible(self, unknown_is_reversible=True):
        if unknown_is_reversible:
            return self.direction == 'REVERSIBLE' or self.direction == 'UNKNOWN'
        else:
            return self.direction == 'REVERSIBLE'

    def __repr__(self):
        if self.direction == 'REVERSIBLE':
            dirstr = ' <-> '
        elif self.direction == 'LEFT-TO-RIGHT':
            dirstr = ' -> '
        elif self.direction == 'IRREVERSIBLE-LEFT-TO-RIGHT':
            dirstr = ' --> '
        elif self.direction == 'RIGHT-TO-LEFT':
            dirstr = ' <- '
        elif self.direction == 'IRREVERSIBLE-RIGHT-TO-LEFT':
            dirstr = ' <-- '
        elif self.direction == 'UNKNOWN':
            dirstr = ' <-?-> '
        else:
            dirstr = ' <?-' + self.direction + '-?> '

        if self.ec_numbers:
            ec = "   {" + " ".join(self.ec_numbers) + "}"
        else:
            ec = ""

        return (self.unique_id + ": " + " + ".join(self.left) + dirstr +
                " + ".join(self.right)) + ec

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


class CycReactionLink(CycObject):
    pass


class CycEnzRxn(CycObject):
    pass


class CycModel(object):
    def __init__(self, directory):
        self.directory = directory

        def fullname(filename):
            return directory + "/" + filename

        to_load = [("genes.dat", CycGene),
                   ("proteins.dat", CycProtein),
                   ("compounds.dat", CycCompound),
                   ("reactions.dat", CycReaction),
#                   ("reaction-links.dat", CycReactionLink),
                   ("enzrxns.dat", CycEnzRxn)]

        self.objects = {}

        for filename, constructor in to_load:
            self.objects.update(index_dat_file(fullname(filename), constructor))

    def find(self, value, field='UNIQUE-ID'):
        r = [v for (k, v) in self.objects.items()
                          if v.matches(value, field=field)]
        r.sort(key=lambda x: x.__class__.__name__)
        return r

    def query(self, tokens):
        flatten = lambda xlist: [i for x in xlist for i in x]
        results = [tokens[0]]
        traces = [tokens[0]]
        pairs = zip(tokens[1::2], tokens[2::2])
        for cmd, value in pairs:
            if cmd == 'm':
                for i in range(len(results)):
                    results[i] = self.find(results[i], field=value)
                    def tracer(r):
                        u = r.get_field('UNIQUE-ID')[0]
                        return traces[i] + " ?{v} -> {u}".format(v=value, u=u)
                    traces[i] = [tracer(r) for r in results[i]]
            elif cmd == 'g':
                for i in range(len(results)):
                    results[i] = results[i].get_field(value, default=[])
                    def tracer(r):
                        return traces[i] + " ." + value + " -> " + r
                    traces[i] = [tracer(r) for r in results[i]]
            results = flatten(results)
            traces = flatten(traces)
        return [x + ": " + str(y) for x, y in zip(traces, results)]


def load_tigr4():
    return CycModel("spne170187cyc")


def load_d39():
    return CycModel("spne373153cyc")


def load_19f():
    return CycModel("spne487213cyc")


# =================== interactive prompt ====================
def general_find(model, value):
    return model.find(value, field=None)


def specific_find(model, value, field):
    return model.find(value, field=field)


def run_query(model, *args):
    return model.query(args)


command_map = dict(f=general_find,
                   ff=specific_find,
                   e=lambda m, v: specific_find(m, 'EC-'+v, 'EC-NUMBER'),
                   q=run_query)

macros = dict(gpr='m REACTION g ENZYME m PRODUCT g ACCESSION-1'.split())


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

        if cmd.startswith('?'):
            uid = cmd[1:]
            for name, model in models.items():
                if uid in model.objects:
                    print "#", name
                    print "CycObject:", uid
                    pprint(model.objects[uid].fields)
            continue

        if cmd.startswith('$'):
            cmd = cmd[1:]
            stringifier = lambda x: x.cellscribe()
        else:
            stringifier = lambda x: ("   [" + x.__class__.__name__ +
                                     "]  " + str(x))

        if cmd.startswith('.'):
            # compile macro
            args += macros[cmd[1:]]
            cmd = 'q'

        if cmd not in command_map:
            print "<<< Error: invalid command '" + cmd + "'>>>"
            continue

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


