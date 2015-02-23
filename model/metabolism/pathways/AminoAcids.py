#2.1.3.2
#AUTOADD ASPCARBTRANS-RXN
Reaction('ASPCARBTRANS-RXN',
         reactants=['L-ASPARTATE', 'CARBAMOYL-P'],
         reversible='LEFT-TO-RIGHT',
         products=['PROTON', 'CARBAMYUL-L-ASPARTATE', 'Pi'],
         ec=['EC-2.1.3.2'],
         minors=['PROTON','Pi'],
         biocyc='ASPCARBTRANS-RXN')
EnzymeAssociation('EC-2.1.3.2', 'SPT_0950') # t19f
EnzymeAssociation('EC-2.1.3.2', 'SP_1277') # tigr4
EnzymeAssociation('EC-2.1.3.2', 'SPD_1133') # d39
Homolog(['SPT_0950'], ['SP_1277'], ['SPD_1133'])

#6.3.1.1
#AUTOADD ASNSYNA-RXN
Reaction('ASNSYNA-RXN',
         reactants=['L-ASPARTATE', 'AMMONIUM', 'ATP'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['PROTON', 'ASN', 'PPI', 'AMP'],
         minors=['AMONIUM', 'ATP', 'PROTON', 'AMP', 'PPI'],
         pairs=[('ATP', 'ADP')],
         ec=['EC-6.3.1.1'],
         biocyc='ASNSYNA-RXN')
EnzymeAssociation('EC-6.3.1.1', 'SPT_1950') # t19f
EnzymeAssociation('EC-6.3.1.1', 'SP_1970') # tigr4
EnzymeAssociation('EC-6.3.1.1', 'SPD_1768') # d39
Homolog(['SPT_1950'], ['SP_1970'], ['SPD_1768'])

#6.3.4.4
#AUTOADD ADENYLOSUCCINATE-SYNTHASE-RXN
Reaction('ADENYLOSUCCINATE-SYNTHASE-RXN',
         reactants=['L-ASPARTATE', 'IMP', 'GTP'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['PROTON', 'ADENYLOSUCC', 'Pi', 'GDP'],
         minors=['IMP', 'GTP', 'PROTON', 'Pi', 'GDP'],
         ec=['EC-6.3.4.4'],
         biocyc='ADENYLOSUCCINATE-SYNTHASE-RXN')
EnzymeAssociation('EC-6.3.4.4', 'SPT_0059') # t19f
EnzymeAssociation('EC-6.3.4.4', 'SP_0019') # tigr4
EnzymeAssociation('EC-6.3.4.4', 'SPD_0024') # d39
Homolog(['SPT_0059'], ['SP_0019'], ['SPD_0024'])

#2.6.1.2
#  Biocyc has no annotation for t19f.  Blast of SP_1994 four hit with SPT_1974,
#  an aminotransferase AlaT.
#
#  Adding SPT_1974 to t19f.
Reaction('ALANINE-AMINOTRANSFERASE-RXN',
         reactants=['2-KETOGLUTARATE', 'L-ALPHA-ALANINE'],
         reversible='REVERSIBLE',
         products=['GLT', 'PYRUVATE'],
         minors=['2-KETOGLUTARATE', 'GLT'],
         ec=['EC-2.6.1.2'],
         biocyc='ALANINE-AMINOTRANSFERASE-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-2.6.1.2', 'SP_1994') # tigr4
EnzymeAssociation('EC-2.6.1.2', 'SPD_1791') # d39
EnzymeAssociation('EC-2.6.1.2', 'SPT_1974') # t19f
Homolog(['SP_1994'], ['SPD_1791'], ['SPT_1974'])

# RXN-13698 is a repeat of ALANINE-AMINOTRANSFERASE-RXN

#4.3.2.2
#AUTOADD AICARSYN-RXN
Reaction('AICARSYN-RXN',
         reactants=['P-RIBOSYL-4-SUCCCARB-AMINOIMIDAZOLE'],
         reversible='LEFT-TO-RIGHT',
         products=['FUM', 'AICAR'],
         minors=['AICAR'],
         ec=['EC-4.3.2.2'],
         biocyc='AICARSYN-RXN')
EnzymeAssociation('EC-4.3.2.2', 'SPT_0094') # t19f
EnzymeAssociation('EC-4.3.2.2', 'SP_0056') # tigr4
EnzymeAssociation('EC-4.3.2.2', 'SPD_0062') # d39
Homolog(['SPT_0094'], ['SP_0056'], ['SPD_0062'])

############ Alanine, Aspartate, and Glutamate Metabolism ############

#1.4.1.4
#  Biocyc has no association for t19f.  Kegg lists SPT_0923 (glutamate 
#  dehydrogenase), which is also associated with 1.4.1.3.
#
#  Including SPT_0923.
Reaction('GLUTDEHYD-RXN',
         reactants=['GLT', 'WATER', 'NADP'],
         reversible='RIGHT-TO-LEFT',
         products=['PROTON', 'AMMONIUM', '2-KETOGLUTARATE', 'NADPH'],
         minors=['WATER', 'NADP', 'PROTON', 'AMMONIUM', 'NADPH'],
         ec=['EC-1.4.1.4'],
         biocyc='GLUTDEHYD-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-1.4.1.4', 'SP_1306') # tigr4
EnzymeAssociation('EC-1.4.1.4', 'SPD_1158') # d39
EnzymeAssociation('EC-1.4.1.4', 'SPT_0923') # t19f
Homolog(['SP_1306'], ['SPD_1158'], ['SPT_0923'])

#2.6.1.16
#AUTOADD L-GLN-FRUCT-6-P-AMINOTRANS-RXN
Reaction('L-GLN-FRUCT-6-P-AMINOTRANS-RXN',
         reactants=['FRUCTOSE-6P', 'GLN'],
         reversible='REVERSIBLE',
         products=['D-GLUCOSAMINE-6-P', 'GLT'],
         ec=['EC-2.6.1.16'],
         biocyc='L-GLN-FRUCT-6-P-AMINOTRANS-RXN')
EnzymeAssociation('EC-2.6.1.16', 'SPT_0313') # t19f
EnzymeAssociation('EC-2.6.1.16', 'SP_0266') # tigr4
EnzymeAssociation('EC-2.6.1.16', 'SPD_0248') # d39
Homolog(['SPT_0313'], ['SP_0266'], ['SPD_0248'])

#6.3.1.2
#AUTOADD GLUTAMINESYN-RXN
Reaction('GLUTAMINESYN-RXN',
         reactants=['AMMONIUM', 'GLT', 'ATP'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['PROTON', 'GLN', 'ADP', 'Pi'],
         ec=['EC-6.3.1.2'],
         biocyc='GLUTAMINESYN-RXN')
EnzymeAssociation('EC-6.3.1.2', 'SPT_0539') # t19f
EnzymeAssociation('EC-6.3.1.2', 'SP_0502') # tigr4
EnzymeAssociation('EC-6.3.1.2', 'SPD_0448') # d39
Homolog(['SPT_0539'], ['SP_0502'], ['SPD_0448'])

#2.4.2.14
#AUTOADD PRPPAMIDOTRANS-RXN
Reaction('PRPPAMIDOTRANS-RXN',
         reactants=['5-P-BETA-D-RIBOSYL-AMINE', 'PPI', 'GLT'],
         reversible='RIGHT-TO-LEFT',
         products=['PRPP', 'GLN', 'WATER'],
         ec=['EC-2.4.2.14'],
         biocyc='PRPPAMIDOTRANS-RXN')
EnzymeAssociation('EC-2.4.2.14', 'SPT_0085') # t19f
EnzymeAssociation('EC-2.4.2.14', 'SP_0046') # tigr4
EnzymeAssociation('EC-2.4.2.14', 'SPD_0053') # d39
Homolog(['SPT_0085'], ['SP_0046'], ['SPD_0053'])

#6.3.5.5
#  carbamoyl phosphate synthase includes both a large and small subunit.
#  Biocyc includes a third gene for t19f (SPT_1316).  Kegg includes only
#  SPT_0951 (small) and SPT_0952 (large).
#
#  SPT_1316 is annotated as a large subunit.  It is highly conserved across
#  the other strains, but unannotated.
#
#  Including SPT_1316 and homologs as possible large subunits.
Reaction('CARBPSYN-RXN',
         reactants=['ATP', 'GLN', 'HCO3', 'WATER'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['GLT', 'CARBAMOYL-P', 'ADP', 'Pi', 'PROTON'],
         minors=['ATP', 'HCO3', 'WATER', 'ADP', 'Pi', 'PROTON'],
         ec=['EC-6.3.5.5'],
         biocyc='CARBPSYN-RXN')
EnzymeAssociation('EC-6.3.5.5', SPT_0951 & SPT_0952) # t19f
EnzymeAssociation('EC-6.3.5.5', SP_1275 & SP_1276) # tigr4
EnzymeAssociation('EC-6.3.5.5', SPD_1131 & SPD_1132) # d39
Homolog(['SPT_0951', 'SPT_0952'], 
        ['SP_1275', 'SP_1276'], 
        ['SPD_1131', 'SPD_1132'])
PossibleHomolog(['SPT_1316', 'SP_0085', 'SPD_0781'],
                ['SPT_0952', 'SP_1276', 'SPD_1132'])

# RXN-13202 is similar, but uses ammonium instead of GLN as a substrate.
# Not included in model.

#3.5.1.1
#AUTOADD ASPARAGHYD-RXN
Reaction('ASPARAGHYD-RXN',
         reactants=['ASN', 'WATER'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['L-ASPARTATE', 'AMMONIUM'],
         minors=['WATER', 'AMMONIUM'],
         ec=['EC-3.5.1.38', 'EC-3.5.1.1'],
         biocyc='ASPARAGHYD-RXN')
EnzymeAssociation(['EC-3.5.1.38', 'EC-3.5.1.1'], 'SPT_1978') # t19f
EnzymeAssociation(['EC-3.5.1.38', 'EC-3.5.1.1'], 'SP_1998') # tigr4
EnzymeAssociation(['EC-3.5.1.38', 'EC-3.5.1.1'], 'SPD_1796') # d39
Homolog(['SPT_1978'], ['SP_1998'], ['SPD_1796'])

#6.3.4.5
#AUTOADD ARGSUCCINSYN-RXN
#  Blast against TIGR4 yielded no homolog.
#  Should RXN-10 also be included?  No, CANAVANINE is only found in plants.
Reaction('ARGSUCCINSYN-RXN',
         reactants=['L-ASPARTATE', 'L-CITRULLINE', 'ATP'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['PROTON', 'L-ARGININO-SUCCINATE', 'PPI', 'AMP'],
         minors=['ATP', 'PROTON', 'PPI', 'AMP'],
         ec=['EC-6.3.4.5'],
         biocyc='ARGSUCCINSYN-RXN')
EnzymeAssociation('EC-6.3.4.5', 'SPT_0147') # t19f
EnzymeAssociation('EC-6.3.4.5', 'SPD_0110') # d39
Homolog(['SPT_0147'], ['SPD_0110'])

#4.3.2.1
#AUTOADD ARGSUCCINLYA-RXN
#  Blast found no homologs in tigr4 or t19f.
Reaction('ARGSUCCINLYA-RXN',
         reactants=['L-ARGININO-SUCCINATE'],
         reversible='LEFT-TO-RIGHT',
         products=['ARG', 'FUM'],
         minors=[],
         ec=['EC-4.3.2.1'],
         biocyc='ARGSUCCINLYA-RXN')
EnzymeAssociation('EC-4.3.2.1', 'SPD_0111') # d39
Homolog(['SPD_0111'])


############ Glycine, Serine, and Threonine Metabolism ############

#2.7.1.31
# Kegg says reversible, Biocyc says None
# homolog for tigr4 added by KZ
Reaction('GLY3KIN-RXN',
         reactants=['GLYCERATE', 'ATP'],
         reversible=True,
         products=['PROTON', 'G3P', 'ADP'],
         minors=['ATP', 'ADP', 'PROTON'],
         ec=['EC-2.7.1.31'],
         biocyc='GLY3KIN-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-2.7.1.31', 'SPT_1172') # t19f
EnzymeAssociation('EC-2.7.1.31', 'SPD_1011') # d39
EnzymeAssociation('EC-2.7.1.31', 'SP_1126') # tigr4
Homolog(['SPT_1172'], ['SPD_1011'], ['SP_1126'])

#4.3.1.17
#  Reaction has both an alpha and beta subunit.  Biocyc does not have alpha
#  subunit (SP_0105) for tigr4; kegg does.
#
#  Associating SP_0105 for tigr4.  This is an AND relation.
#  Adding iron and sulfur as co-factors per kegg.
Reaction('4.3.1.17-RXN',
         reactants=['SER'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['PYRUVATE', 'AMMONIUM'],
         minors=['AMMONIUM'],
         cofactors=['CPD-6'],  #2Fe-2S
         ec=['EC-4.3.1.17'],
         biocyc='4.3.1.17-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-4.3.1.17', SPT_0139 & SPT_0140) # t19f
EnzymeAssociation('EC-4.3.1.17', SP_0105 & SP_0106) # tigr4
EnzymeAssociation('EC-4.3.1.17', SPD_0102 & SPD_0103) # d39
Homolog([SPT_0139, SPT_0140], [SP_0105, SP_0106], [SPD_0102, SPD_0103])

#4.3.1.19
#  Kegg associates this EC number with the 4.3.1.17-RXN as well as the
#  THREDEHYD-RXN.  Biocyc adds SP_0106 to this rxn, which kegg does not.
#
#  Removing annotation for SP_0106.
#  Removing cross reactivity with 4.3.1.17-RXN.
Reaction('THREDEHYD-RXN',
         reactants=['THR'],
         reversible='PHYSIOL-LEFT-TO-RIGHT',
         products=['2-OXOBUTANOATE', 'AMMONIUM'],
         minors=['AMMONIUM'],
         ec=['EC-4.3.1.19'],
         biocyc='THREDEHYD-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-4.3.1.19', 'SPT_0486') # t19f
EnzymeAssociation('EC-4.3.1.19', 'SP_0450') # tigr4
EnzymeAssociation('EC-4.3.1.19', 'SPD_0409') # d39
Homolog(['SPT_0486'], ['SP_0450'], ['SPD_0409'])

#4.2.1.20
#  Alpha and beta subunits (via kegg); AND relation
#
#  Made reversible to match kegg.
Reaction('TRYPSYN-RXN',
         reactants=['INDOLE-3-GLYCEROL-P', 'SER'],
         reversible=False,
         products=['TRP', 'WATER', 'GAP'],
         minors=['INDOLE-3-GLYCEROL-P', 'WATER', 'GAP'],
         ec=['EC-4.2.1.20'],
         biocyc='TRYPSYN-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-4.2.1.20', SPT_1734 & SPT_1735) # t19f
EnzymeAssociation('EC-4.2.1.20', SP_1811 & SP_1812) # tigr4
EnzymeAssociation('EC-4.2.1.20', SPD_1596 & SPD_1597) # d39
Homolog([SPT_1734, SPT_1735], [SP_1811, SP_1812], [SPD_1596, SPD_1597])

#2.1.2.1
#AUTOADD GLYOHMETRANS-RXN
Reaction('GLYOHMETRANS-RXN',
         reactants=['SER', 'THF'],
         reversible='REVERSIBLE',
         products=['METHYLENE-THF', 'GLY', 'WATER'],
         minors=['WATER'],
         ec=['EC-2.1.2.1'],
         biocyc='GLYOHMETRANS-RXN')
EnzymeAssociation('EC-2.1.2.1', 'SPT_1076') # t19f
EnzymeAssociation('EC-2.1.2.1', 'SP_1024') # tigr4
EnzymeAssociation('EC-2.1.2.1', 'SPD_0910') # d39
Homolog(['SPT_1076'], ['SP_1024'], ['SPD_0910'])

#4.2.3.1
#AUTOADD THRESYN-RXN
Reaction('THRESYN-RXN',
         reactants=['O-PHOSPHO-L-HOMOSERINE', 'WATER'],
         reversible='LEFT-TO-RIGHT',
         products=['Pi', 'THR'],
         minors=['WATER', 'Pi'],
         ec=['EC-4.2.3.1'],
         biocyc='THRESYN-RXN')
EnzymeAssociation('EC-4.2.3.1', 'SPT_2061') # t19f
EnzymeAssociation('EC-4.2.3.1', 'SP_2066') # tigr4
EnzymeAssociation('EC-4.2.3.1', 'SPD_1877') # d39
Homolog(['SPT_2061'], ['SP_2066'], ['SPD_1877'])

#2.7.1.39
#AUTOADD HOMOSERKIN-RXN
Reaction('HOMOSERKIN-RXN',
         reactants=['HOMO-SER', 'ATP'],
         reversible='LEFT-TO-RIGHT',
         products=['PROTON', 'O-PHOSPHO-L-HOMOSERINE', 'ADP'],
         minors=['ATP', 'PROTON', 'ADP'],
         ec=['EC-2.7.1.39'],
         biocyc='HOMOSERKIN-RXN')
EnzymeAssociation('EC-2.7.1.39', 'SPT_0914') # t19f
EnzymeAssociation('EC-2.7.1.39', 'SP_1360') # tigr4
EnzymeAssociation('EC-2.7.1.39', 'SPD_1194') # d39
Homolog(['SPT_0914'], ['SP_1360'], ['SPD_1194'])

#1.1.1.3
#  Kegg and biocyc do not have homolog in t19f.  Blast did not find homolog.
#  Kegg lists as reversible; biocyc does not.
#
#  This rxn is only present in tigr4 and d39.
Reaction('HOMOSERDEHYDROG-RXN',
         reactants=['HOMO-SER', 'NAD-P-OR-NOP'],
         reversible='RIGHT-TO-LEFT',
         products=['L-ASPARTATE-SEMIALDEHYDE', 'NADH-P-OR-NOP', 'PROTON'],
         minors=['NAD-P-OR-NOP', 'NADH-P-OR-NOP', 'PROTON'],
         ec=['EC-1.1.1.3'],
         biocyc='HOMOSERDEHYDROG-RXN',
         db_differences=['reversible'])
EnzymeAssociation('EC-1.1.1.3', 'SP_1361') # tigr4
EnzymeAssociation('EC-1.1.1.3', 'SPD_1195') # d39
Homolog(['SP_1361'], ['SPD_1195'])

#1.2.1.11
#AUTOADD ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN
Reaction('ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN',
         reactants=['L-ASPARTATE-SEMIALDEHYDE', 'Pi', 'NADP'],
         reversible='RIGHT-TO-LEFT',
         products=['L-BETA-ASPARTYL-P', 'NADPH', 'PROTON'],
         minors=['Pi', 'NADP', 'NADPH', 'PROTON'],
         ec=['EC-1.2.1.11'],
         biocyc='ASPARTATE-SEMIALDEHYDE-DEHYDROGENASE-RXN')
EnzymeAssociation('EC-1.2.1.11', 'SPT_1067') # t19f
EnzymeAssociation('EC-1.2.1.11', 'SP_1013') # tigr4
EnzymeAssociation('EC-1.2.1.11', 'SPD_0900') # d39
Homolog(['SPT_1067'], ['SP_1013'], ['SPD_0900'])

#2.7.2.4
#AUTOADD ASPARTATEKIN-RXN
Reaction('ASPARTATEKIN-RXN',
         reactants=['L-ASPARTATE', 'ATP'],
         reversible='LEFT-TO-RIGHT',
         products=['L-BETA-ASPARTYL-P', 'ADP'],
         minors=['ATP', 'ADP'],
         ec=['EC-2.7.2.4'],
         biocyc='ASPARTATEKIN-RXN')
EnzymeAssociation('EC-2.7.2.4', 'SPT_0450') # t19f
EnzymeAssociation('EC-2.7.2.4', 'SP_0413') # tigr4
EnzymeAssociation('EC-2.7.2.4', 'SPD_0377') # d39
Homolog(['SPT_0450'], ['SP_0413'], ['SPD_0377'])

