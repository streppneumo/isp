
from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


atp = Metabolite("atp")
adp = Metabolite("adp")
H20 = Metabolite("H20")
βmaltose = Metabolite("βmaltose")
maltodextrin = Metabolite("maltodextrin")

βmaltose_transport = Reaction(name="βmaltose_transport",
                       reactants=βmaltose + H20+ atp,
                       products=βmaltose + adp + phosphate,
                       pairs=[(atp, adp)],
                       minors=[atp, adp])

SP_2108 = Gene("SP_2108")
SP_2109 = Gene("SP_2109")
SP_2110 = Gene("SP_2110")

βmaltose_GA = GeneAssociation(βmaltose, SP_2108 & SP_2109 & SP_2110)


maltodextrin_transport = Reaction(name="maltodextrin_transport",
                       reactants=maltodextrin + H20+ atp,
                       products=maltodextrin + adp + phosphate,
                       pairs=[(atp, adp)],
                       minors=[atp, adp])


SP_2108 = Gene("SP_2108")
SP_2109 = Gene("SP_2109")
SP_2110 = Gene("SP_2110")

maltodextrin_GA = GeneAssociation(maltodextrin, SP_2108 & SP_2109 & SP_2110)
