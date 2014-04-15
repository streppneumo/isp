
class Reactable(object):
    # this is an Abstract Base Class

    def __mul__(self, other):
        return StoichiometricPair(species=self, coefficient=other)

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
    def __init__(self, species, coefficient=1):
        self.species = species
        self.coefficient = coefficient

    def __mul__(self, other):
        return StoichiometricPair(species=self.species,
                                  coefficient=other*self.coefficient)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return "({c},{m})".format(c=str(self.coefficient), m=str(self.species))

    @property
    def tuple(self):
        return self.coefficient, self.species


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

