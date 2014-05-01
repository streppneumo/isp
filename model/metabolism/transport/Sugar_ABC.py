from CellScribe import *
from model.compartments import e
from model.metabolites import *
from model.genes import SP_1386, SP_1387, SP_1388, SP_1389, SP_1386, SP_1387, SP_1388, SP_1389, SP_1580

spermidine = Metabolite("spermidine", kegg="C00315")
putrescine = Metabolite("putrescine", kegg="C00134")
spermidine_rxn = Reaction(name="spermidine_rxn",
                          reactants=e(spermidine) + h2o + atp,
                          products=spermidine + adp + phosphate,
                          pairs=[(spermidine, putrescine), (atp, adp)],
                          minors=[atp, adp])

GeneAssociation(spermidine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)


putrescine_rxn = Reaction(name="putrescine_rxn",
                          reactants=e(putrescine) + h2o + atp,
                          products=putrescine + adp + phosphate)

GeneAssociation(putrescine_rxn, SP_1386 & SP_1387 & SP_1388 & SP_1389)

cellobiose = Metabolite("cellobiose", kegg="C00185")
cellobiose_rxn = Reaction(name="cellobiose_rxn",
                          reactants=e(cellobiose) + h2o + atp,
                          products=cellobiose + adp + phosphate)

chitobiose = Metabolite("chitobiose", kegg="C01674")
chitobiose_rxn = Reaction(name="chitobiose_rxn",
                          reactants=e(chitobiose) + h2o + adp,
                          products=chitobiose + adp + phosphate)

GeneAssociation(cellobiose_rxn or chitobiose_rxn, SP_1580)


mannitol = Metabolite("manitol", kegg="C00392")
mannitol_rxn = Reaction(name="mannitol_rxn",
                        reactants=e(mannitol) + h2o + atp,
                        products=mannitol + adp + phosphate)

GeneAssociation(mannitol_rxn, SP_1580)

sucrose = Metabolite("sucrose", kegg="C00089")
sucrose_rxn = Reaction(name="sucrose_rxn",
                      reactants=e(sucrose) + h2o + atp,
                      products=sucrose + adp + phosphate)
GeneAssociation(sucrose_rxn, SP_1580)

#sucrose, cellobiose, and chitobiose share the same 1 gene... how to approach this?