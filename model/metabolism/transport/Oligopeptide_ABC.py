from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_1527, SP_1891, SP_0366, SP_1887, SP_1888, SP_1889 , SP_1890



oligopeptide = Metabolite("oligopeptide", kegg="C00098")

oligopeptide_rxn = Reaction(name="oligopeptide_rxn",
                            reactants=e(oligopeptide) + H20 + atp,
                            products=oligopeptide + adp + phosphate)

GeneAssociation(oligopeptide_rxn, SP_1527 or SP_1891 or SP_0366 or SP_1887 or SP_1888 or SP_1889 or SP_1890 )
