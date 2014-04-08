from CellScribe.main import *
from model.compartments import e, c
from model.metabolites import *
from model.genes import SP_1961, SP_1960, SP_0236, SP_1737, SP_0493


#this function takes a subunit name and its associate gene(s) and creates a subunit object via subunit class
def buildsubunit(subunitname, associatedgene):
    subunit = Subunit(subunitname, associatedgene)
    GeneAssociation(subunit, associatedgene)


#define function to combine subunits to make complex
def buildcomplex(complexname, complexkegg, ):
    Reaction(name='charge' + aaname,
             reactants=trna + amino_acid + atp,
             products=complexname,
             kegg=complexkegg)


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
