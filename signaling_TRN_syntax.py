
Effect(effector, target, relationship=["activator", "repressor"])
#this is not code

activates(activator, target)
represses(repressor, target)

malX = Gene("SP_2012")
malA = Gene("SP_2013")

represses(malX, malA)

# do this (use ~ for not, & for and, | for or)
If(~e(maltose), represses(malX, malA))

# not this
if not e(maltose):
   represses(malX, malA)

#Iff : if and only if

#If(A, B)
#If(homework, A on final)
#Iff(A, B) <=> Iff(B, A)

#geneA activates geneB
#If(geneA, geneB)
#Iff(geneA, geneB)

# keywords
#If <-> sufficient
#Iff <-> necessary



Modification(target, enzyme, modification=["phosphorylation", "acetylation"])

phosphorylates(enzyme, target)

ModifiedProtein(protein, modification=["phosphorylation", "acetylation"])

phospho(protein)
phospho(protein, n)

# DEREK - THIS IS NOT CODE
#malX -> p-malX (kinase is malK)
#p-malX -| geneY

phosphorylates(malK, malX)
represses(phospho(malX), geneY)

phospho(malX) <-> phospho(malX, 1)
phospho(phospho(malX)) -> phospho(malX, 2)

# operon example
Operon(gene1, gene2, gene2, ...)
Regulon(gene1, ...)

malOperon = Operon(malA, malB, malC)
If(~e(maltose), represses(malX, malOperon))
activates(malW, malC)

#Operons - proximal to one another in genome
#Regulon - regulated together, but in different places


If(cond, action)
Iff(cond, action)




