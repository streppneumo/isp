from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp")
adp = Metabolite("adp")
phosphate = Metabolite("phosphate")
H20 = Metabolite("H20",kegg="C00001")
spermidine = Metabolite("spermidine", kegg="C00315")
putrescine = Metabolite("putrescine", kegg="C00134")
cellobiose = Metabolite("cellobiose", kegg="C00185")
chitobiose = Metabolite("chitobiose", kegg="C01674")
mannitol = Metabolite("mannitol", kegg="C00392")
sucrose = Metabolite("sucrose", kegg="C00089")





spermidine = Reaction(name="spermidine",
                      reactants=e(spermidine) + H20 + atp,
                      products=spermidine + adp + phosphate,
                      pairs=[(spermidine, putrescine), (atp, adp)],
                      minors=[atp, adp])

SP_1386 = Gene("SP_1386")
SP_1387 = Gene("SP_1387")
SP_1388 = Gene("SP_1388")
SP_1389 = Gene("SP_1389")
spermidine_GA = GeneAssociation(spermidine, SP_1386 & SP_1387 & SP_1388 & SP_1389)



putrescine = Reaction(name="putrescine",
                            reactants=e(putrescine) + H20 + atp,
                            products=glucose + adp + phosphate)

SP_1386 = Gene("SP_1386")
SP_1387 = Gene("SP_1387")
SP_1388 = Gene("SP_1388")
SP_1389 = Gene("SP_1389")
putrescine_GA = GeneAssociation(putrescine, SP_1386 & SP_1387 & SP_1388 & SP_1389)

cellobiose = Reaction(name="cellobiose",
                      reactants=e(cellobiose) + H20 + atp,
                      products=cellobiose + adp + phosphate)

SP_1580 = Gene("SP_1580")
cellobiose_GA = GeneAssociation(cellobiose or chitobiose, SP_1580)

chitobiose = Reaction(name="chitobiose",
                      reactants=e(chitobiose) + H20 + adp,
                      products=chitobiose + adp + phosphate)

SP_1580 = Gene("SP_1580")
chitobiose_GA = GeneAssociation(chitobiose or cellobiose, SP_1580)

mannitol = Reaction(name="mannitol",
                    reactants=e(mannitol) + H20 + atp,
                    products=mannitol + adp + phosphate)

mannitol_GA = GeneAssociation(mannitol, SP_1580)

sucrose = Reaction(name="sucrose",
                      reactants=e(sucrose) + H20 + atp,
                      products=sucrose + adp + phosphate)

SP_1580 = Gene("SP_1580")
sucrose_GA = GeneAssociation(sucrose, SP_1580)
