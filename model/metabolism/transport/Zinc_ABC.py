from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_2169, SP_2170, SP_2171


zinc_rxn = Reaction(name="zinc_rxn",
                    reactants=e(zinc) + H20 + atp,
                    products=zinc + adp + phosphate,
                    pairs=[(atp, adp)],
                    minors=[atp, adp])

GeneAssociation(zinc_rxn, SP_2169 & SP_2170 & SP_2171)