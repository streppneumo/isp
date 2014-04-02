from CellScribe import *
from model.compartments import e
from model.metabolites import *
from model.genes import SP_2169, SP_2170, SP_2171, SP_1648, SP_1649, SP_1650, SP_1858, SP_1858, SP_1552


zinc_rxn = Reaction(name="zinc_rxn",
                    reactants=e(zinc) + H20 + atp,
                    products=zinc + adp + phosphate,
                    pairs=[(e(zinc), zinc)])

GeneAssociation(zinc_rxn, SP_2169 & SP_2170 & SP_2171)

manganese_rxn = Reaction(name="manganese_rxn",
                       reactants=e(manganese) + atp,
                       products=manganese + adp + phosphate,
                       pairs=[(e(manganese), manganese)])

GeneAssociation(manganese_rxn, SP_1648 & SP_1649 & SP_1650)

#regulation

#SczA = Gene("SP_1858")
#czcD = Gene("SP_1857")

If(SczA, ~czcD)
If (zinc, ~SczA)

#PsaR = Gene("SP_1638")
#psaBCA  genes SP_1650, SP_1649, SP_1648
#mntE = Gene(Sp_1552)   cation efflux system


If(PsaR & (zinc | manganese), ~psaBCA)

# if there is manganese, it will bind to PsaR, which will repress transcription of psaBCA



