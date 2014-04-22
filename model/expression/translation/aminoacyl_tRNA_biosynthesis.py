from CellScribe import *
from model.metabolites import *
from model.genes import (SP_0568, SP_0254, SP_1659, SP_0713, SP_2078, SP_0264, SP_2121, SP_0581, SP_0579, SP_2100,
                         SP_2229, SP_1383, SP_1474, SP_1475, SP_1631, SP_0411, SP_0788, SP_0591, SP_1542, SP_2114,
                         SP_2069, SP_1735, SP_0436, SP_0437, SP_0438)


def charge_trna(reactionkegg, amino_acid, trnaname, trnakegg, chargedrna_name, chargedkegg, associated_genes):
    trna = RNA(trnaname, kegg=trnakegg)

    charged_trna = Metabolite(chargedrna_name, kegg=chargedkegg)

    charge_rxn = Reaction(name='charge' + amino_acid.name + reactionkegg,  # probably cold name these better..?
                          reactants=trna + amino_acid + atp,
                          products=charged_trna + amp + diphosphate,
                          pairs=[(trna, charged_trna), (atp, amp)],
                          minors=[atp, amp],
                          kegg=reactionkegg)

    GeneAssociation(charge_rxn, associated_genes)

charge_trna("R03665", l_valine, "tRNA_val", "C01653", "L_valyl_tRNA(val)", "C02554", SP_0568)
charge_trna("R03657", l_leucine, "tRNA_leu", "C01645", "L_leucyl_tRNA(leu)", "C02047", SP_0254)
charge_trna("R03656", l_isoleucine, "tRNA_ile", "C01644", "L_isoleucyl_tRNA(ile)", "C03127", SP_1659)
charge_trna("R03658", l_lysine, "tRNA_lys", "C01646", "L_lysyl_tRNA(lys)", "C01931", SP_0713)
charge_trna("R03646", l_arginine, "tRNA_arg", "C01636", "L_arginyl_tRNA(arg)", "C02163", SP_2078)
charge_trna("R03661", l_proline, "tRNA_pro", "C01649", "L_prolyl_tRNA(pro)", "C02702", SP_0264)
charge_trna("R03655", l_histidine, "tRNA_his", "C01643", "L_histidyl_tRNA(his)", "C02988", SP_2121)
charge_trna("R03660", l_phenylalanine, "tRNA_phe", "C01648", "L_phenylalanyl_tRNA(phe)", "C03511", SP_0581 & SP_0579)
charge_trna("R02918", l_tyrosine, "tRNA_tyr", "C00787", "L_tyrosyl_tRNA(tyr)", "C02839", SP_2100)
charge_trna("R03664", l_tryptophan, "tRNA_trp", "C01652", "L_tryptophanyl_tRNA(trp)", "C03512", SP_2229)
charge_trna("R03038", l_alanine, "tRNA_ala", "C01635", "L_alanyl_tRNA(ala)", "C00886", SP_1383)
charge_trna("R03654", l_glycine, "tRNA_gly", "C01642", "L_glycyl_tRNA(gly)", "C02412", SP_1474 & SP_1475)
charge_trna("R03663", l_threonine, "tRNA_thr", "C01651", "L_threonyl_tRNA(thr)", "C02992", SP_1631)
charge_trna("R03662", l_serine, "tRNA_ser", "C01650", "L_seryl_tRNA(ser)", "C02553", SP_0411)
charge_trna("R03659", l_methionine, "tRNA_met", "C01647", "L_methionyl_tRNA(met)", "C02430", SP_0788)
charge_trna("R03650", l_cysteine, "tRNA_cys", "C01639", "L_cysteinyl_tRNA(cys)", "C03125", SP_0591)
charge_trna("R03648", l_asparagine, "tRNA_asn", "C01637", "L_asparaginyl_tRNA(asn)", "C03402", SP_1542)
charge_trna("R05578", l_glutamate, "tRNA_glu", "C01641", "L_glutamyl_tRNA(glu)", "C02987", SP_2069)
charge_trna("R05577", l_aspartate, "tRNA_asp", "C01638", "L_aspartyl_tRNA(asp)", "C02984", SP_2114)

# L_glutamyl_tRNA from glutamate and tRNA_gln. get to L_glutaminyl_tRNA through SP_0436, SP_0437, SP_0438
#charge_trna("R03651", l_glutamate, "tRNA_gln", "C01640", "L_glutamyl_tRNA(gln)", "C06112", SP_2069)
#convert = Reaction(name='L_glutamine_amido_ligase',
#                   reactants=Metabolite("L_glutamyl_tRNA(gln)", kegg="C06112") + h2o + atp + l_glutamine,
#                   products=Metabolite("L_glutaminyl_tRNA(gln)", kegg="C02282") + l_glutamate + phosphate + adp,
#                   pairs=[(atp, adp)],
#                   minors=[h2o, atp, adp],
#                   kegg="R03905")
#GeneAssociation(convert, SP_0436 & SP_0437 & SP_0438)

# make N_formyl_methionyl_tRNA
ten_formyl_THF = Metabolite("ten_formyl_THF", kegg="C00234")
L_methionyl_tRNA = Metabolite("L_methionyl_tRNA", kegg="C02430")
THF = Metabolite("THF", kegg="C00101")
N_formylmethionyl_tRNA = Metabolite("N_formylmethionyl_tRNA", kegg="C03294")

met_tRNA_formyltransferase = Reaction(name='met_tRNA_formyltransferase',
                                      reactants=h2o + ten_formyl_THF + L_methionyl_tRNA,
                                      products=THF + N_formylmethionyl_tRNA,
                                      pairs=[(ten_formyl_THF, THF), (L_methionyl_tRNA, N_formylmethionyl_tRNA)],
                                      minors=[h2o],
                                      kegg="R03940")

GeneAssociation(met_tRNA_formyltransferase, SP_1735)
