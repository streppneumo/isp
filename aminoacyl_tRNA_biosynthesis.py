__author__ = 'Corey'

from CellScribe import *

#REACTION TEMPLATE
#NAME = Reaction(name="NAME",
#                       reactants=REACT1 + REACT2,
#                       products=PROD1 + PROD2,
#                       pairs=[(pair1, pair1), (pair2, pair2)],
#                       minors=[minor1, minor2])

#GENE ASSOCIATION TEMPLATE
#GENE = Gene("GENE")
#REACTIONNAME_GA = GeneAssociation(REACTIONNAME, GENE)

extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp")
amp = Metabolite("adp")

#CHARGE tRNA-Val REACTION. reaction is identical for following amino acids (gene associations below):
#Leucine, Isoleucine, Arginine, Proline, Histidine, Tyrosine, Tryptophan, Alanine, Threonine, Serine, Methionine
#SP_0254.... 1659..... 2078.... 0264...... 2121...... 2100...... 2229.... 1383..... 1639...... 0411..... 0788

tRNA_val = RNA("tRNA_val")
L_valine = Metabolite("L_valine")
L_valyl_tRNA = RNA("L_valyl_tRNA")
#need to create tRNA...write RNA class? or use metabolite?

chargeValRNA = Reaction(name='chargeValRNA',
                        reactants=tRNA_val + L_valine,
                        products=L_valyl_tRNA + amp,
                        pairs=[(tRNA_val, L_valyl_tRNA), (atp, amp)],
                        minors=[atp, amp])

SP_0568 = Gene("SP_0568")
chargeValRNA_GA = GeneAssociation(chargeValRNA, SP_0568)
#gene association: valyl-tRNA synthetase

#CHARGE tRNA-Phe REACTION. reaction is not simple because phenylalyl-tRNA synthetase has alpha and beta subunits (two GAs)
#system is similar to Glycine, which also has alpha and beta subunits

tRNA_phe = RNA("tRNA_phe")
L_phenylalanine = Metabolite("L_phenylalanine")
L_phenylalanyl_tRNA = Metabolite("L_phenylalanyl_tRNA")

chargePheRNA = Reaction(name='chargePheRNA',
                        reactants=tRNA_phe + L_phenylalanine,
                        products=L_phenylalanyl_tRNA + amp,
                        pairs=[(tRNA_phe, L_phenylalanyl_tRNA), (atp, amp)],
                        minors=[atp, amp])

SP_0581 = Gene("SP_0581") #beta subunit
SP_0579 = Gene("SP_0579") #alpha subunit
chargePheRNA_GA = GeneAssociation(chargePheRNA, SP_0581 & SP_0579)
#gene association: phenylalanyl-tRNA synthetase subunits