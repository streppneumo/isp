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
l-lysine = Metabolite("l-lysine", kegg="C00047")
l-glutamate = Metabolite("l-glutamate", kegg="C00064")



l-lysine = Reaction(name="l-lysine",
                    reactants=e(l-lysine) + H20 + atp,
                    products=l-lysine + adp + phosphate,
                    pairs=[(atp, adp)],
                    minors=[atp, adp])

SP_1386 = Gene("SP_0452")
SP_1387 = Gene("SP_0453")

l-lysine_GA = GeneAssociation(l-lysine, SP_0452 & SP_0453)



l-glutamate= Reaction(name="l-glutamate",
                      reactants=e(l-glutamate) + H20+ atp,
                      products=l-glutamate + adp + phosphate)

SP_0609 = Gene("SP_0609")
SP_0607 = Gene("SP_0607")
SP_0608 = Gene("SP_0608")
SP_0610 = Gene("SP_0610")
l-glutamate_GA = GeneAssociation(l-glutamate, SP_0609 & SP_0607 & SP_0608 & SP_0610)