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
ferrichrome = Metabolite("ferrichrome", kegg="C06228")

#iron vs ferrichrome?

ferrichrome = Reaction(name="ferrichrome_ABC",
                      reactants=e(ferrichrome) + H20 + atp,
                      products=ferrichrome + adp + phosphate,
                      pairs=[(atp, adp)],
                      minors=[atp, adp])

SP_1386 = Gene("SP_1032")
SP_1387 = Gene("SP_1033")
SP_1388 = Gene("SP_1034")
SP_1389 = Gene("SP_1035")
ferrichrome_GA = GeneAssociation(ferrichrome, SP_1032 & SP_1033 & SP_1034 & SP_1035)

# also (SP_1869 SP_1870 SP_1871 SP_1872) another cluster
