__author__ = 'Corey'

from CellScribe import *

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

# L_glutamyl_tRNA from glutamate and tRNA_gln. get to L_glutaminyl_tRNA through SP_0436, SP_0437, SP_0438
charge_trna_simple("L_glutamate", "tRNA_gln", "L_glutamyl_tRNA", "SP_2069")

# L_seryl_tRNA using

# make N_formyl_methionyl_tRNA
ten_formyl_THF = Metabolite("ten_formyl_THF")
L_methionyl_tRNA = Metabolite("L_methionyl_tRNA")
THF = Metabolite("THF")
N_formylmethionyl_tRNA = Metabolite("N_formylmethionyl_tRNA")
h2o = Metabolite("h2o")

met_tRNA_formyltransferase = Reaction(name='met_tRNA_formyltransferase',
                                      reactants=h2o + ten_formyl_THF + L_methionyl_tRNA,
                                      products=THF + N_formylmethionyl_tRNA,
                                      pairs=[(ten_formyl_THF, THF), (L_methionyl_tRNA, N_formylmethionyl_tRNA)],
                                      minors=[h2o])

GeneAssociation(met_tRNA_formyltransferase, Gene('SP_1735'))
