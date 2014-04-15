
from foundation import Composite
from registry import Registered


class Logicable(object):
    # this is an Abstract Base Class

    def __and__(self, other):
        return And(self, other)

    def __rand__(self, other):
        return self.__and__(other)

    def __or__(self, other):
        return Or(self, other)

    def __ror__(self, other):
        return self.__or__(other)

    def __invert__(self):
        return Not(self)

    def __str__(self):
        return self.name


class Not(Logicable, Composite):
    def __init__(self, expr):
        self.expression = expr

    def __str__(self):
        return "Not[{e}]".format(e=str(self.expression))

    @property
    def members(self):
        return [self.expression]


class Junction(Logicable, Composite):
    def __init__(self, left, right, operator=None):
        self.left = left
        self.right = right
        self.operator = operator

    @property
    def members(self):
        return [self.left, self.right]

    def __str__(self):
        return "{op}[{left}, {right}]".format(op=self.operator,
                                              left=str(self.left),
                                              right=str(self.right))


class Or(Junction):
    def __init__(self, left, right):
        Junction.__init__(self, left, right, operator="Or")


class And(Junction):
    def __init__(self, left, right):
        Junction.__init__(self, left, right, operator="And")


class Implication(Composite, Registered):
    def __init__(self, subject, predicate):
        self.subject = subject
        self.predicate = predicate
        self.register()

    @property
    def members(self):
        return self.subject.members + self.predicate.members


class If(Implication):
    pass


class Iff(Implication):
    pass
