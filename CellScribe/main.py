
from logic import *
from location import *


class Gene(Logicable):
    def __init__(self, name, **kwargs):
        self.name = name
        self.fields = kwargs

    def __str__(self):
        return self.name


class Pseudogene(Gene):
    pass


class Association(object):
    # this is an Abstract Base Class
    pass


class GeneAssociation(Association):
    def __init__(self, reaction, rule):
        self.reaction = reaction
        self.name = reaction.name
        self.rule = rule

    def __str__(self):
        return "{rxn} <-> {rule}".format(rxn=self.name, rule=self.rule)


class Reactable(object):
    # this is an Abstract Base Class

    def __mul__(self, other):
        return StoichiometricPair(metabolite=self, coefficient=other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        return ReactableSet(1*self, 1*other)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return self.name

    @property
    def tuple(self):
        return (1*self).tuple

    @property
    def tupleset(self):
        return [self.tuple]


class StoichiometricPair(Reactable):
    def __init__(self, metabolite, coefficient=1):
        self.metabolite = metabolite
        self.coefficient = coefficient

    def __mul__(self, other):
        return StoichiometricPair(metabolite=self.metabolite, coefficient=other*self.coefficient)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return "({c},{m})".format(c=str(self.coefficient), m=str(self.metabolite))

    @property
    def tuple(self):
        return self.coefficient, self.metabolite


class ReactableSet(Reactable):
    def __init__(self, a, b):
        self.reactables = [a, b]

    def __add__(self, other):
        return self.append(other)

    def __radd__(self, other):
        return self.__add__(other)

    def append(self, a):
        if isinstance(a, ReactableSet):
            self.reactables += a
        else:
            self.reactables.append(1*a)
        return self

    def __str__(self):
        return "{" + (";".join([str(r) for r in self.reactables])) + "}"

    @property
    def tuple(self):
        return [r.tuple for r in self.reactables]

    @property
    def tupleset(self):
        return self.tuple


class LocalizedMetabolite(Reactable):
    def __init__(self, metabolite, location):
        self.metabolite = metabolite
        self.location = location

    def __str__(self):
        return str(self.metabolite) + self.location.suffix


class Location(object):
    def __init__(self, name, abbreviation=None):
        self.name = name
        self.abbreviation = abbreviation

    def __str__(self):
        if self.abbreviation:
            return "{name}[{abbrev}]".format(name=self.name, abbrev=self.abbreviation)
        else:
            return self.name

    @property
    def suffix(self):
        if self.abbreviation:
            return "[" + self.abbreviation + "]"
        else:
            return "[" + self.name + "]"

    @property
    def localizer(self):
        return lambda m: LocalizedMetabolite(m, self)


class RNA(Reactable):
    def __init__(self, name, **kwargs):
        self.name = name
        self.fields = kwargs

    def __str__(self):
        return self.name


class Metabolite(Reactable):
    default_location = None

    def __init__(self, name, **kwargs):
        self.name = name
        self.fields = kwargs

    @property
    def localized(self):
        return LocalizedMetabolite(self, Metabolite.default_location)

    def __str__(self):
        return self.name


class Reaction(object):
    def __init__(self, name, reactants, products, minors=None, pairs=None, reversible=None, **kwargs):
        self.name = name
        self.reactants = reactants.tupleset
        self.products = products.tupleset
        self.minors = minors
        self.pairs = pairs
        self.reversible = reversible
        self.fields = kwargs

    def __str__(self):
        def to_str(tupleset):
            def aux(pair):
                if pair[0] == 1:
                    return str(pair[1])
                else:
                    return str(pair[0]) + " " + str(pair[1])

            return " + ".join([aux(x) for x in tupleset])

        return self.name + ":  " + to_str(self.reactants) + " <=> " + to_str(self.products)


class Operon(object):
    def __init__(self, name, genes, **kwargs):
        self.name = name
        self.genes = genes
        self.fields = kwargs


class MinorSuggestion(object):
    def __init__(self, minor):
        self.minor = minor


def MinorSuggestions(*args):
    return [MinorSuggestion(arg) for arg in args]


class PairSet(object):
    def __init__(self, *args):
        self.members = set(args)



class Model(object):
    def __init__(self, name):
        self.name = name
        self.objects = {}
        self.associations = {}

    def add(self, obj):
        if isinstance(obj, Association):
            self.associations[obj.name] = obj
        else:
            self.objects[obj.name] = obj

    def __str__(self):
        pass






if __name__ == '__main__':
    m1 = Metabolite("m1")
    m2 = Metabolite("m2")

    eloc = Location("Extracellular", 'e')
    cloc = Location("Cytoplasm", 'c')
    Metabolite.default_location = cloc
    e = eloc.localizer
    #print m1.localized
    #print e(m1)

    #r1 = Logicable("r1")
    #r2 = Logicable("r2")

    #print r1
    #print r1 | ~(r2 & ~r1)


