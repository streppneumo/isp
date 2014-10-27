from model.metabolites import *
from model.common.genes import SP_1961, SP_1960, SP_0236, SP_1737, SP_0493


#this function takes a subunit name and its associate gene(s) and creates a subunit object via subunit class
def buildsubunit(subunitname, associatedgenes):  # "associatedgenes" arg can be one or many genes, related by & or |
    subunit = Subunit(subunitname, associatedgenes)
    GeneAssociation(subunit, associatedgenes)
    return subunit  # returns the subunit so that we can parse it into the subunit variable name when calling function

#call the build function for all 5 subunits
#for these subunits, they all have a common Kegg ID...is that the ID for the rna poly complex? how do we tag these?
beta_subunit = buildsubunit('beta_subunit', SP_1961)
beta_prime_subunit = buildsubunit('beta_prime_subunit', SP_1960)
alpha_subunit = buildsubunit('alpha_subunit', SP_0236)
omega_subunit = buildsubunit('omega_subunit', SP_1737)
delta_subunit = buildsubunit('delta_subunit', SP_0493)

#call the build complex to build RNA poly by combining all 5 subunits
rna_polymerase = SubComplex('rna_polymerase', beta_subunit, beta_prime_subunit, alpha_subunit, omega_subunit,
                            delta_subunit)
#need to make sure we set up the SubComplex class so that it takes however many subunits are placed as args.
