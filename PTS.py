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
glucose = Metabolite  ("glucose", kegg=C00031)
glucose_6_phosphate = Metabolite ("glucose6phosphate", kegg=C00092)

glucose_phosphorylation = Reaction(name="GP",
                        reactants="glucose" + "ATP",
                        products="glucose6phosphate" + "ADP",
                        pairs=[("glucose", "glucose6phosphate"), ("ATP", "ADP")],
                        minors=["ATP", "ADP"])

SP_0758 = Gene("SP_0758")
SP_1684 = Gene("SP_1684")
GP_GA = GeneAssociation(GP, SP_0758 & (SP_1684))


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
                                products = "PBG" + "ADP",
                                pairs=[("BG", "PBG"),("ATP", "ADP")],
                                minors=["ATP","ADP"])
SP_0577 = Gene("SP_0577")
BGP_GA+ GeneAssociation(BGP, SP_0577)


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




#OTHER FAMILY



#NITROGEN REGULATION


