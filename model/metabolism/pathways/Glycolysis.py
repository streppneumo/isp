__author__ = 'derekthibault'

#β-D-glucose to pyruvate

from model.common.compartments import e
from model.metabolites import *

#majors
bDGlu = Metabolite("beta-D-Glucose", kegg="C00221")
bDGlu6P = Metabolite("beta-D-Glucose 6-phosphate", kegg="C01172")
Dfru6P = Metabolite("D-fructose 6-phosphate", kegg="C00085")
Dfru16bisP = Metabolite("D-fructose 1,6-bisphosphate", kegg="C00354")
Dglycerald3P = Metabolite("D-glyceraldehyde 3-phosphate", kegg="C00118")
glyceroneP = Metabolite("glycerone phosphate", kegg="C00111")
BisPDglycerate13 = Metabolite("1,3-Bisphospho-D-glycerate", kegg="C00236")
PDglycerate3 = Metabolite("3-phospho-D-glycerate", kegg="C00197")
PDglycerate2 = Metabolite("2-phospho-D-glycerate", kegg="C00631")
phosphoenolpyruvate = Metabolite("phosphoenolpyruvate", kegg="C00074")
pyruvate = Metabolite("pyruvate", kegg="C00022")

glucokinase = Reaction(name="glucokinase",
                       reactants=e(bDGlu) + atp,
                       products=bDGlu6P + adp + H,
                       pairs=[(bDGlu, bDGlu6P), (atp, adp)],
                       minors=[atp, adp, H]
)
SP_0668 = Gene("SP_0668")
GeneAssociation(glucokinase, SP_0668)

pgi = Reaction(name="pgi",
               reactants=bDGlu6P,
               products=Dfru6P,
               pairs=[b - D - Glu, b - D - Glu6P],
               reversible=True
)
SP_2070 = Gene("SP_2070")
pgi = GeneAssociation(pgi, SP_2070)

pfkA = Reaction(name="pfkA",
                reactants=Dfru6P + atp,
                products=Dfru16bisP + adp + H,
                pairs=[(Dfru6P, Dfru16bisP), (atp, adp)],
                minors=[atp, adp, H]
)
SP_0896 = Gene("SP_0896")
GeneAssociation(pfkA, SP_0896)


#since enzyme names can be complex why
#not use E.C. enzyme/rxn numbers instead of common names?
fruBisPaldolase = Reaction(name="fruBisPaldolase",
                           reactants=Dfru16bisP,
                           products=Dglycerald3P + glyceroneP,
                           pairs=[(Dfru16bisP, Dglycerald3P), (Dfru16bisP, glyceroneP)],
                           reversible=True
)
SP_0605 = Gene("SP_0605")
GeneAssociation(fruBisPaldolase, SP_0605)

tpiA = Reaction(name="tpiA",
                reactants=glyceroneP,
                products=Dglycerald3P,
                pairs=[glyceroneP, Dglycerald3P],
                reversible=True
)
SP_1574 = Gene("SP_1574")
tpiA = GeneAssociation(tpiA, SP_1574)

#SP_2012 and SP_1119 are the same enzyme that can catalyze two different rxns, in this case
#should I use the EC# to describ ethe reaction? AND/OR??
EC12112 = Reaction(name="EC12112",
                   reactants=Dglycerald3P + phosphate + NAD,
                   products=BisPDglycerate13 + NADH + H,
                   pairs=[(Dglycerald3P, BisPDglycerate13), (NAD, NADH)],
                   minors=[phosphate, H, NAD, NADH],
                   reversible=True
)
SP_2012 = Gene("SP_2012")
GeneAssociation(EC12112, SP_2012)

#SP_2012 and SP_1119 have the same common name 'glyceraldehyde-3-phosphate dehydrogenase'
#that can catalyze two different rxns, in this case
#should I use the EC# to describ ethe reaction?
EC1219 = Reaction(name="EC1219",
                  reactants=Dglycerald3P + NADP + H2O,
                  products=PDglycerate3 + NADPH + H,
                  pairs=[(Dglycerald3P, PDglycerate3), (NADPH, NADP)],
                  minors=[NADP, H2O, NADPH, H],
                  reversible=True
)
SP_1119 = Gene("SP_1119")
GeneAssociation(EC1219, SP_1119)

pgk = Reaction(name="pgk",
               reactants=BisPDglycerate13 + adp,
               products=PDglycerate3 + atp,
               pairs=[(BisPDglycerate13, PDglycerate3), (atp, adp)],
               reversible=True
)
SP_0499 = Gene("SP_0499")
GeneAssociation(pgk, SP_0499)


Pglycermutase = Reaction(name="Pglycermutase",
                         reactants=PDglycerate3,
                         products=PDglycerate2,
                         pairs=[(PDglycerate3, PDglycerate2)],
                         reversible=True
)
SP_1655 = Gene("SP_1655")
SP_0240 = Gene("SP_0240")
SP_0984 = Gene("SP_0984")
GeneAssociation(Pglycermutase, SP_1655 & (SP_0240 | SP_0984))

eno = Reaction(name="eno",
               reactants=PDglycerate2,
               products=phosphoenolpyruvate + H20,
               pairs=[(PDglycerate2, phosphoenolpyruvate)],
               reversible=True
)
SP_1128 = Gene("SP_1128")
GeneAssociation(eno, SP_1128)

pyruvkinase = Reaction(name="pyruvkinase",
                       reactants=phosphoenolpyruvate + adp + H,
                       products=pyruvate + atp,
                       pairs=[(phosphoenolpyruvate, pyruvate), (adp, atp)],
)
SP_0897 = Gene("SP_0897")
GeneAssociation(pyruvkinase, SP_0897)