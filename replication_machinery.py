#Replication fork machinery


def replicationmachinery(subunits, builtPsubunit):
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
