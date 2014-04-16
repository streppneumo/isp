
from logic import *
from location import *
from foundation import *


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


