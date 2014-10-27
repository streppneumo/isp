from CellScribe import *

from ...common import *


l_lysine_rxn = Reaction(name="l_lysine_rxn",
                        reactants=e(l_lysine) + H2O + ATP,
                        products=l_lysine + ADP + phosphate,
                        pairs=[(ATP, ADP)],
                        minors=[ATP, ADP])

GeneAssociation(l_lysine_rxn, SP_0452 & SP_0453)


l_glutamate_rxn = Reaction(name="l-glutamate_rxn",
                           reactants=e(l_glutamate) + H2O + ATP,
                           products=l_glutamate + ADP + phosphate)

GeneAssociation(l_glutamate_rxn, SP_0609 & SP_0607 & SP_0608 & SP_0610)

l_valine_rxn = Reaction(name="l_valine_rxn",
                        reactants=e(l_valine) + H2O + ATP,
                        products=l_valine + ADP + phosphate,
                        pairs=[(e(l_valine), l_valine)])

GeneAssociation(l_valine_rxn, SP_0749 & SP_0750 & SP_0751 & SP_0752 & SP_0753)


phosphate_rxn = Reaction(name="phosphate_rxn",
                         reactants=e(diphosphate) + H2O,
                         products=phosphate)

GeneAssociation(phosphate_rxn, SP_1396 & SP_1397 & SP_1398 & SP_1399 & SP_1400)