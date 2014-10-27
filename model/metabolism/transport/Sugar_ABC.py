from CellScribe import *

from ...common import *


spermidine_rxn = Reaction(name="spermidine_rxn",
                          reactants=e(spermidine) + H2O + ATP,
                          products=spermidine + ADP + phosphate)
GeneAssociation(spermidine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)


putrescine_rxn = Reaction(name="putrescine_rxn",
                          reactants=e(putrescine) + H2O + ATP,
                          products=putrescine + ADP + phosphate)
GeneAssociation(putrescine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)

cellobiose_rxn = Reaction(name="cellobiose_rxn",
                          reactants=e(cellobiose) + H2O + ATP,
                          products=cellobiose + ADP + phosphate)
GeneAssociation(cellobiose_rxn, SP_1580)

chitobiose_rxn = Reaction(name="chitobiose_rxn",
                          reactants=e(chitobiose) + H2O + ATP,
                          products=chitobiose + ADP + phosphate)
GeneAssociation(chitobiose_rxn, SP_1580)


mannitol_rxn = Reaction(name="mannitol_rxn",
                        reactants=e(mannitol) + H2O + ATP,
                        products=mannitol + ADP + phosphate)
GeneAssociation(mannitol_rxn, SP_1580)

sucrose_rxn = Reaction(name="sucrose_rxn",
                      reactants=e(sucrose) + H2O + ATP,
                      products=sucrose + ADP + phosphate)
GeneAssociation(sucrose_rxn, SP_1580)

