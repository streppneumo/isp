from CellScribe import *
from model.compartments import e
from model.metabolites import *
from model.genes import SP_1032, SP_1033, SP_1034, SP_1035, SP_1869, SP_1870, SP_1871, SP_1872, SP_0242, SP_0243


iron = Metabolite("iron", kegg="C14819")
iron_rxn = Reaction(name="iron_rxn",
                           reactants=e(iron) + h2o + atp,
                           products=iron + adp + phosphate,
                           pairs=[(e(iron), iron)])

GeneAssociation(iron_rxn, SP_1032 & SP_1033 & SP_1034 & SP_1035 or
                                              SP_1869 & SP_1870 & SP_1871 & SP_1872)

#iron vs ferrichrome? reaction states that it transfers ferrichrome

#Pit 2 is first & Pit 1 is second (PiuB,PiuC,PiuD,PiuA)
#SP_0241 pseudogene

#ritR regulates pit1

#regulation

#sp_0240
