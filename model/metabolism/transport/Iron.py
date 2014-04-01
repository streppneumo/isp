from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_1032, SP_1033, SP_1034, SP_1035, SP_1869, SP_1870, SP_1871, SP_1872, SP_0241, SP_0242, SP_0243



iron = Metabolite("iron", kegg="C14819")
iron_rxn = Reaction(name="iron_rxn",
                           reactants=e(iron) + H20 + atp,
                           products=iron + adp + phosphate,
                           Reversible=true,
                           pairs=[(e(iron), iron)])


GeneAssociation(iron_rxn, SP_1032 & SP_1033 & SP_1034 & SP_1035 or SP_1869 & SP_1870 & SP_1871 & SP_1872
or SP_0241 & SP_0242 & SP_0243)


#Pit 2 is first & Pit 1 is second & Pit is last
#SP_0241 isn't in genome spreadsheet

#regulation

