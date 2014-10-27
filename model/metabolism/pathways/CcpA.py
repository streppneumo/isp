__author__ = 'emmawest'
#GLYCOLYSIS → fructose 1,6-bisphosphate →HPr kinase
# → phosphorylation of HPr on serine residue →
# dimeric complex of P-Ser-HPr-CcpA →
# this makes CcpA able to bind to cre sequences

from model.metabolites import *
from model.common.genes import SP_1413


Dfru16bisP = Metabolite("D-fructose 1,6-bisphosphate", kegg="C00354")

# fill in kegg IDs
HPr = Metabolite("HPr", kegg="")
P_HPr_Ser = Metabolite("P-Hpr-Ser", kegg="")
phosphorylation_rxn = Reaction(name='phosphorylation',
                          reactants= HPr + atp,
                          products=P_HPr_Ser + adp,
                          pairs=[(HPr, P_HPr_Ser), (atp, adp)],
                          minors=[atp, adp],
                          kegg="")

#Gene for HPr kinase (SP_1413) allows this to happen

GeneAssociation(phosphorylation_rxn, SP_1413)
If()
