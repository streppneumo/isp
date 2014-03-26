from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_1386, SP_1387, SP_1388, SP_1389, SP_1386, SP_1387, SP_1388, SP_1389, SP_1580

spermidine_rxn = Reaction(name="spermidine_rxn",
                          reactants=e(spermidine) + H20 + atp,
                          products=spermidine + adp + phosphate,
                          pairs=[(spermidine, putrescine), (atp, adp)],
                          minors=[atp, adp])

GeneAssociation(spermidine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)



putrescine_rxn = Reaction(name="putrescine_rxn",
                          reactants=e(putrescine) + H20 + atp,
                          products=glucose + adp + phosphate)

#kegg pathway states that glucose is the product.... but it should be putrescine right?

GeneAssociation(putrescine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)



cellobiose_rxn = Reaction(name="cellobiose_rxn",
                          reactants=e(cellobiose) + H20 + atp,
                          products=cellobiose + adp + phosphate)

chitobiose_rxn = Reaction(name="chitobiose_rxn",
                          reactants=e(chitobiose) + H20 + adp,
                          products=chitobiose + adp + phosphate)

GeneAssociation(cellobiose_rxn or chitobiose_rxn, SP_1580)



mannitol_rxn = Reaction(name="mannitol_rxn",
                        reactants=e(mannitol) + H20 + atp,
                        products=mannitol + adp + phosphate)

GeneAssociation(mannitol_rxn, SP_1580)

sucrose = Reaction(name="sucrose",
                      reactants=e(sucrose) + H20 + atp,
                      products=sucrose + adp + phosphate)

SP_1580 = Gene("SP_1580")
sucrose_GA = GeneAssociation(sucrose, SP_1580)

#sucrose, cellobiose, and chitobiose share the same 1 gene... how to approach this?