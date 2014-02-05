
from CellScribe import *

##extracellular = Location("Extracellular", 'e')
##e = extracellular.localizer
##
##cytoplasm = Location("Cytoplasm", 'c')
##c = cytoplasm.localizer
##Metabolite.default_location = cytoplasm


#MAKE TONS OF LISTS for each gene pairrrs

S16 = [Gene("SP_0838") & Gene("SP_0085")]
S =


subunits = Gene("dsadsa")]
S20psubunit = Metabolite("S20psubunit")
S16psubunit = Metabolite("S16psubunit")

def proteinSubunits(subunits, builtPsubunit):
for i in subunits:
    for k in builtPSubunit:
    Reaction(name="builtPSubunit",
            reactants= subunits,
            products=builtPsubunit)


            #pairs=[(glucose, glucose6phosphate), (atp, adp)],
            #minors=[atp, adp])


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
