from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_2169, SP_2170, SP_2171, SP_1648, SP_1649, SP_1650, SP_1858, SP_1858


zinc_rxn = Reaction(name="zinc_rxn",
                    reactants=e(zinc) + H20 + atp,
                    products=zinc + adp + phosphate,
                    reversible=True,
                    pairs=[(e(zinc), zinc)])

GeneAssociation(zinc_rxn, SP_2169 & SP_2170 & SP_2171)

manganese_rxn = Reaction(name="manganese_rxn",
                       reactants=e(manganese) + atp,
                       products=manganese + adp + phosphate,
                       reversible=True,
                       pairs=[(e(manganese), manganese)])

GeneAssociation(manganese_rxn, SP_1648 & SP_1649 & SP_1650)

#regulation

#SczA = Gene("SP_1858")
#czcD = Gene("SP_1857")

If(SczA, ~czcD)
If (Zn2+, ~SczA)

#PsaR = Gene("SP_1638)

If(PsaR,~psaBCA)
If(Zn2+, ~psaBCA)



