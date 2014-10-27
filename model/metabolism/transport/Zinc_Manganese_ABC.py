from CellScribe import *

from ...common import *

zinc_rxn = Reaction(name="zinc_rxn",
                    reactants=e(zinc) + H2O + ATP,
                    products=zinc + ADP + phosphate,
                    pairs=[(e(zinc), zinc)])
GeneAssociation(zinc_rxn, SP_2169 & SP_2170 & SP_2171)

manganese_rxn = Reaction(name="manganese_rxn",
                         reactants=e(manganese) + ATP,
                         products=manganese + ADP + phosphate,
                         pairs=[(e(manganese), manganese)])
GeneAssociation(manganese_rxn, SP_1648 & SP_1649 & SP_1650)

If(sczA, ~czcD)
If(zinc, ~sczA)
If(psaR & (zinc | manganese), ~psaBCA)

#mntE = Gene(Sp_1552)   cation efflux system

