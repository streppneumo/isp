from CellScribe import *
from model.genes import SP_1081, SP_1966, SP_1390, SP_1521, SP_0688, SP_1530, SP_1671, SP_1670, SP_0337, SP_0689, SP_0615, SP_0616, SP_0457, SP_0369, SP_2010, SP_2099, SP_0336, SP_1673, SP_0872

#minors
phosphate = Metabolite("phosphate", kegg="C00009")
PEP = Metabolite("phosphoenolpyruvate", kegg="C00074")
NADP = Metabolite("NADP+", kegg="C00006")
NADPH = Metabolite("NADPH", kegg="C00005")
H = Metabolite("H+", kegg="C00080")
atp = Metabolite("atp", kegg="C00002")
adp = Metabolite("adp", kegg="C00008")
L_alanine = Metabolite("L-alanine", kegg="C00041")
UDP = Metabolite("UDP", kegg="C00015")
L_Lysine = Metabolite("L-lysine", kegg="C00047")
undecaprenyl_phosphate = Metabolite("undecaprenyl phosphate", kegg="C17556")
L_Alanyl_tRNA = Metabolite("L_Alanyl_tRNA", kegg="C00886")
tRNA_Ala = Metabolite("tRNA_Ala", kegg="C01635")
undecaprenyl_diphosphate = Metabolite("undecaprenyl diphosphate", kegg="C04574")
H2O = Metabolite("H2O", kegg="C00001")

#major metabolites
UDP_N_acetyl_alpha_D_glucosamine = Metabolite("UDP-N-acetyl-alpha-D-glucosamine", kegg="C00043")
UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine = Metabolite("UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine", kegg="C04631")
UDP_N_acetylmuramate = Metabolite("UDP-N-acetylmuramate", kegg="C01050")
UDP_N_acetylmuramoyl_L_alanine = Metabolite("UDP-N-acetylmuramoyl-L-alanine", kegg="C01212")
UDP_N_acetylmuramoyl_L_alanyl_D_glutamate = Metabolite("UDP-N-acetylmuramoyl-L-alanyl-D-glutamate", kegg="C00692")
UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine = Metabolite("UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-L-lysine", kegg="C05892")
UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-L-lysyl-D-alanyl-D-alanine", kegg="C04702")
Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl-diphospho-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-L_lysyl-D_alanyl-D-alanine", kegg="C04851")
Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D_glutamyl-L-lysyl-D-alanyl-D-alanine", kegg="C05893")
Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine = Metabolite("Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-gamma-D-glutamyl-L-lysyl-L-alanyl-D-alanyl-D-alanine", kegg="C17550")
peptidoglycan = Metabolite("Undecaprenyl-diphospho-N-acetylmuramoyl-(N_acetylglucosamine)-L-alanyl-gamma-D-glutamyl-L_lysyl-(L_alanyl)2-D-alanyl-D-alanine", kegg="C17549")
di_peptidoglycan = Metabolite("[(2*((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala-D-Ala))-diphosphoundecaprenol]")
cleaved_dipeptidoglycan = Metabolite("[((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala-D-Ala))-(((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala))-diphosphoundecaprenol)]")
bridged_peptidoglycan = Metabolite("[((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala-D-Ala))-(((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala))-diphosphoundecaprenol)-(((GlcNAc-(1->4)-Mur2Ac(oyl-L-Ala-gamma-D-Glu-L-Lys-(L-Ala)2-D-Ala-D-Ala))-diphosphoundecaprenol)]")

D_glutamate = Metabolite("D-glutamate", kegg="C00217")
D_alanyl_D_alanine = Metabolite("D-alanyl-D-alanine", kegg="C00993")
D_alanine = Metabolite("D-alanine", kegg="C00133")
UMP = Metabolite("UMP", kegg="C00105")

##############################################################################

MurA = Reaction(name="MurA",
                reactants=PEP + UDP_N_acetyl_alpha_D_glucosamine,
                products=phosphate + UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine,
                pairs=[(UDP_N_acetyl_alpha_D_glucosamine, UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine)],
                minors=[PEP, phosphate])

MurA_GA = GeneAssociation(MurA, SP_1081 | SP_1966)

##############################################################################

MurB = Reaction(name="MurB",
                reactants=NADPH + H + UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine,
                products=NADP + UDP_N_acetylmuramate,
                pairs=[(UDP_N_acetyl_3_O_1_carboxyvinyl_alpha_D_glucosamine, UDP_N_acetylmuramate)],
                minors=[NADPH, NADP, H])

MurB_GA = GeneAssociation(MurB, SP_1390)

###Make sure minors are going in the right direction

##############################################################################

MurC = Reaction(name="MurC",
                reactants=atp + UDP_N_acetylmuramate + L_alanine,
                products=adp + UDP_N_acetylmuramoyl_L_alanine + phosphate + H,
                pairs=[(UDP_N_acetylmuramate, UDP_N_acetylmuramoyl_L_alanine)],
                minors=[atp, adp, phosphate, L_alanine, H])

MurC_GA = GeneAssociation(MurC, SP_1521)

##############################################################################

MurD = Reaction(name="MurD",
                reactants=UDP_N_acetylmuramoyl_L_alanine + atp + D_glutamate,
                products=UDP_N_acetylmuramoyl_L_alanyl_D_glutamate + adp + phosphate + H,
                pairs=[(UDP_N_acetylmuramoyl_L_alanine, UDP_N_acetylmuramoyl_L_alanyl_D_glutamate)],
                minors=[atp, adp, phosphate, H])

MurD_GA = GeneAssociation(MurD, SP_0688)

##############################################################################

MurE = Reaction(name="MurE",
                reactants=UDP_N_acetylmuramoyl_L_alanyl_D_glutamate + atp + L_Lysine,
                products=adp + phosphate + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine + H,
                pairs=[(UDP_N_acetylmuramoyl_L_alanyl_D_glutamate, UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine)],
                minors=[atp, adp, phosphate, L_Lysine, H])

MurE_GA = GeneAssociation(MurE, SP_1530)

# Left side of the peptidoglycan biosynthesis pathway

##############################################################################

ddl = Reaction(name="ddl",
               reactants=atp + 2*(D_alanine),
               products=adp + phosphate + D_alanyl_D_alanine + H,
               pairs=[(2*(D_alanine), D_alanyl_D_alanine)],
               minors=[atp, adp, phosphate, H])

ddl_GA = GeneAssociation(ddl, SP_1671)

##############################################################################

MurF_Homolog = Reaction(name="MurF_Homolog",
                          reactants=atp + D_alanyl_D_alanine + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine,
                          products=adp + phosphate + UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + H,
                          pairs=[(UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysine, UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)],
                          minors=[atp, adp, phosphate, H])

MurF_Homolog_GA = GeneAssociation(MurF_Homolog, SP_1670)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MraY = Reaction(name="MraY",
                reactants = UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + undecaprenyl_phosphate,
                products=UMP + Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine,
                pairs=[(UDP_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)])

MraY_GA = GeneAssociation(MraY, SP_0337)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MurG = Reaction("MurG",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + UDP_N_acetyl_alpha_D_glucosamine,
                products=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + UDP,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine)],
                minors=[UDP_N_acetyl_alpha_D_glucosamine, UDP])

MurG_GA = GeneAssociation(MurG, SP_0689)

#Left side of the peptidoglycan biosynthesis pathway

##############################################################################

MurM = Reaction("MurM",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine + L_Alanyl_tRNA,
                products=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine + tRNA_Ala,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_D_alanyl_D_alanine, Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine)],
                minors=[L_Alanyl_tRNA, tRNA_Ala])

MurM_GA = GeneAssociation(MurM, SP_0615)

##############################################################################

MurN = Reaction("MurN",
                reactants=Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine + L_Alanyl_tRNA,
                products=peptidoglycan + tRNA_Ala,
                pairs=[(Undecaprenyl_diphospho_N_acetylmuramoyl_N_acetylglucosamine_L_alanyl_gamma_D_glutamyl_L_lysyl_L_alanyl_D_alanyl_D_alanine, peptidoglycan)],
                minors=[L_Alanyl_tRNA, tRNA_Ala])

MurN_GA = GeneAssociation(MurN, SP_0616)

##############################################################################

Class_A_PBP = SP_0369 & SP_2010 & SP_2099
Class_B_PBP = SP_0336 & SP_1673
Class_C_PBP = SP_0872

#glycosyltransferase : elongation of uncross-linked glycans (N-acetylmuramic acid and N-acetylglucosamine)
#transpeptidase : peptide cross-linking between two adjacent glycans
#DD-carboxypeptidase : hydrolyzes peptide bonds (in this case, between D-ala-D-alanine) to help control the extent of PG cross-linking

##Class A PBPs: N-terminal has a glycosyltransferase activity and the C-terminal has a transpeptidase activity
###pbp1a = SP_0369
###pbp1b = SP_2099
###pbp2a = SP_2010

##Class B PBPs: C-terminal has a transpeptidase activity; other functions not characterized but plays a role in cell division; has PASTA domains which are thought to bind unlinked peptidoglycans
###pbp2x = SP_0336 (cell division)
###pbp2b = SP_1673 (functions during growth phase)

##Class C PBPs: DD-carboxypeptidases
###SP_0872 (EC 3.4.16.4)

##############################################################################

#Peptidoglycans consist of two alternating sugars N-acetylmuramic acid or N-acetylglucosamine
#N-acetylmuramic acid has a pentapeptide chain attached to it. Third amino acid is the cross-linking site and is, in the case of S. pneumoniae, a L-Lys
#Cross bridge consists of two L-Ala

Glycolsyltransferase = Reaction("Glycosyltransferase",
                                reactants = 2*(peptidoglycan),
                                products = undecaprenyl_diphosphate + di_peptidoglycan,
                                pairs = [(2*(peptidoglycan), di_peptidoglycan)],
                                minors = [undecaprenyl_diphosphate])

Glycolsyltransferase_GA = GeneAssociation(Glycolsyltransferase, Class_A_PBP)

#SP_0369 = pbp1a; septal location
#SP_2010 = pbp2a; equatorial location
#SP_2099 = pbp1b; septal or equatorial (exclusively one or the other)

#Knockouts:
## ~SP_0369 and ~SP_2099 = nonlethal; possibly enlarged diploid morphology
## ~SP_2010 and ~SP_2099 = nonlethal; divides without elongation leading to non-viable minicells
## ~SP_2010 = nonlethal; significant # of pbp1a proteins found at the equator
## ~SP_0369 and ~SP_2010 = lethal

#Reference = "Growth and Division of Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet

##############################################################################

uppP = Reaction("uppP",
                reactants=undecaprenyl_diphosphate + H2O,
                products=undecaprenyl_phosphate + phosphate + H,
                pairs=[(undecaprenyl_diphosphate, undecaprenyl_phosphate)],
                minors=[H2O, H])

uppP_GA = GeneAssociation(uppP, SP_0457)

##############################################################################

Carboxypeptidase = Reaction("Carboxypeptidase",
                            reactants = di_peptidoglycan + H2O,
                            products = cleaved_dipeptidoglycan + D_alanine,
                            pairs = [(di_peptidoglycan, cleaved_dipeptidoglycan)],
                            minors = [H2O, D_alanine])

Carboxypeptidase_GA = GeneAssociation(Carboxypeptidase, Class_C_PBP)

#SP_0872: No apparent phenotype associated with its inactivation in S. aureus

#Reference = "The penicillin binding proteins..." Kerff, Terrak, and Charlier, pg. 244-245

##############################################################################

Transpeptidase = Reaction("Transpeptidase",
                          reactants = cleaved_dipeptidoglycan + peptidoglycan,
                          products = bridged_peptidoglycan)

Transpeptidase_GA = GeneAssociation(Transpeptidase, Class_A_PBP & Class_B_PBP)

#SP_0369 = pbp1a; septal location
#SP_2010 = pbp2a; equatorial location
#SP_2099 = pbp1b; septal or equatorial (exclusively one or the other)

#Knockouts:
## ~SP_0369 and ~SP_2099 = nonlethal; possibly enlarged diploid morphology
## ~SP_2010 and ~SP_2099 = nonlethal; divides without elongation leading to non-viable minicells
## ~SP_2010 = nonlethal; significant # of pbp1a proteins found at the equator
## ~SP_0369 and ~SP_2010 = lethal

#SP_0336 = pbp2x; septal location
#SP_1673 = pbp2a; equilibrium location

#Knockouts:
## ~SP_0336 = lethal
## ~SP_1673 = lethal

#Reference = "Growth and Division of Streptococcus pnuemoniae..." Morlot, Zapun, Dideberg and Vernet

##############################################################################






