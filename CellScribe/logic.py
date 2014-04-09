
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


class Not(Logicable):
    def __init__(self, expr):
        self.expression = expr

    def __str__(self):
        return "Not[{e}]".format(e=str(self.expression))


class Junction(Logicable):
    def __init__(self, left, right, operator=None):
        self.left = left
        self.right = right
        self.operator = operator

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


