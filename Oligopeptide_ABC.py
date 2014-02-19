from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp")
adp = Metabolite("adp")
phosphate = Metabolite("phosphate")
H20 = Metabolite("H20",kegg="C00001")
oligopeptide = Metabolite("oligopeptide", kegg="C00098")

oligopeptide = Reaction(name="oligopeptide",
                    reactants=e(oligopeptide) + H20 + atp,
                    products=oligopeptide + adp + phosphate)

SP_1527 = Gene("SP_1527")
SP_1891 = Gene("SP_1891")
SP_0366 = Gene("SP_0366")
SP_1887 = Gene("SP_1887")
SP_1888 = Gene("SP_1888")
SP_1889 = Gene("SP_1889")
SP_1890 = Gene("SP_1890")


oligopeptide_GA = GeneAssociation(oligopeptide, SP_1527 or SP_1891 or SP_0366 or SP_1887 or SP_1888 or SP_1889 or SP_1890 )
