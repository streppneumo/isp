from CellScribe import *

from ...common import *

choline_rxn = Reaction(name="choline_rxn",
                       reactants=e(choline) + ATP,
                       products=choline + ADP + phosphate)

GeneAssociation(choline_rxn, SP_1860 & SP_1861)


