
from CellScribe import *

##extracellular = Location("Extracellular", 'e')
##e = extracellular.localizer
##
##cytoplasm = Location("Cytoplasm", 'c')
##c = cytoplasm.localizer
##Metabolite.default_location = cytoplasm


def proteinSubunits(subunits, builtPsubunit):
    Reaction(name="builtPSubunit",
            reactants= subunits,
            products=builtPsubunit)

proteinSubunits(Gene("SP_0838") & Gene("SP_0085"), Gene("SP_0775")) #S16
proteinSubunits(Gene("SP_0272"), Gene("SP_0295")) #S9
proteinSubunits(Gene("SP_0272"), Gene("SP_0234"))#S13
proteinSubunits(Gene("SP_0272"), Gene("SP_0213"))#S19
proteinSubunits(Gene("SP_0218") & Gene("SP_0272"), buildPsubunit)#S12
proteinSubunits(subunits, buildPsubunit)#S5
proteinSubunits(subunits, buildPsubunit)#S11
proteinSubunits(subunits, buildPsubunit)#S21
proteinSubunits(subunits, buildPsubunit)#S10
proteinSubunits(subunits, buildPsubunit)#S14
proteinSubunits(subunits, buildPsubunit)#S3
proteinSubunits(subunits, buildPsubunit)
proteinSubunits(subunits, buildPsubunit)

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
