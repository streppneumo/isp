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
amp = Metabolite("amp")

#generic charge simple tRNA


def charge_trna_simple(aaname, trnaname, chargedrna_name, *associated_genes):

    trna = RNA(trnaname)
    amino_acid = Metabolite(aaname)
    charged_trna = Metabolite(chargedrna_name)

    charge_trna = Reaction(name='charge' + aaname,
                           reactants=trna + amino_acid + atp,
                           products=charged_trna + amp,
                           pairs=[(trna, charged_trna), (atp, amp)],
                           minors=[atp, amp])

    GeneAssociation(charge_trna, associated_genes)

charge_trna_simple("L-valine", "tRNA_val", "L_valyl_tRNA", Gene('SP_0568'))
charge_trna_simple("L_leucine", "tRNA_leu", "L_leucyl_tRNA", Gene('SP_0254'))
charge_trna_simple("L_isoleucine", "tRNA_ile", "L_isoleucyl_tRNA", Gene('SP_1659'))
charge_trna_simple("L-lysine", "tRNA_lys", "L_lysyl_tRNA", Gene('SP_0713'))
charge_trna_simple("L_arginine", "tRNA_arg", "L_arginyl_tRNA", Gene('SP_2078'))
charge_trna_simple("L_proline", "tRNA_pro", "L_prolyl_tRNA", Gene('SP_0264'))
charge_trna_simple("L_histidine", "tRNA_his", "L_histidyl_tRNA", Gene('SP_2121'))
charge_trna_simple("L_phenylalanine", "tRNA_phe", "L_phenylalanyl_tRNA", Gene('SP_0581') & Gene('SP_0579'))
charge_trna_simple("L_tyrosine", "tRNA_tyr", "L_tyrosyl_tRNA", Gene('SP_2100'))
charge_trna_simple("L_tryptophan", "tRNA_trp", "L_tryptophanyl_tRNA", Gene('SP_2229'))
charge_trna_simple("L_alanine", "tRNA_ala", "L_alanyl_tRNA", Gene('SP_1383'))
charge_trna_simple("L_glycine", "tRNA_gly", "L_glycyl_tRNA", Gene('SP_1474') & Gene('SP_1475'))
charge_trna_simple("L_threonine", "tRNA_thr", "L_threonyl_tRNA", Gene('1631'))
charge_trna_simple("L_serine", "tRNA_ser", "L_seryl_tRNA", Gene('SP_0411'))
charge_trna_simple("L_methionine", "tRNA_met", "L_methionyl_tRNA", Gene('SP_0788'))

