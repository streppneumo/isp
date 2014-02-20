__author__ = 'Corey'

from CellScribe import *

extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp", kegg="C00002")
amp = Metabolite("amp", kegg="C00020")


def charge_trna(reactionkegg, aaname, aakegg, trnaname, trnakegg, chargedrna_name, chargedkegg, associated_genes):

    trna = RNA(trnaname, kegg=trnakegg)
    amino_acid = Metabolite(aaname, kegg=aakegg)
    charged_trna = Metabolite(chargedrna_name, kegg=chargedkegg)

    charge_rxn = Reaction(name='charge' + aaname,
                          reactants=trna + amino_acid + atp,
                          products=charged_trna + amp,
                          pairs=[(trna, charged_trna), (atp, amp)],
                          minors=[atp, amp],
                          kegg=reactionkegg)

    GeneAssociation(charge_rxn, associated_genes)

charge_trna("R03665", "L_valine", "C00183", "tRNA_val", "C01653", "L_valyl_tRNA", "C02554", Gene('SP_0568'))
charge_trna("R03657", "L_leucine", "C00123", "tRNA_leu", "C01645", "L_leucyl_tRNA", "C02047", Gene('SP_0254'))
charge_trna("R03656", "L_isoleucine", "C00407", "tRNA_ile", "C01644", "L_isoleucyl_tRNA", "C03127", Gene('SP_1659'))
charge_trna("R03658", "L_lysine", "C00047", "tRNA_lys", "C01646", "L_lysyl_tRNA", "C01931", Gene('SP_0713'))
charge_trna("R03646", "L_arginine", "C00062", "tRNA_arg", "C01636", "L_arginyl_tRNA", "C02163", Gene('SP_2078'))
charge_trna("R03661", "L_proline", "C00148", "tRNA_pro", "C01649", "L_prolyl_tRNA", "C02702", Gene('SP_0264'))
charge_trna("R03655", "L_histidine", "C00135", "tRNA_his", "C01643", "L_histidyl_tRNA", "C02988", Gene('SP_2121'))
charge_trna("R03660", "L_phenylalanine", "C00079", "tRNA_phe", "C01648", "L_phenylalanyl_tRNA", "C03511", Gene('SP_0581')
            & Gene('SP_0579'))
charge_trna("R02918", "L_tyrosine", "C00082", "tRNA_tyr", "C00787", "L_tyrosyl_tRNA", "C02839", Gene('SP_2100'))
charge_trna("R03664", "L_tryptophan", "C00078", "tRNA_trp", "C01652", "L_tryptophanyl_tRNA", "C03512", Gene('SP_2229'))
charge_trna("R03038", "L_alanine", "C00041", "tRNA_ala", "C01635", "L_alanyl_tRNA", "C00886", Gene('SP_1383'))
charge_trna("R03654", "L_glycine", "C00037", "tRNA_gly", "C01642", "L_glycyl_tRNA", "C02412", Gene('SP_1474')
            & Gene('SP_1475'))
charge_trna("R03663", "L_threonine", "C00188", "tRNA_thr", "C01651", "L_threonyl_tRNA", "C02992", Gene('1631'))
charge_trna("R03662", "L_serine", "C00065", "tRNA_ser", "C01650", "L_seryl_tRNA", "C02553", Gene('SP_0411'))
charge_trna("R03659", "L_methionine", "C00073", "tRNA_met", "C01647", "L_methionyl_tRNA", "C02430", Gene('SP_0788'))
charge_trna("R03650", "L_cysteine", "C00097", "tRNA_cys", "C01639", "L_cysteinyl_tRNA", "C03125", Gene('SP_0591'))
charge_trna("R03648", "L_asparagine", "C00152", "tRNA_asn", "C01637", "L_asparaginyl_tRNA", "C03402", Gene("SP_1542"))

# L_glutamyl_tRNA from glutamate and tRNA_gln. get to L_glutaminyl_tRNA through SP_0436, SP_0437, SP_0438
charge_trna("R03651", "L_glutamate", "C00025", "tRNA_gln", "C01640", "L_glutamyl_tRNA", "C06112", Gene('SP_2069'))

# L_asparginyl_tRNA from aspartate and tRNA_asn. 

# make N_formyl_methionyl_tRNA
ten_formyl_THF = Metabolite("ten_formyl_THF", kegg="C00234")
L_methionyl_tRNA = Metabolite("L_methionyl_tRNA", kegg="C02430")
THF = Metabolite("THF", kegg="C00101")
N_formylmethionyl_tRNA = Metabolite("N_formylmethionyl_tRNA", kegg="C03294")
h2o = Metabolite("h2o", kegg="C00001")

met_tRNA_formyltransferase = Reaction(name='met_tRNA_formyltransferase',
                                      reactants=h2o + ten_formyl_THF + L_methionyl_tRNA,
                                      products=THF + N_formylmethionyl_tRNA,
                                      pairs=[(ten_formyl_THF, THF), (L_methionyl_tRNA, N_formylmethionyl_tRNA)],
                                      minors=[h2o],
                                      kegg="R03940")

GeneAssociation(met_tRNA_formyltransferase, Gene('SP_1735'))
