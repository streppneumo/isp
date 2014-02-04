from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp")
adp = Metabolite("adp")
phosphate = Metabolite("phosphate")
H20 = Metabolite("H20")
spermidine = Metabolite("spermidine", kegg="C00315")
putrescine = Metabolite("putrescine", kegg="C00134")



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
                            reactants=e(putrescine) + H20+ atp,
                            products=glucose + adp + phosphate)

SP_1386 = Gene("SP_1386")
SP_1387 = Gene("SP_1387")
SP_1388 = Gene("SP_1388")
SP_1389 = Gene("SP_1389")
putrescine_GA = GeneAssociation(putrescine, SP_1386 & SP_1387 & SP_1388 & SP_1389)