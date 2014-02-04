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

phosphoenol_pyruvate = Metabolite ("PEP")
pyruvate = Metabolite ("pyruvate")
ADP = Metabolite ("ADP")
ATP = Metabolite ("ATP")

ATPgeneration = Reaction(name="ATP",
                reactants=PEP + ADP,
                products=pyruvate + ATP,
                pairs=[(PEP, pyruvate),(ADP,ATP)],
                minors=[PEP,pyruvate])

SP_1176 = Gene("SP_1176")
ATP_GA = GeneAssociation(ATP, SP_1176)



glucose = Metabolite  ("glucose")
glucose_6_phosphate = Metabolite ("glucose6phosphate")
ATP = Metabolite ("ATP")
ADP = Metabolite ("ADP")

glucose_phosphorylation = Reaction(name="GP",
                        reactants=glucose + ATP,
                        products=glucose6phosphate + ADP,
                        pairs=[(glucose, glucose6phosphate), (ATP, ADP)],
                        minors=[ATP, ADP])

SP_0758 = Gene("SP_0758")
SP_1684 = Gene("SP_1684")
GP_GA = GeneAssociation(GP, SP_0758 & (SP_1684))



sucrose = Metabolite("sucrose")
sucrose_6_phosphate = Metabolite("sucrose6phosphate")
ATP = Metabolite ("ATP")
ADP = Metabolite ("ADP")

sucrose_phosphorylation = Reaction(name="SP",
                        reactants=sucrose + ATP,
                        products=sucrose6phosphate + ADP,
                        pairs=[(sucrose, sucrose6phosphate), (ATP, ADP)],
                        minors=[ATP, ADP])
SP_1722 = Gene("SP_1722")
SP_GA = GeneAssociation(SP, SP_1722)

