
from copy import deepcopy
from pprint import pprint
from warnings import warn


class RegistryError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Object {name} already exists in registry.".format(name=self.name)


class RegistryWarning(Warning):
    pass


class Registry(object):
    def __init__(self):
        self.objects = {}
        self.annotations = {}
        self.properties = {}

    def set_property(self, **kwargs):
        self.properties.update(**kwargs)

    def register(self, obj):
        key = repr(obj)
        if key in self.objects:
            #raise RegistryError(key)
            warn(str(RegistryError(key)), RegistryWarning)
        else:
            self.objects[key] = obj
            self.annotations[key] = deepcopy(self.properties)

    def show(self):
        objs = deepcopy(self.objects)
        for key in objs:
            if self.annotations[key]:
                objs[key] = dict(object=objs[key],
                                 annotations=self.annotations[key])
        pprint(objs)


class Registered(object):
    registry = Registry()

    def register(self):
        self.__class__.registry.register(self)


if __name__ == '__main__':
    class Met(Registered):
        def __init__(self, name):
            self.name = name
            self.register()

    Met("m1")
    Registered.registry.set_property(here="there")
    Met("m1")

    Registered.registry.show()