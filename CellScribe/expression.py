
from foundation import Primitive, Composite, Named
from logic import Logicable
#from location import Localizable
from stoichiometry import Reactable


class Gene(Primitive, Logicable):
    def __init__(self, name, **kwargs):
        Primitive.__init__(self, name)
        self.fields = kwargs


class Pseudogene(Gene):
    pass


class RNA(Primitive, Reactable):
    def __init__(self, name, **kwargs):
        Primitive.__init__(self, name)
        self.fields = kwargs


class Protein(Primitive, Reactable, Logicable):
    def __init__(self, name, **kwargs):
        Primitive.__init__(self, name)
        self.fields = kwargs


class Complex(Composite, Named, Reactable, Logicable):
    def __init__(self, name, subunits, **kwargs):
        Named.__init__(self, name)
        self.subunits = subunits
        self.fields = kwargs

    @property
    def members(self):
        return self.subunits


class Operon(Composite, Named):
    def __init__(self, name, genes, **kwargs):
        Named.__init__(self, name)
        self.genes = genes
        self.fields = kwargs

    @property
    def members(self):
        return self.genes
