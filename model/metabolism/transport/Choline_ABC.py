from CellScribe import *
from model.compartments import e
from model.metabolites import atp, adp, phosphate
from model.genes import SP_1860, SP_1861

choline_rxn = Reaction(name="choline_rxn",
                       reactants=e(choline) + atp,
                       products=choline + adp + phosphate)

GeneAssociation(choline_rxn, SP_1860 & SP_1861)

choline = Metabolite("choline", kegg="C00114")
choline_rxn = Reaction(name="choline",
                       reactants=e(choline) + atp,
                       products=choline + adp + phosphate,
                       reversible=True,
                       pairs=[(e(choline), choline)])
GeneAssociation(choline_rxn, SP_1860 & SP_1861)

