#Shikimate pathway:

#reaction1:
E4P = Metabolite ("D_erythrose_4_phosphate", kegg=C00279)
PEP = Metabolite("phosphoenolpyruvate", kegg=C00074)
H2O = Metabolite("H2O", kegg=C00001)
DAHP = Metabolite ("7_phosphate_2_dehydro_3_deoxy_D_arabinoheptonate",kegg=C04691)
Pi = Metabolite("phosphate",kegg=C00009)

DAHP_synthesis = Reaction(name="DAHP_syn",
                                reactants="E4P" + "PEP" + "H2O",
                                products="DAHP" + "Pi",
                                pairs = [("E4P","DAHP")],
                                minors=["PEP", "Pi", "H2O"],
                                reversible = False)
SP_1700 = Gene("SP_1700")
SP_1701 = Gene("SP_1701")
GeneAssociation(DAHP_syn, SP_1700 & (SP_1701))

#reaction2; SP_1375(aroB)
m3_DHQ = Metabolite("3_dehydroquinate", kegg=C00944)

m3_dehydroquinate_synthesis = Reaction(name="3-DHQ_syn",
                                reactants="DAHP",
                                products="m3_DHQ","Pi",
                                majors=[("DAHP","m3_DHQ")],
                                minors=["Pi"],
                                reversible = False)
SP_1375 = Gene("SP_1375")
GeneAssociation(3-DHQ_syn, SP_1375)

#reaction3; SP_1377(aroD)
m3_DHS = Metabolite("3_dehydroshikimate", kegg=C02637)

m3_dehydroshikimate_synthesis = Reaction(name="m3_DHS_syn",
                                reactants="m3_DHQ",
                                products="m3_DHS","H2O",
                                majors=["m3_DHQ","m3_DHS"],
                                minors=["H2O"],
                                reversible = True)
SP_1377 = Gene("SP_1377")
GeneAssociation(m3_DHS_syn, SP_1377)

#reaction4;SP_1376(aroE), how to express NAD+ vs NADPH in different directions
SKM = Metabolite("shikimate",kegg=C00493)
NADPH = Metabolite("NADPH",kegg=C00005)
H = Metabolite ("H+",kegg=C00080)
NADP = Metabolite ("NADP+", kegg=C00006)

shikimate_synthesis = Reaction(name="SKM_syn",
                                reactants = "m3_DHS","NADPH","H",
                                products = "SKM","NADP",
                                majors=["m3_DHS","SKM"],
                                minors=["NADPH","NADP","H"],
                                reversible = True)
SP_1376 = Gene("SP_1376")
GeneAssociation(SKM_syn, SP_1376)

#reaction5
SKM3P = Metabolite("3_phosphoshikimate",kegg=C03175)
ATP = Metabolite("ATP",kegg=C00002)
ADP = Metabolite("ADP",kegg=C00008)

Shikimate_phosphorylation = Reaction(name="SKM_P",
                                reactants = "SKM","ATP",
                                products = "SKM3P","ADP",
                                majors=["SKM","SKM3P"],
                                minors=["ATP","ADP"],
                                reversible = False)
SP_1370 = Gene("SP_1370")
GeneAssociation(SKM_P, SP_1370)

#Reaction6
EPSP = Metabolite("5_O_(1_Carboxyvinyl)_3_phosphoshikimate", kegg=C01269)
PEP = Metabolite("phosphoenolpyruvate", kegg=C00074)
Pi = Metabolite("Phosphate",kegg=C00009)

EPSP_synthesis = Reaction(name="EPSP_syn",
                                reactants = "SKM3P","PEP",
                                products = "EPSP","Pi",
                                majors=["SKM3P","EPSP"],
                                minors=["PEP","Pi"],
                                reversible = True)
SP_1371 = Gene("SP_1371")
GeneAssociation(EPSP_syn, SP_1371)

#Reaction7
CRM = Metabolite ("chorismate",kegg=C00251)
Pi = Metabolite("Phosphate",kegg=C00009)
EPSP = Metabolite("5_O_(1_Carboxyvinyl)_3_phosphoshikimate", kegg=C01269)

Chorismate_formation = Reaction(name="CRM_syn",
                                reactants = "EPSP",
                                products = "CRM","Pi",
                                majors=["EPSP","CRM"],
                                minors=["Pi"],
                                reversible = False)
SP_1374 = Gene("SP_1374")
GeneAssociation(CRM_syn, SP_1374)

#Reaction8 to Reaction12: Tryptophan biosynthesis
ANTL = Metabolite ("anthranilate",kegg=C00108)
L_Q = Metabolite ("L_Glutamine",kegg=C00064)
L-E = Metabolite ("L_Glutamate",kegg=C00025)
pyr = Metabolite ("pyruvate",kegg=C00022)

Anthranilate_formation = Reaction(name="ATNL_syn",
                                reactants = "CRM","L_Q",
                                products = "ATNL","L_E","pyr",
                                majors = ["CRM","ATNL"],
                                minors = ["L_Q","L_E","pyr"],
                                reversible = False)
SP_1817 = Gene("SP_1817")
SP_1818 = Gene("SP_1818")
GeneAssociation(ATNL_syn, SP_1817 &(SP_1818))

#Reaction9
ANTL = Metabolite ("anthranilate",kegg=C00108)
N5PRATNL= Metabolite ("N_5_phospho_D_ribosyl_anthranilate",kegg=C04302)
PRPP = Metabolite("5_phospho_alpha_D_ribose_1_diphosphate",kegg=C00119)
PPi = Metabolite ("diphosphate",kegg=C00013)

N_5_phospho_D_ribosyl_anthranilate_formation = Reaction(name="N5PRATNL_syn",
                                reactants = "ATNL","PRPP",
                                products = "N5PRATNL","PPi",
                                majors=["ATNL","N5PRATNL"],
                                minors=["PRPP","PPi"],
                                reversible = True)
SP_1815 = Gene("SP_1815")
GeneAssociation(N5PRATNL_syn,SP_1815)

#Reaction10
CarboxyphenylaminoR5P = Metabolite ("1_(2_Carboxyphenylamino)_1_deoxy_D_ribulose_5_phosphate", kegg=C01302)

CarboxyphenylaminoR5P_formation = Reaction(name="CarboxyphenylaminoR5P_syn",
                                reactants = "N5PRATNL",
                                products = "CarboxyphenylaminoR5P",
                                majors = ["N5PRATNL", "CarboxyphenylaminoR5P"],
                                reversible = True)
SP_1813 = Gene("SP_1813")
GeneAssociation(CarboxyphenylaminoR5P_syn,SP_1813)

#Reaction11
IGPS = Metabolite ("3_indonyl_glycerolphosphate")
CO2 = Metabolite ("Carbon dioxide", kegg=C00011)

m3_indonyl_glycerolphosphate_formation = Reaction ("IGPS_syn",
                                reactants = "CarboxyphenylaminoR5P",
                                products = "IGPS", "CO2", "H2O",
                                majors = ["CarboxyphenylaminoR5P", "IGPS"],
                                minors = ["CO2", "H2O"],
                                reversible = True)
SP_1814 = Gene("SP_1814")
GeneAssociation(IGPS_syn,SP_1814)

#Reaction12
Indole = Metabolite ("indole", kegg=C00463)
G3P = Metabolite ("D_glyceraldehyde_3_phosphatre", kegg=C00118)

Indole_formation = Reaction ("Indole_syn",
                                reactants = "IGPS",
                                products = "Indole", "G3P",
                                majors = ["IGPS","Indole"],
                                minors = ["G3P"])
SP_1811 = Gene ("SP_1811")
SP_1812 = Gene ("SP_1812")
GeneAssociation(Indole_syn,SP_1811 & (SP_1812))


L_S = Metabolite ("L_Serine", kegg=C00065)
L_W = Metabolite ("L_Tryptophan", kegg=C00078)
Tryptophan_formation = Reaction ("Trp_syn",
                                reactants = "L_S", "Indole",
                                products = "L_W", "H2O",
                                majors = ["L_S", "Indole", "L_W"],
                                minors = ["L_W"],
                                reversible = False)
SP_1811 = Gene ("SP_1811")
SP_1812 = Gene ("SP_1812")
GeneAssociation(Trp_syn,SP_1811 & (SP_1812))

#Reaction 13 first reaction committed to Tyrosine and Phenylalanine synthesis
PPN = Metabolite ("prephenate", kegg=C00254)

Prephenate_formation = Reaction ("PPN_syn",
                                reactants = "CRM",
                                products = "PPN",
                                majors = ["CRM", "PPN"],
                                reversible = True)
SP_1296 = Gene ("SP_1296")
GeneAssociation(PPN_syn, SP_1296)

#Reaction 14 Tyrosine synthesis
HPPD = Metabolite ("4_hydroxyphenylpyruvate", kegg=C01179)
NAD = Metabolite ("NAD", kegg=C00003)
NADH = Metabolite ("NADH", kegg=C00004)

m4_hydroxyphenylpyruvate_formation = Reaction ("HPPD_syn",
                                reactants = "PPN", "NAD+",
                                products = "HPPD", "NADH", "H", "CO2",
                                majors = ["PPN", "HPPD"],
                                minors = ["NAD+", "NADH", "CO2", "H+"],
                                reversible = True)
SP_1373 = Gene ("SP_1373")
GeneAssociation(HPPD_syn, SP_1373)

#Reaction 14 Tyrosine synthesis step only annotated in Biocyc
L_Y = Metabolite ("L_Tyrosine", kegg=C00082)
oxoglutarate = Metabolite ("2_oxoglutarate", kegg=C00026)

tyrosine_formation = Reaction ("try_syn",
                                reactants = "HPPD", "L_E",
                                products = "L_Y", "oxoglutarate",
                                majors = ["HPPD", "L_Y"],
                                minors = ["L_E", "oxoglutarate"],
                                reversible = True)
SP_0035 = Gene ("SP_0035")
GeneAssociation(try_syn, SP_0035)

#Reaction 15 Phenylalanine synthesis_1
phenylpyr = Metabolite ("phenylpyruvate", kegg=C00166)

phenylpyruvate_formation = Reaction ("phenylpyr_syn",
                                reactants = "PPN",
                                products = "phenylpyr", "CO2", "H2O",
                                majors = ["PPN", "phenylpyr"],
                                minors = ["CO2", "H2O"],
                                reversible = True)
SP_1369 = Gene ("SP_1369")
GeneAssociation(phenylpyr_syn, SP_1369)

#Reaction 16 Phenylalanine synthesis_1
L_F = Metabolite ("L_Phenylalanine", kegg=C0079)

phenylalanine_formation = Reaction ("phe_syn",
                                reactants = "PPN", "L_E",
                                products = "L_F", "oxoglutarate",
                                majors = ["PPN", "L_F"],
                                minors = ["L_E", "oxoglutarate"],
                                reversible = True)
SP_0035 = Gene ("SP_0035")
GeneAssociation(phe_syn, SP_0035)

