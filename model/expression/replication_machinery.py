#Replication fork machinery
from CellScribe import *
from model.genes import SP_0993, SP_0274, SP_0895, SP_0865, SP_0936, SP_765, SP_0002, \
     SP_2203, SP_1072, SP_1540, SP_1908, 


def replicationmachinery(subunits, builtPsubunit):
    Reaction(name="replicationmachinery",
            reactants= subunits,
            products=builtPsubunit)

DNA_pol_iii = Complex("DNA_pol_iii")
helicase = Enzyme("helicase")
primase = Enzyme("primase")
DNA_pol_i = Enzyme("DNA_pol_i")
DNA_ligase = Enzyme("DNA_ligase")
SSB_DNA_rep = Enzyme{"SSB_DNA_rep")


replicationmachinery(SP_0993 & SP_0274 & SP_0895 & SP_0865, SP_0936, SP_765, SP_0002), DNA_pol_iii)
replicationmachinery(SP_2203, helicase)
replicationmachinery(SP_1072, primase)
replicationmachinery(SP_1540 & SP_1908, SSB_DNA_rep)
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
