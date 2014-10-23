from CellScribe import *

from compartments import e
from metabolites import *
from genes import SP_0452, SP_0453, SP_1034, SP_1035, SP_0609, SP_0607, SP_0608, SP_0610, SP_0749, \
    SP_0750, SP_0751, SP_0752, SP_0753, SP_1396, SP_1397, SP_1398, SP_1399, SP_1400

l_lysine_rxn = Reaction(name="l_lysine_rxn",
                        reactants=e(l_lysine) + h2o + atp,
                        products=l_lysine + adp + phosphate,
                        pairs=[(atp, adp)],
                        minors=[atp, adp])

GeneAssociation(l_lysine_rxn, SP_0452 & SP_0453)


l_glutamate_rxn = Reaction(name="l-glutamate_rxn",
                           reactants=e(l_glutamate) + h2o + atp,
                           products=l_glutamate + adp + phosphate)

GeneAssociation(l_glutamate_rxn, SP_0609 & SP_0607 & SP_0608 & SP_0610)

l_valine_rxn = Reaction(name="l_valine_rxn",
                        reactants=e(l_valine) + h2o + atp,
                        products=l_valine + adp + phosphate,
                        pairs=[(e(l_valine), l_valine)])

GeneAssociation(l_valine_rxn, SP_0749 & SP_0750 & SP_0751 & SP_0752 & SP_0753)


phosphate_rxn = Reaction(name="phosphate_rxn",
                         reactants=e(diphosphate) + h2o,
                         products=phosphate)

GeneAssociation(phosphate_rxn, SP_1396 & SP_1397 & SP_1398 & SP_1399 & SP_1400)