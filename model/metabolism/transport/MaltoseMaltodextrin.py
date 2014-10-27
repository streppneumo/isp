from CellScribe import *

from ...common import *


maltose_transport = Reaction(name="maltose_transport",
                              reactants=e(maltose) + H2O + ATP,
                              products=maltose + ADP + phosphate,
                              pairs=[(ATP, ADP)],
                              minors=[ATP, ADP])

GeneAssociation(maltose_transport, SP_2108 & SP_2109 & SP_2110)


maltodextrin_transport = Reaction(name="maltodextrin_transport",
                                  reactants=e(maltodextrin) + H2O + ATP,
                                  products=maltodextrin + ADP + phosphate,
                                  pairs=[(ATP, ADP)],
                                  minors=[ATP, ADP])

GeneAssociation(maltodextrin_transport, SP_2108 & SP_2109 & SP_2110)

# In the absence of maltose, malR binds to the DNA between these two
# divergent operons to repress them
If(malR & ~maltose, ~malXCD)
If(malR & ~maltose, ~malMP)
