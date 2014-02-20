
from CellScribe import *

##extracellular = Location("Extracellular", 'e')
##e = extracellular.localizer
##
##cytoplasm = Location("Cytoplasm", 'c')
##c = cytoplasm.localizer
##Metabolite.default_location = cytoplasm


16S_5S_23S_operon = Operon("16S_5S_23S_operon")

L33_L28_operon = Operon("L33_L28_operon")


16S_rrna = RRNA("16S_rrna")
5S_rrna = RRNA("5S_rrna")
23S_rrna = RRNA("23S_rrna")


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
#proteinSubunits(subunits, buildPsubunit) Below is the rRNA 16S interaction:
proteinSubunits(Gene("SP_0218") & Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0224") & Gene("SP_1626") & Gene("SP_0272") \
                & Gene("SP_rrnaA16S"), 16S_rrna)
                
def proteinSubunitsL(subunitsL, builtPsubunitL):
    Reaction(name="builtPSubunitL",
            reactants= subunitsL,
            products=builtPsubunitL)

L13_complex = Complex("L13_complex")
L2_complex = Complex("L2_complex")
L22_complex = Complex("L22_complex")
L17_complex = Complex("L17_complex")
L21_complex = Complex("L21_complex")
L29_complex = Complex("L29_complex")
L15_complex = Complex("L15_complex")
L33_complex = Complex("L33_complex")
L18_complex = Complex("L18_complex")
L5_complex = Complex("L5_complex")
L10_complex = Complex("L10_complex")
L28_complex = Complex("L28_complex")
L27_complex = Complex("L27_complex")
#L25_complex = Complex("L25_complex") NOT IN STREP. BUT IT IS IN E. COLI

proteinSubunitsL(Gene("SP_0961") & Gene("SP_0294"), L13_complex)
proteinSubunitsL(Gene("SP_0210") & Gene("SP_0212"), L2_complex)
proteinSubunitsL(Gene("SP_0210") & Gene("SP_0220") & Gene("SP_0237") & Gene("SP_0214"), L22_complex) 
proteinSubunitsL(Gene("SP_0229") & Gene("SP_0209") & Gene("SP_0237"), L17_complex)
proteinSubunitsL(Gene("SP_0961") & Gene("SP_1105"), L21_complex)
proteinSubunitsL(Gene("SP_0210") & Gene("SP_0217"), L29_complex)
proteinSubunitsL(Gene("SP_0210") & Gene("SP_0209") & Gene("SP_0212") & Gene("SP_0229"), L15_complex)
proteinSubunitsL(Gene("SP_0441") & Gene("SP_0973")& Gene("SP_2009")& Gene("SP_2135"), L33_complex) #operon with L28 subunit
proteinSubunitsL(Gene("SP_0229") & Gene("SP_0226"), L18_complex)
proteinSubunitsL(Gene("SP_0212") & Gene("SP_0221"), L5_complex)
proteinSubunitsL(Gene("SP_0229") & Gene("SP_1355"), L10_complex)
proteinSubunitsL(Gene("SP_0229") & Gene("SP_0237") & Gene("SP_0441"), L28_complex) #operon with L33 subunit
proteinSubunitsL(Gene("SP_0229") & Gene("SP_1107"), L27_complex)
#proteinSubunitsL(Gene("SP_0229") & Gene("SP_2215"), L25_complex) NOT IN STREP. BUT IT IS IN E. COLI
proteinSubunitsL(Gene("SP_0221") & Gene("SP_0229") & Gene("SP_0226") & 


