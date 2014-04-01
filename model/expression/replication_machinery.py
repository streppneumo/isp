#Replication fork machinery
from CellScribe import *
from genes import SP_0993, SP_0274, SP_0895, SP_0865, SP_0936, SP_765, SP_0002, \
     SP_2203, SP_


def replicationmachinery(subunits, builtPsubunit):
    Reaction(name="replicationmachinery",
            reactants= subunits,
            products=builtPsubunit)

DNA_pol_iii = Complex("DNA_pol_iii")
helicase = Enzyme("helicase")
primase = Enzyme("S13_complex")
DNA_pol_i = Enzyme("S19_complex")
DNA_ligase = Complex("S12_complex")


replicationmachinery(SP_0993 & SP_0274 & SP_0895 & SP_0865, SP_0936, SP_765, SP_0002), DNA_pol_iii)
replicationmachinery(SP_2203, helicase)
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
