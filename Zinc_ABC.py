extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

atp = Metabolite("atp")
adp = Metabolite("adp")
phosphate = Metabolite("phosphate")
H20 = Metabolite("H20",kegg="C00001")
zinc = Metabolite("zinc", kegg="C00038")



zinc = Reaction(name="zinc",
                      reactants=e(zinc) + H20 + atp,
                      products=zinc + adp + phosphate,
                      pairs=[(atp, adp)],
                      minors=[atp, adp])

SP_2169 = Gene("SP_2169")
SP_2170 = Gene("SP_21170")
SP_2171 = Gene("SP_2171")
zinc_GA = GeneAssociation(zinc, SP_2169 & SP_2170 & SP_2171)

