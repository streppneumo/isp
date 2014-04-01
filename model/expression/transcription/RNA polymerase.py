from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_1961, SP_1960, SP_0236, SP_1737, SP_0493


#define function to build subunits with gene associations
def buildsubunit(subunitname, associatedgene):
    subunit = complex(subunitname)
    GeneAssociation(subunit, associatedgene)
complex

#define function to combine subunits to make complex
def buildcomplex(complexname, complexkegg, ):
    Reaction(

    )


#call the build function for all 5 subunits
buildsubunit('beta_subunit', SP_1961)
buildsubunit('beta_prime_subunit', SP_1960)
buildsubunit('aplha_subunit', SP_0236)
buildsubunit('omega_subunit', SP_1737)
buildsubunit('delta_subunit', SP_0493)

#call the build complex to build RNA poly by combining all 5 subunits
buildcomplex('rna_polymerase', beta_subunit,)


#not code, just associations
#SP_1961 beta_subunit
#SP_1960 beta_prime_subunit
#SP_0236 alpha_subunit
#SP_1737 omega_subunit
#SP_0493 delta_subunit
