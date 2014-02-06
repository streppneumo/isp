
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

S16_complex = Complex("S16_complex")
S9_complex = Complex("S9_complex")
S13_complex = Complex("S13_complex")
S19_complex = Complex("S19_complex")
S12_complex = Complex("S12_complex")
S5_complex = Complex("S5_complex")
S21_complex = Complex("S21_complex")
S6_S18_complex = Complex("S6_S18_complex")
S10_complex = Complex("S10_complex")
S14_complex = Complex("S14_complex")
S3_complex = Complex("S3_complex")
S2_complex = Complex("S2_complex")



proteinSubunits(Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0775"), ) #S16
proteinSubunits(Gene("SP_0272"), Gene("SP_0295")) #S9
proteinSubunits(Gene("SP_0272"), Gene("SP_0234"))#S13
proteinSubunits(Gene("SP_0272"), Gene("SP_0213"))#S19
proteinSubunits(Gene("SP_0218") & Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227"), Gene("SP_0271"))#S12
proteinSubunits(Gene("SP_0775") & Gene("SP_0224"), Gene("SP_0227"))#S5
proteinSubunits(Gene("SP_1541") & Gene("SP_1539"), Gene("SP_0235"))#S11
proteinSubunits(Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0227"), Gene("SP_1414"))#S21
proteinSubunits(Gene("SP_1626"), Gene("SP_1541") & Gene("SP_1539"))#S6_S18 complex (heterodimers)
proteinSubunits(Gene("SP_0295"),  Gene("SP_0208"))#S10
proteinSubunits(Gene("SP_0208") & Gene("SP_0295") & Gene("SP_0213"), Gene("SP_0222"))#S14
proteinSubunits(Gene("SP_0227") & Gene("SP_0208"), Gene("SP_0215"))#S3
proteinSubunits(Gene("SP_0215"), Gene("SP_2215"))#S2
#proteinSubunits(subunits, buildPsubunit)


def proteinSubunitsL(subunitsL, builtPsubunitL):
    






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
