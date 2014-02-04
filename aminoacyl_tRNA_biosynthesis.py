__author__ = 'Corey'

from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


tRNA_val = RNA("tRNA_val")
L_valine = Metabolite("L_valine")
L_valyl_tRNA = RNA("L_valyl_tRNA")
atp = Metabolite("atp")
amp = Metabolite("adp")
#need to create tRNA...write RNA class? or use metabolite?

chargeValRNA = Reaction(name='chargeValRNA',
                        reactants=tRNA_val + L_valine,
                        products=L_valyl_tRNA + amp,
                        pairs=[(tRNA_val, L_valyl_tRNA), (atp, amp)],
                        minors=[atp, amp])

SP_0568 = Gene("SP_0568")
chargeValRNA_GA = GeneAssociation(chargeValRNA, SP_0568)
#gene association: valyl-tRNA synthetase

#REACTION TEMPLATE
#NAME = Reaction(name="NAME",
#                       reactants=REACT1 + REACT2,
#                       products=PROD1 + PROD2,
#                       pairs=[(pair1, pair1), (pair2, pair2)],
#                       minors=[minor1, minor2])

#GENE ASSOCIATION TEMPLATE
#GENE = Gene("GENE")
#REACTIONNAME_GA = GeneAssociation(REACTIONNAME, GENE)