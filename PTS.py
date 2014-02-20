__author__ = 'amanda'

extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

#REACTION TEMPLATE
#NAME = Reaction(name="NAME",
#                       reactants=REACT1 + REACT2,
#                       products=PROD1 + PROD2,
#                       pairs=[(pair1, pair1), (pair2, pair2)],
#                       minors=[minor1, minor2])

#GENE ASSOCIATION TEMPLATE
#GENE = Gene("GENE")
#REACTIONNAME_GA = GeneAssociation(REACTIONNAME, GENE)


phosphoenol_pyruvate = Metabolite ("PEP", kegg=C00074)
pyruvate = Metabolite ("pyruvate", kegg=C00022)
ADP = Metabolite ("ADP")
ATP = Metabolite ("ATP")

ATPgeneration = Reaction(name="ATP",
                reactants="PEP" + "ADP",
                products="pyruvate" + "ATP",
                pairs=[("PEP", "pyruvate"),("ADP","ATP")],
                minors=["PEP", "pyruvate"])

SP_1176 = Gene("SP_1176")
ATP_GA = GeneAssociation(ATP, SP_1176)


#GLUCOSE FAMILY
glucose = Metabolite("glucose", kegg=C00031)
glucose_6_phosphate = Metabolite("glucose6phosphate", kegg=C00092)

glucose_phosphorylation = Reaction(name="GP",
                        reactants="glucose" + "ATP",
                        products="glucose6phosphate" + "ADP",
                        pairs=[("glucose", "glucose6phosphate"), ("ATP", "ADP")],
                        minors=["ATP", "ADP"])

SP_0758 = Gene("SP_0758")
SP_1684 = Gene("SP_1684")
GP_GA = GeneAssociation(GP, SP_0758 & (SP_1684))

#Still don't know genes for the following:
n_acetyl_d_glucosamine = Metabolite("NADG", kegg=C00140)
n_acetyl_d_glucosamine_6_phosphate = Metabolite("NADG6P", kegg=C00357)

n_acetyl_d_glucosamine_phosphorylation = Reaction(name="NADGP",
                                                  reactants="NADG" + "ATP",
                                                  products="NADG6P" + "ADP",
                                                  pairs=[("NADG","NADG6P"), ("ATP", "ADP")],
                                                  minors=["ATP", "ADP"])

#Only know one gene for the following:
maltose = Metabolite("maltose", kegg=C00208)
maltose_6_phosphate = Metabolite("maltose6P", kegg=C05737)

maltose_phosphorylation = Reaction(name="MaP",
                                   reactants="maltose" + "ATP",
                                   products="maltose6P" + "ADP",
                                   pairs=[("maltose", "maltose6P"), ("ATP", "ADP")],
                                   minors=["ATP", "ADP"])

MaP_GA = GeneAssociation(MaP, SP_0758)

#Still don't know genes for the following:
d_glucosamine = Metabolite("DG", kegg=C00329)
d_glucosamine_6_phosphate = Metabolite("DG6P", kegg=C00352)

d_glucosamine_phosphorylation = Reaction(name="DGP",
                                         reactants="DG" + "ATP",
                                         products="DG6P" + "ADP",
                                         pairs=[("DG","DG6P"), ("ATP" + "ADP")],
                                         minors=["ATP", "ADP"])

sucrose = Metabolite("sucrose", kegg=C00089)
sucrose_6_phosphate = Metabolite("sucrose6phosphate", kegg=C16688)

sucrose_phosphorylation = Reaction(name="SP",
                        reactants="sucrose" + "ATP",
                        products="sucrose6phosphate" + "ADP",
                        pairs=[("sucrose", "sucrose6phosphate"), ("ATP", "ADP")],
                        minors=["ATP", "ADP"])
SP_1722 = Gene("SP_1722")
SP_GA = GeneAssociation(SP, SP_1722)


beta_glucosides = Metabolite("BG", kegg=C00963)
phospho_beta_glucoside = Metabolite("PBG", kegg=C01135)

beta_glucosides_phosphorylation = Reaction(name="BGP",
                                reactants="BG" + "ATP",
                                products="PBG" + "ADP",
                                pairs=[("BG", "PBG"),("ATP", "ADP")],
                                minors=["ATP","ADP"])
SP_0577 = Gene("SP_0577")
BGP_GA+ GeneAssociation(BGP, SP_0577)

#Only know one gene for the following:
arbutin = Metabolite ("arbutin", kegg=C06186)
arbutin_6_phosphate = Metabolite ("arbutin6P", kegg=C06187)

arbutin_phosphorylation = Reaction(name="ArP",
                                   reactants="arbutin" + "ATP",
                                   products="arbutin6P" + "ADP",
                                   pairs=[("arbutin", "arbutin6P"), ("ATP", "ADP")],
                                   minors=["ATP", "ADP"])
ArP_GA = GeneAssociation (ArP, SP_0758)


#Only know one gene for the following:
salicin = Metabolite("salicin", kegg=C01451)
salicin_6_phosphate = Metabolite("Sa6P", kegg=C06188)

salicin_phosphorylation = Reaction(name="SaP",
                                   reactants="salicin" + "ATP",
                                   products="Sa6P" + "ADP",
                                   pairs=[("salicin", "Sa6P"), ("ATP", "ADP")],
                                   minors=["ATP", "ADP"])

SaP_GA = GeneAssociation (SaP, SP_0758)

trehalose = Metabolite("trehalose", kegg=C01083)
trehalose_6_phosphate = Metabolite("T6P",kegg=C00689)

trehalose_phosphorylation = Reaction(name="TP",
                            reactants="trehalose" + "ATP",
                            products="T6P" + "ADP",
                            pairs=[("trehalose", "T6P"),("ATP", "ADP")],
                            minors=["ATP","ADP"])
SP_1884 = Gene("SP_1884")
SP_0758 = Gene("SP_0758")
TP_GA = GeneAssociation(TP, SP_1884 & (SP_0758))


#LACTOSE FAMILY
lactose = Metabolite("lactose", kegg=C00243)
lactose_6_phosphate = Metabolite("L6P", kegg=C05396)

lactose_phosphorylation = Reaction(name="LP",
                        reactants="lactose" + "ATP",
                        products="L6P" + "ADP",
                        pairs=[("lactose","L6P"),("ATP","ADP")],
                        minors=["ATP","ADP"])
SP_0474 = Gene("SP_0474")
SP_0478 = Gene("SP_0478")
SP_1185 = Gene("SP_1185")
SP_0476 = Gene("SP_0476")
SP_1186 = Gene("SP_1186")
LP_GA = GeneAssociation(LP, SP_0474 & (SP_0478 | SP_0476 | SP_1185 | SP_1186))

#Cellbiose pathway is incomplete on Kegg so this could be incorrect
cellobiose = Metabolite("cellobiose", kegg=C00185)
cellobiose_monophosphate = Metabolite("COM")

cellobiose_phosphorylation = Reaction(name="COP",
                                      reactants="cellobiose" + "ATP",
                                      products="COM" + "ADP",
                                      pairs=[("cellobiose", "COM"),("ATP","ADP")],
                                      minors=["ATP","ADP"])
SP_0250 = Gene("SP_0250")
SP_2022 = Gene("SP_2022")
SP_1617 = Gene("SP_1617")
SP_0249 = Gene("SP_0249")
SP_2023 = Gene("SP_2023")
SP_2024 = Gene("SP_2024")
SP_0305 = Gene("SP_0305")
COP_GA = GeneAssociation(COP, SP_0250 & (SP_2022 | SP_1617 | SP_2049 | SP_2023 | SP_2024 | SP_0305))


#FRUCTOSE FAMILY
fructose = Metabolite("fructose",kegg=C00095)
fructose_1_phosphate = Metabolite("F1P",kegg=C01094)

fructose_phosphorylation = Reaction(name="FP",
                            reactants="fructose" + "ATP",
                            products="F1P" + "ADP",
                            pairs=[("fructose","F1P"),("ATP", "ADP")],
                            minors=["ATP", "ADP"])
SP_0877 = Gene("SP_0877")
SP_1617 = Gene("SP_1617")
SP_1618 = Gene("SP_1618")
SP_1619 = Gene("SP_1619")
FP_GA = GeneAssociation(FP, SP_0877 & (SP_1617 | SP_1618 | SP_1619))

mannitol = Metabolite("mannitol",kegg=C00392)
mannitol_1_phosphate = Metabolite("M1P",kegg=C00644)

mannitol_phosphorylation = Reaction(name="MP",
                            reactants="mannitol" + "ATP",
                            products="M1P" + "ADP",
                            pairs=[("mannitol", "MP"),("ATP", "ADP")],
                            minors=["ATP", "ADP"])
SP_0394 = Gene("SP_0394")
SP_0396 = Gene("SP_0396")
MP_GA = GeneAssociation(MP, SP_0394 & (SP_0396))

#MANNOSE FAMILY

mannose = Metabolite("mannose", kegg=C00159)
mannose_6_phosphate = Metabolite("M6P", kegg=C00275)

mannose_phosphorylation = Reaction(name="M2P",
                                   reactants="mannose" + "ATP",
                                   products="M6P" + "ADP",
                                   pairs=[("mannose", "M2P"),("ATP", "ADP")],
                                   minors=["ATP", "ADP"])
SP_0062 = Gene("SP_0062")
SP_0283 = Gene("SP_0283")
SP_2162 = Gene("SP_2162")
SP_0063 = Gene("SP_0063")
SP_0282 = Gene("SP_0282")
SP_2161 = Gene("SP_2161")
SP_0061 = Gene("SP_0061")
SP_0064 = Gene("SP_0064")
SP_0284 = Gene("SP_0284")
SP_2163 = Gene("SP_2163")
SP_2164 = Gene("SP_2164")
M2P_GA = GeneAssociation(M2P, SP_0062 & (SP_0283 | SP_2162 | SP_0063 | SP_0282 | SP_2161 | SP_0061 | SP_0064 | SP_0284
                                         | SP_2163 | SP_2164))

n_acetyl_galactosamine = Metabolite("NAG", kegg=C01132)
n_acetyl_galactosamine_6_phosphate = Metabolite("NAG6P", kegg=C06376)

n_acetyl_galactosamine_phosphorylation = Reaction(name="NAGP",
                                                  reactants="NAG" + "ATP",
                                                  products="NAG6P" + "ADP",
                                                  pairs=[("NAG" + "NAG6P"),("ATP", "ADP")],
                                                  minors=["ATP", "ADP"])
SP_0324 = Gene("SP_0324")
SP_0325 = Gene("SP_0325")
SP_0321 = Gene("SP_0321")
SP_0323 = Gene("SP_0323")
NAGP_GA = GeneAssociation(NAGP, SP_0324 & (SP_0325 | SP_0321 | SP_0323))

#OTHER FAMILY
galactitol = Metabolite("galactitol", kegg=C01697)
galactitol_1_phosphate = Metabolite("G1P", kegg=C06311)

galactitol_phosphorylation = Reaction(name="G2P",
                                      reactants="galactitol" + "ATP",
                                      products="G1P" + "ADP",
                                      pairs=[("galactitol", "G1P"),("ATP", "ADP")],
                                      minors=["ATP", "ADP"])
SP_0647 = Gene("SP_0647")
SP_0645 = Gene("SP_0645")
SP_1198 = Gene("SP_1198")
SP_0646 = Gene("SP_0646")
SP_1197 = Gene("SP_1197")
G2P_GA = GeneAssociation(G2P, SP_0647 & (SP_0645 | SP_1198 | SP_0646 | SP_1197))

l_ascorbate = Metabolite("LA", kegg=C00072)
l_ascorbate_6_phosphate = Metabolute("LA6P", kegg=C16186)

l_ascorbate_phosphorylation = Reaction(name="LAP",
                                       reactants="LA" + "ATP",
                                       products="LA6P" + "ADP",
                                       pairs=[("LA", "LA6P"),("ATP","ADP")],
                                       minors=["ATP", "ADP"])
SP_2038 = Gene("SP_2038")
SP_2129 = Gene("SP_2129")
SP_2036 = Gene("SP_2036")
SP_2037 = Gene("SP_2037")
SP_2130 = Gene("SP_2130")
LAP_GA = GeneAssociation(LAP, SP_2038 & (SP_2129 | SP_2036 | SP_2037 | SP_2130))

#NITROGEN REGULATION


