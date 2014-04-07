from CellScribe import *
from compartments import e, c
from metabolites import *
from genes import SP_2108, SP_2109, SP_2110, SP_2108, SP_2109, SP_2110


βmaltose_transport = Reaction(name="βmaltose_transport",
                              reactants=e(βmaltose) + H20+ atp,
                              products=βmaltose + adp + phosphate,
                              pairs=[(atp, adp)],
                              minors=[atp, adp])

GeneAssociation(βmaltose_transport, SP_2108 & SP_2109 & SP_2110)


maltodextrin_transport = Reaction(name="maltodextrin_transport",
                                  reactants=e(maltodextrin) + H20+ atp,
                                  products=maltodextrin + adp + phosphate,
                                  pairs=[(atp, adp)],
                                  minors=[atp, adp])

<<<<<<< HEAD
GeneAssociation(maltodextrin_transport, SP_2108 & SP_2109 & SP_2110)
=======
maltodextrin_GA = GeneAssociation(maltodextrin, SP_2108 & SP_2109 & SP_2110)

# In the absence of maltose, malR binds to the DNA between these two divergent operons to repress them

If (malR & ~maltose, ~malXCD)
If (malR & ~maltose, ~malMP)
>>>>>>> FETCH_HEAD
