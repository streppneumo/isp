__author__ = 'amanda'


#FOR GITHUB CLICK REPOSITORY FROM TOP BAR THEN 'PULL' THEN COMMIT N SYNC!

from CellScribe.main import *
from model.genes import *
from model.metabolites import *
from model.compartments import *
from model.operons import *

phosphoenol_pyruvate = Metabolite ("PEP", kegg=C00074)
pyruvate = Metabolite ("pyruvate", kegg=C00022)
phosphoenol_group = Metabolite("PG")

Pyr_Generation = Reaction(name="PYRG",
                reactants=phosphoenol_pyruvate,
                products=pyruvate + phosphoenol_group,
                pairs=[(phosphoenol_pyruvate, pyruvate),],
                minors=[phosphoenol_group])

GeneAssociation(PYRG_rxn, SP_1176)

Modification (SP_1176, phosphoenol_group, modification="phosphorylation")
phosphorylates(phosphoenol_group, SP_1176)
ModifiedProtein(SP_1176, modification="phosphorylation")

Modification (SP_1177, SP_1176, modification="phosphorylation")
phosphorylates(SP_1176, SP_1177)
ModifiedProtein(SP_1177, modification="phosphorylation")

#GLUCOSE FAMILY
glucose = Metabolite("glucose", kegg=C00031)
glucose_6_phosphate = Metabolite("glucose6phosphate", kegg=C00092)

glucose_phosphorylation = Reaction(name="GP",
                        reactants=glucose + phosphoenol_group,
                        products=glucose_6_phosphate,
                        pairs=[(glucose, glucose_6_phosphate)],
                        minors=[phosphoenol_group])

GeneAssociation(GP_rxn, SP_0758 & (SP_1684))

gluOperon = Operon(SP_0758, SP_1684)

Modification (SP_0758, phospho(SP_1177), modification="phosphorylation")
phosphorylates(phospho(SP_1177), SP_0758)
ModifiedProtein(SP_0758, modification="phosphorylation")

#Still don't know genes for the following:
n_acetyl_d_glucosamine = Metabolite("NADG", kegg=C00140)
n_acetyl_d_glucosamine_6_phosphate = Metabolite("NADG6P", kegg=C00357)

n_acetyl_d_glucosamine_phosphorylation = Reaction(name="NADGP",
                                                  reactants=n_acetyl_d_glucosamine + phosphoenol_group,
                                                  products=n_acetyl_d_glucosamine_6_phosphate,
                                                  pairs=[(n_acetyl_d_glucosamine, n_acetyl_d_glucosamine_6_phosphate)],
                                                  minors=[phosphoenol_group])

#Only know one gene for the following:
maltose = Metabolite("maltose", kegg=C00208)
maltose_6_phosphate = Metabolite("maltose6P", kegg=C05737)

maltose_phosphorylation = Reaction(name="MaP",
                                   reactants=maltose + phosphoenol_group,
                                   products=maltose_6_phosphate,
                                   pairs=[(maltose, maltose_6_phosphate)],
                                   minors=[phosphoenol_group])

GeneAssociation(MaP_rxn, SP_0758)



#Still don't know genes for the following:
d_glucosamine = Metabolite("DG", kegg=C00329)
d_glucosamine_6_phosphate = Metabolite("DG6P", kegg=C00352)

d_glucosamine_phosphorylation = Reaction(name="DGP",
                                         reactants=d_glucosaminate + phosphoenol_group,
                                         products=d_glucosaminate_6_phosphate,
                                         pairs=[(d_glucosaminate, d_glucosaminate_6_phosphate)],
                                         minors=[phosphoenol_group])

sucrose = Metabolite("sucrose", kegg=C00089)
sucrose_6_phosphate = Metabolite("sucrose6phosphate", kegg=C16688)

sucrose_phosphorylation = Reaction(name="SP",
                        reactants=sucrose + phosphoenol_group,
                        products=sucrose_6_phosphate,
                        pairs=[(sucrose, sucrose_6_phosphate)],
                        minors=[phosphoenol_group])
GeneAssociation(SP, SP_1722)


Modification (SP_1722, phospho(SP_1177), modification="phosphorylation")
phosphorylates(phospho(SP_1177), SP_1722)
ModifiedProtein(SP_1722, modification="phosphorylation")


beta_glucosides = Metabolite("BG", kegg=C00963)
phospho_beta_glucoside = Metabolite("PBG", kegg=C01135)

beta_glucosides_phosphorylation = Reaction(name="BGP",
                                reactants=beta_glucosides + phosphoenol_group,
                                products=phospho_beta_glucoside,
                                pairs=[(beta_glucosides, phospho_beta_glucoside)],
                                minors=[phosphoenol_group])
GeneAssociation(BGP, SP_0577)

Modification (SP_0577, phospho(SP_1177), modification="phosphorylation")
phosphorylates(phospho(SP_1177), SP_0577)
ModifiedProtein(SP_0577, modification="phosphorylation")

#Only know one gene for the following:
arbutin = Metabolite ("arbutin", kegg=C06186)
arbutin_6_phosphate = Metabolite ("arbutin6P", kegg=C06187)

arbutin_phosphorylation = Reaction(name="ArP",
                                   reactants=arbutin + phosphoenol_group,
                                   products=arbutin_6_phosphate,
                                   pairs=[(arbutin, arbutin_6_phosphate)],
                                   minors=[phosphoenol_group])
GeneAssociation (ArP, SP_0758)
ArPOperon = Operon(SP_0758)

#Only know one gene for the following:
salicin = Metabolite("salicin", kegg=C01451)
salicin_6_phosphate = Metabolite("Sa6P", kegg=C06188)

salicin_phosphorylation = Reaction(name="SaP",
                                   reactants=salicin + phosphoenol_group,
                                   products=salicin_6_phosphate,
                                   pairs=[(salicin, salicin_6_phosphate)],
                                   minors=[phosphoenol_group])

GeneAssociation (SaP, SP_0758)

trehalose = Metabolite("trehalose", kegg=C01083)
trehalose_6_phosphate = Metabolite("T6P",kegg=C00689)

trehalose_phosphorylation = Reaction(name="TP",
                            reactants=trehalose + phosphoenol_group,
                            products=trehalose_6_phosphate,
                            pairs=[(trehalose, trehalose_6_phosphate)],
                            minors=[phosphoenol_group])

GeneAssociation(TP, SP_1884 & (SP_0758))

#Only know one gene for the following:
N_acetylmuramic_acid = Metabolite("NAMA", kegg=C02713)
N_acetylmuramic_acid_6_phosphate = Metabolite("NAMA6P", kegg=C16698)

N_acetylmuramic_acid_phosphorylation = Reaction(name="NAMAP",
                                                reactants=N_acetylmuramic_acid + phosphoenol_group,
                                                products=N_acetylmuramic_acid_6_phosphate,
                                                pairs=[(N_acetylmuramic_acid, N_acetylmuramic_acid_6_phosphate)],
                                                minors=[phosphoenol_group])

GeneAssociation(NAMAP, SP_0758)


#LACTOSE FAMILY
lactose = Metabolite("lactose", kegg=C00243)
lactose_6_phosphate = Metabolite("L6P", kegg=C05396)

lactose_phosphorylation = Reaction(name="LP",
                        reactants=lactose + phosphoenol_group,
                        products=lactose_6_phosphate,
                        pairs=[(lactose, lactose_6_phosphate)],
                        minors=[phosphoenol_group])

GeneAssociation(LP, SP_0474 & (SP_0478 | SP_0476 | SP_1185 | SP_1186))


#Cellbiose pathway is incomplete on Kegg so this could be incorrect
cellobiose = Metabolite("cellobiose", kegg=C00185)
cellobiose_monophosphate = Metabolite("COM")

cellobiose_phosphorylation = Reaction(name="COP",
                                      reactants=cellobiose + phosphoenol_group,
                                      products=cellobiose_monophosphate,
                                      pairs=[(cellobiose, cellobiose_monophosphate)],
                                      minors=[phosphoenol_group])

GeneAssociation(COP, SP_0250 & (SP_2022 | SP_1617 | SP_2049 | SP_2023 | SP_2024 | SP_0305))


#FRUCTOSE FAMILY
fructose = Metabolite("fructose",kegg=C00095)
fructose_1_phosphate = Metabolite("F1P",kegg=C01094)

fructose_phosphorylation = Reaction(name="FP",
                            reactants=fructose + phosphoenol_group,
                            products=fructose_1_phosphate,
                            pairs=[(fructose, fructose_1_phosphate)],
                            minors=[phosphoenol_group])

GeneAssociation(FP, SP_0877 & [SP_1617 | SP_1618 | SP_1619])


mannitol = Metabolite("mannitol",kegg=C00392)
mannitol_1_phosphate = Metabolite("M1P",kegg=C00644)

mannitol_phosphorylation = Reaction(name="MP",
                            reactants=mannitol + phosphoenol_group,
                            products=mannitol_1_phosphate,
                            pairs=[(mannitol, mannitol_1_phosphate)],
                            minors=[phosphoenol_group])

GeneAssociation(MP, SP_0394 & (SP_0396))

#Incomplete pathway; no genes:
two_o_alpha_mannosyl_D_glycerate = Metabolite("2OAMDG", kegg=C11544)
two_o_6_phospho_alpha_mannosyl_D_glycerate = Metabolite("2O6PAMDG", kegg=C16699)

two_o_alpha_mannosyl_D_glycerate_phosphorylation = Reaction(name="2OAMDGP",
                                                            reactants= two_o_alpha_mannosyl_D_glycerate
                                                                       + phosphoenol_group,
                                                            products= two_o_6_phospho_alpha_mannosyl_D_glycerate,
                                                            pairs=[(two_o_alpha_mannosyl_D_glycerate,
                                                                    two_o_6_phospho_alpha_mannosyl_D_glycerate)],
                                                            minors=[phosphoenol_group])

#MANNOSE FAMILY

mannose = Metabolite("mannose", kegg=C00159)
mannose_6_phosphate = Metabolite("M6P", kegg=C00275)

mannose_phosphorylation = Reaction(name="M2P",
                                   reactants=mannose + phosphoenol_group,
                                   products=mannose_6_phosphate,
                                   pairs=[(mannose, mannose_6_phosphate)],
                                   minors=[phosphoenol_group])

GeneAssociation(M2P, SP_0062 & (SP_0283 | SP_2162 | SP_0063 | SP_0282 | SP_2161 | SP_0061 | SP_0064 | SP_0284
                                         | SP_2163 | SP_2164))

#Incomplete pathway; no genes:
sorbose = Metabolite("sorbose", kegg=C01452)
sorbose_1_phosphate = Metabolite("S1P", kegg=C02888)

sorbose_phosphorylation = Reaction(name="S2P",
                                   reactants= sorbose + phosphoenol_group,
                                   products=sorbose_1_phosphate,
                                   pairs=[(sorbose, sorbose_1_phosphate)],
                                   minors=[phosphoenol_group])

n_acetyl_galactosamine = Metabolite("NAG", kegg=C01132)
n_acetyl_galactosamine_6_phosphate = Metabolite("NAG6P", kegg=C06376)

n_acetyl_galactosamine_phosphorylation = Reaction(name="NAGP",
                                                  reactants=n_acetyl_galactosamine + phosphoenol_group,
                                                  products=n_acetyl_galactosamine_6_phosphate,
                                                  pairs=[(n_acetyl_galactosamine + n_acetyl_galactosamine_6_phosphate)],
                                                  minors=[phosphoenol_group])

GeneAssociation(NAGP, SP_0324 & (SP_0325 | SP_0321 | SP_0323))

#Only know one gene from the following:
galactosamine = Metabolite("galactosamine", kegg=C02262)
galactosamine_6_phospate = Metabolite("Ga6P", kegg=C06377)

galactosamine_phosphorylation = Reaction(name="Ga2P",
                                         reactants=galactosamine + phosphoenol_group,
                                         products=galactosamine_6_phospate,
                                         pairs=[(galactosamine, galactosamine_6_phospate)],
                                         minors=[phosphoenol_group])

GeneAssociation(Ga2P, SP_0321)

#Incomplete
d_glucosaminate = Metabolite("DGL", kegg=C03752)
d_glucosaminate_6_phosphate = Metabolite("DG6P", kegg=C20589)

d_glucosaminate_phosphorylation = Reaction(name="DGLP",
                                           reactants=d_glucosaminate + phosphoenol_group,
                                           products=d_glucosaminate_6_phosphate,
                                           pairs=[d_glucosaminate, d_glucosaminate_6_phosphate],
                                           minors=[phosphoenol_group])

#OTHER FAMILY
#Incomplete pathway, no genes listed:
sorbitol = Metabolite("sorbitol", kegg=C00794)
sorbitol_6_phosphate = Metabolite("SO6P", kegg=C01096)

sorbitol_phosphorylation = Reaction(name="SoP",
                                    reactants=sorbitol + phosphoenol_group,
                                    products=sorbitol_6_phosphate,
                                    pairs=[(sorbitol, sorbitol_6_phosphate)],
                                    minors=[phosphoenol_group])

galactitol = Metabolite("galactitol", kegg=C01697)
galactitol_1_phosphate = Metabolite("G1P", kegg=C06311)

galactitol_phosphorylation = Reaction(name="G2P",
                                      reactants=galactitol + phosphoenol_group,
                                      products=galactitol_1_phosphate,
                                      pairs=[(galactitol, galactitol_1_phosphate)],
                                      minors=[phosphoenol_group])

GeneAssociation(G2P, SP_0647 & (SP_0645 | SP_1198 | SP_0646 | SP_1197))

l_ascorbate = Metabolite("LA", kegg=C00072)
l_ascorbate_6_phosphate = Metabolute("LA6P", kegg=C16186)

l_ascorbate_phosphorylation = Reaction(name="LAP",
                                       reactants=l_ascorbate + phosphoenol_group,
                                       products=l_ascorbate_6_phosphate,
                                       pairs=[(l_ascorbate, l_ascorbate_6_phosphate)],
                                       minors=[phosphoenol_group])

GeneAssociation(LAP, SP_2038 & (SP_2129 | SP_2036 | SP_2037 | SP_2130))

#NITROGEN REGULATION
#No reactants listed for this pathway?

#GENE REGULATION
