#Ribosomal protein and RNA subunits

from CellScribe import *
from model.operons import rRNA_A, rRNA_B, rRNA_C, rRNA_D

S16_complex = Complex("S16_complex", Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0775"))
S9_complex = Complex("S9_complex", Gene("SP_0272") & Gene("SP_0295"))
S13_complex = Complex("S13_complex", Gene("SP_0272") & Gene("SP_0234"))
S19_complex = Complex("S19_complex", Gene("SP_0272") & Gene("SP_0213"))
S12_complex = Complex("S12_complex", Gene("SP_0218") & Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227") & Gene("SP_0271"))
S5_complex = Complex("S5_complex", Gene("SP_0775") & Gene("SP_0224") & Gene("SP_0227"))
S11_complex = Complex("S11_complex", Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0235"))
S21_complex = Complex("S21_complex", Gene("SP_1541") & Gene("SP_1539") & Gene("SP_0227") & Gene("SP_1414"))
S6_S18_complex = Complex("S6_S18_complex", Gene("SP_1626") & Gene("SP_1541") & Gene("SP_1539"))
S10_complex = Complex("S10_complex", Gene("SP_0295") & Gene("SP_0208"))
S14_complex = Complex("S14_complex", Gene("SP_0208") & Gene("SP_0295") & Gene("SP_0213") & Gene("SP_0222"))
S3_complex = Complex("S3_complex", Gene("SP_0227") & Gene("SP_0208") & Gene("SP_0215"))
S2_complex = Complex("S2_complex", Gene("SP_0215") & Gene("SP_2215"))
r_16S_rrna = Complex("r_16S_rrna", Gene("SP_0218") & Gene("SP_0838") & Gene("SP_0085") & Gene("SP_0224") & Gene("SP_1626") & Gene("SP_0272") \
                & (Gene("SP_rrnaA16S") | Gene("SP_rrnaB16S") | Gene("SP_rrnaC16S") | Gene("SP_rrnaD16S"))

L13_complex = Complex("L13_complex", Gene("SP_0961") & Gene("SP_0294"))
L2_complex = Complex("L2_complex", Gene("SP_0210") & Gene("SP_0212"))
L22_complex = Complex("L22_complex", Gene("SP_0210") & Gene("SP_0220") & Gene("SP_0237") & Gene("SP_0214"))
L17_complex = Complex("L17_complex", Gene("SP_0229") & Gene("SP_0209") & Gene("SP_0237"))
L21_complex = Complex("L21_complex", Gene("SP_0961") & Gene("SP_1105"))
L29_complex = Complex("L29_complex", Gene("SP_0210") & Gene("SP_0217"))
L15_complex = Complex("L15_complex", Gene("SP_0210") & Gene("SP_0209") & Gene("SP_0212") & Gene("SP_0229"))
L33_complex = Complex("L33_complex", Gene("SP_0441") & Gene("SP_0973")& Gene("SP_2009")& Gene("SP_2135"))
L18_complex = Complex("L18_complex", Gene("SP_0229") & Gene("SP_0226"))
L5_complex = Complex("L5_complex", Gene("SP_0212") & Gene("SP_0221"))
L10_complex = Complex("L10_complex", Gene("SP_0229") & Gene("SP_1355"))
L28_complex = Complex("L28_complex", Gene("SP_0229") & Gene("SP_0237") & Gene("SP_0441"))
L27_complex = Complex("L27_complex", Gene("SP_0229") & Gene("SP_1107"))
L16_complex = Complex("L16_complex", Gene("SP_0225") & Gene("SP_1355") & Gene("SP_0630") & Gene("SP_0216"))
#L25_complex = Complex("L25_complex") NOT IN STREP. BUT IT IS IN E. COLI
r_5S_rrna = Complex("r_5S_rrna", Gene("SP_0221") & Gene("SP_0229") & Gene("SP_0226") & ((Gene("SP_0212") & Gene("SP_0209")) | (Gene("SP_0212") & Gene("SP_0210"))) \
    & (Gene("SP_rrnaA5S") | Gene("SP_rrnaB5S") | Gene("SP_rrnaC5S") | Gene("SP_rrnaD5S")))
r_23S_rrna = Complex("r_23S_rrna", Gene("SP_0220") & Gene("SP_0961") & Gene("SP_0210") & Gene("SP_0211") & Gene("SP_0209") \
    & Gene("SP_2204") & Gene("SP_0631") & Gene("SP_0212") & (Gene("SP_rrnaA23S") | Gene("SP_rrnaB23S") | Gene("SP_rrnaC23S") | Gene("SP_rrnaD23S")))