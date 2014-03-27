
from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


atp = Metabolite("atp")
adp = Metabolite("adp")
H20 = Metabolite("H20", kegg="C00001")
βmaltose = Metabolite("βmaltose", kegg="C00208")
maltodextrin = Metabolite("maltodextrin", kegg="C01935")

βmaltose_transport = Reaction(name="βmaltose_transport",
                       reactants=e(βmaltose) + H20+ atp,
                       products=βmaltose + adp + phosphate,
                       pairs=[(atp, adp)],
                       minors=[atp, adp])

SP_2108 = Gene("SP_2108")
SP_2109 = Gene("SP_2109")
SP_2110 = Gene("SP_2110")

βmaltose_GA = GeneAssociation(βmaltose, SP_2108 & SP_2109 & SP_2110)


maltodextrin_transport = Reaction(name="maltodextrin_transport",
                       reactants=e(maltodextrin) + H20+ atp,
                       products=maltodextrin + adp + phosphate,
                       pairs=[(atp, adp)],
                       minors=[atp, adp])


SP_2108 = Gene("SP_2108")
SP_2109 = Gene("SP_2109")
SP_2110 = Gene("SP_2110")

maltodextrin_GA = GeneAssociation(maltodextrin, SP_2108 & SP_2109 & SP_2110)

# In the absence of maltose, malR binds to the DNA between these two divergent operons to repress them

If (malR & ~maltose, ~malXCD)
If (malR & ~maltose, ~malMP)
