
from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


S4psubunit = Metabolite("S4psubunit")
S20psubunit = Metabolite("S20psubunit")
S16psubunit = Metabolite("S16psubunit")

S16psubunit = Reaction(name="S16psubunit",
                       reactants=S4psubunit + S20psubunit,
                       products=S16psubunit
                       #pairs=[(glucose, glucose6phosphate), (atp, adp)],
                       #minors=[atp, adp])

SP_0775 = Gene("SP_0775")
S16psubunit_GA = GeneAssociation(S16psubunit, SP_0085 & SP_0838)








##glucose_transport1 = Reaction(name="glucose_transport1",
##                              reactants=e(glucose) + atp,
##                              products=glucose + adp)
##
##SP_1000 = Gene("SP_1000")
##SP_1001 = Gene("SP_1001")
##SP_1002 = Gene("SP_1002")
##
##glucose_transport1_GA = GeneAssociation(glucose_transport1, SP_1000 & (SP_1001 | SP_1002))
##
##if __name__ == "__main__":
##    print glucokinase
##    #print glucokinase_GA
##
##    #print glucose_transport1
##    #print glucose_transport1_GA
