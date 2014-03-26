from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_1032, SP_1033, SP_1034, SP_1035


atp = Metabolite("atp")
adp = Metabolite("adp")
phosphate = Metabolite("phosphate")
H20 = Metabolite("H20",kegg="C00001")
ferrichrome = Metabolite("ferrichrome", kegg="C06228")

#iron vs ferrichrome? reaction states that it transfers ferrichrome

ferrichrome_rxn = Reaction(name="ferrichrome_rxn",
                           reactants=e(ferrichrome) + H20 + atp,
                           products=ferrichrome + adp + phosphate,
                           pairs=[(atp, adp)],
                           minors=[atp, adp])


GeneAssociation(ferrichrome_rxn, SP_1032 & SP_1033 & SP_1034 & SP_1035 or
                                              SP_1869 & SP_1870 & SP_1871 & SP_1872)

#Pit 2 is first line & Pit 1 is second line