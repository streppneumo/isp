
from abc import ABCMeta, abstractproperty


class Named(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Named):
            return self.name == other.name
        else:
            return False

    def __repr__(self):
        return self.__class__.__name__ + "(" + self.name + ")"


class Primitive(Named):
    def __contains__(self, item):
        return self == item


class Composite(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def members(self):
        pass

    @property
    def primitives(self):
        prims = []
        for member in self.members:
            if isinstance(member, Composite):
                prims += member.primitives
            else:
                prims.append(member)
        return prims

    # no setter; primitives should be quasi-immutable

    def __contains__(self, item):
        return item in self.primitives


if __name__ == "__main__":
    class Metabolite(Primitive):
        pass

    m1 = Metabolite("met1")
    m2 = Metabolite("met2")
    m3 = Metabolite("met3")
    #c = Composite([m1, m2])
    #print m1 in c
    #print m3 in c
    #Named("hello")

