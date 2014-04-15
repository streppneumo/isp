
from abc import ABCMeta, abstractproperty

from foundation import Composite
from registry import Registered


class Association(Composite):
    __metaclass__ = ABCMeta

    @abstractproperty
    def members(self):
        pass


class GeneAssociation(Association, Registered):
    def __init__(self, reaction, rule):
        super(GeneAssociation, self).__init__(self)
        self.reaction = reaction
        self.rule = rule

    @property
    def members(self):
        return self.reaction.members + self.rule.members

    def __str__(self):
        #return "{rxn} <-> {rule}".format(rxn=self.name, rule=self.rule)
        pass