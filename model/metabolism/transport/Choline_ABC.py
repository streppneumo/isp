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
choline = Metabolite("choline", kegg="C00114")




choline = Reaction(name="choline",
                    reactants=e(choline) + atp,
                    products=choline + adp + phosphate)


SP_1860 = Gene("SP_1860")
SP_1861 = Gene("SP_1861")

GeneAssociation(choline, SP_1860 & SP_1861)