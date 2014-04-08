from CellScribe import *
from model.compartments import e
from model.metabolites import *
from model.genes import SP_2169, SP_2170, SP_2171, SP_1858, SP_1857


zinc_rxn = Reaction(name="zinc_rxn",
                    reactants=e(zinc) + H20 + atp,
                    products=zinc + adp + phosphate,
                    pairs=[(e(zinc), zinc)])

GeneAssociation(zinc_rxn, SP_2169 & SP_2170 & SP_2171)

#regulation

SczA = Gene("SP_1858")
czcD = Gene("SP_1857")

If(SczA, ~czcD)
If(Zn, ~SczA)

