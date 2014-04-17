#Replication fork machinery
from CellScribe import *
from model.genes import SP_0993, SP_0274, SP_0895, SP_0865, SP_0936, SP_0765, SP_0002, \
     SP_2203, SP_1072, SP_1540, SP_1908, SP_0403, SP_1156, SP_0032, SP_1117


def replicationmachinery_DNA_pol_iii(subunits, builtPsubunit):
    Reaction(name="replicationmachinery",
            reactants= subunits,
            products=builtPsubunit)
    
def replicationmachinery(gene, enzyme):
    Reaction(name="replicationmachinery",
            reactants= subunits,
            products=builtPsubunit)

DNA_pol_iii = Complex("DNA_pol_iii")
helicase = Enzyme("helicase")
primase = Enzyme("primase")
DNA_pol_i = Enzyme("DNA_pol_i")
DNA_ligase = Enzyme("DNA_ligase")
SSB_DNA_rep = Enzyme("SSB_DNA_rep")
RNaseH = Enzyme("RNaseH")


replicationmachinery_DNA_pol_iii(SP_0993 & SP_0274 & SP_0895 & SP_0865, SP_0936, SP_765, SP_0002, DNA_pol_iii)
replicationmachinery(SP_2203, helicase)
replicationmachinery(SP_1072, primase)
replicationmachinery(SP_1540 & SP_1908, SSB_DNA_rep)
replicationmachinery(SP_0403 & SP_1156, RNaseH)
replicationmachinery(SP_0032, DNA_pol_i)
replicationmachinery(SP_1117, DNA_ligase)