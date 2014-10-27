
from pprint import pprint

from logic import *
from location import *
from foundation import *


def get_all(objs):
    allobjs = []
    for obj in objs:
        allobjs.append(obj)
        if isinstance(obj, Composite):
            allobjs += obj.primitives
    return set(allobjs)


def group_by_class(objs):
    classes = set([x.__class__.__name__ for x in objs])
    groups = {}
    for cls in classes:
        groups[cls] = [x for x in objs if x.__class__.__name__ == cls]
    return groups


class Model(object):
    def __init__(self, name):
        self.name = name
        self.objects = {}

    def add(self, obj):
        if "name" not in obj.__dict__:
            self.objects[repr(obj)] = obj
        else:
            self.objects[obj.name] = obj

    def __str__(self):
        pass

    def show(self):
        pprint(self.objects)

    def summary(self, showall=False):
        groups = group_by_class(get_all(self.objects.values()))
        print "\nSummary for model '" + self.name + "'\n"
        print "Object Summary:"
        for cls, objs in groups.items():
            print "  ", len(objs), cls
        print ""
        if showall:
            print "Objects:"
            for cls, objs in groups.items():
                print "   " + cls + ":"
                for obj in objs:
                    print "      " + str(obj)


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


