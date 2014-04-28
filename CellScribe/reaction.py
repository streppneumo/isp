
from stoichiometry import Reactable
from foundation import Primitive, Composite, Named
from location import Localizable, Localized
from logic import Logicable


class Metabolite(Primitive, Reactable, Localizable, Logicable):
    default_location = None
    localized_constructor = None  # deferred to LocalizedMetabolite

    def __init__(self, name, **kwargs):
        Primitive.__init__(self, name)
        self.fields = kwargs


class LocalizedMetabolite(Localized, Metabolite):
    pass


Metabolite.localized_constructor = LocalizedMetabolite


class Reaction(Named, Composite):
    def __init__(self, name, reactants, products, minors=None, pairs=None,
                 reversible=None, **kwargs):
        Named.__init__(self, name)
        self.name = name
        self.reactants = reactants.tupleset
        self.products = products.tupleset
        self.minors = minors
        self.pairs = pairs
        self.reversible = reversible
        self.fields = kwargs

    @property
    def members(self):
        def snds(l):
            return [x[1] for x in l]
        return snds(self.reactants) + snds(self.products)

    def __str__(self):
        def to_str(tupleset):
            def aux(pair):
                if pair[0] == 1:
                    return str(pair[1])
                else:
                    return str(pair[0]) + " " + str(pair[1])

            return " + ".join([aux(x) for x in tupleset])

        return (self.name + ":  " + to_str(self.reactants) + " <=> "
                + to_str(self.products))


class MinorSuggestion(object):
    def __init__(self, minor):
        self.minor = minor


def MinorSuggestions(*args):
    return [MinorSuggestion(arg) for arg in args]


class PairSet(object):
    def __init__(self, *args):
        self.members = set(args)

