
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



proteinSubunits(Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0775"), S16_complex) #S16
proteinSubunits(Gene("SP_0272") & Gene("SP_0295"), S9_complex) #S9
proteinSubunits(Gene("SP_0272") & Gene("SP_0234"), S13_complex)#S13
proteinSubunits(Gene("SP_0272") & Gene("SP_0213"), S19_complex)#S19
proteinSubunits(Gene("SP_0218") & Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227") & Gene("SP_0271"), S12_complex)#S12
proteinSubunits(Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227"), S5_complex)#S5
proteinSubunits(Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0235"), S11_complex)#S11
proteinSubunits(Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0227") & Gene("SP_1414"), S21_complex)#S21
proteinSubunits(Gene("SP_1626") & Gene("SP_1541") & Gene("SP_1539"), S6_S18_complex)#S6_S18 complex (heterodimers)
proteinSubunits(Gene("SP_0295") & Gene("SP_0208"), S10_complex)#S10
proteinSubunits(Gene("SP_0208") & Gene("SP_0295") & Gene("SP_0213") & Gene("SP_0222"), S14_complex)#S14
proteinSubunits(Gene("SP_0227") & Gene("SP_0208") & Gene("SP_0215"), S3_complex)#S3
proteinSubunits(Gene("SP_0215") & Gene("SP_2215"), S2_complex)#S2
#proteinSubunits(subunits, buildPsubunit)


def proteinSubunitsL(subunitsL, builtPsubunitL):
    Reaction(name="builtPSubunitL",
            reactants= subunitsL,
            products=builtPsubunitL)

L13_complex = Complex("L13_complex")
L22_complex = Complex("L22_complex")
L17_complex = Complex("L17_complex")
L3_complex = Complex("L3_complex")
L21_complex = Complex("L21_complex")
L29_complex = Complex("L29_complex")
L15_complex = Complex("L15_complex")
L33_complex = Complex("L33_complex")
L18_complex = Complex("L18_complex")
L5_complex = Complex("L5_complex")
L10_complex = Complex("L10_complex")
L28_complex = Complex("L28_complex")
L27_complex = Complex("L27_complex")
L25_complex = Complex("L25_complex")

proteinSubunitsL(Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0775"), L13_complex) #S16
proteinSubunitsL(Gene("SP_0272") & Gene("SP_0295"), L22_complex) #S9
proteinSubunitsL(Gene("SP_0272") & Gene("SP_0234"), L17_complex)#S13
proteinSubunitsL(Gene("SP_0272") & Gene("SP_0213"), L3_complex)#S19
proteinSubunitsL(Gene("SP_0218") & Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227") & Gene("SP_0271"), L21_complex)#S12
proteinSubunitsL(Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227"), L29_complex)#S5
proteinSubunitsL(Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0235"), L15_complex)#S11
proteinSubunitsL(Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0227") & Gene("SP_1414"), L33_complex)#S21
proteinSubunitsL(Gene("SP_1626") & Gene("SP_1541") & Gene("SP_1539"), L18_complex)#S6_S18 complex (heterodimers)
proteinSubunitsL(Gene("SP_0295") & Gene("SP_0208"), L5_complex)#S10
proteinSubunitsL(Gene("SP_0208") & Gene("SP_0295") & Gene("SP_0213") & Gene("SP_0222"), L10_complex)#S14
proteinSubunitsL(Gene("SP_0227") & Gene("SP_0208") & Gene("SP_0215"), L28_complex)#S3
proteinSubunitsL(Gene("SP_0215") & Gene("SP_2215"), L27_complex)#S2
proteinSubunitsL(Gene("SP_0215") & Gene("SP_2215"), L25_complex)#S2


