#Replication fork machinery

from CellScribe import *
from model.genes import SP_0993, SP_0274, SP_0895, SP_0865, SP_0936, SP_0765, SP_0002, \
     SP_2203, SP_1072, SP_1540, SP_1908, SP_0403, SP_1156, SP_0032, SP_1117


DNA_pol_iii = Complex("DNA_pol_iii", SP_0993 & SP_0274 & SP_0895 & SP_0865 & SP_0936 & SP_0765 & SP_0002)
helicase = Complex("helicase", SP_2203) #maybe rename this and below to an enzyme class later?
primase = Complex("primase", SP_1072)
DNA_pol_i = Complex("DNA_pol_i", SP_0032)
DNA_ligase = Complex("DNA_ligase", SP_1117)
SSB_DNA_rep = Complex("SSB_DNA_rep", SP_1540 & SP_1908)
RNaseH = Complex("RNaseH", SP_0403 & SP_1156)