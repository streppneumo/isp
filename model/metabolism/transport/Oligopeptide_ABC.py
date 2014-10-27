from CellScribe import *

from ...common import *



oligopeptide = Metabolite("oligopeptide", kegg="C00098")

oligopeptide_rxn = Reaction(name="oligopeptide_rxn",
                            reactants=e(oligopeptide) + H2O + ATP,
                            products=oligopeptide + ADP + phosphate)

GeneAssociation(oligopeptide_rxn, (SP_1527 | SP_1891 | SP_0366 | SP_1887 |
                                   SP_1888 | SP_1889 | SP_1890))
