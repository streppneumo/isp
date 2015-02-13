
#glucose
#  biocyc uses GLC for beta-glucose and ALPHA-GLUCOSE for alpha-glucose.
#  We will specify alpha- and beta-glucose explicitly for intracellular
#  reactions.  GLUCOSE will be a group name for both isomers.
#
#  Both forms refer to D-glucose.
Metabolite('ALPHA-GLUCOSE', biocyc='ALPHA-GLUCOSE')
Metabolite('BETA-GLUCOSE', biocyc='GLC')
MetaboliteGroup('GLUCOSE', ['ALPHA-GLUCOSE', 'BETA-GLUCOSE']) 

#3.1.3.10
#   biocyc has for d39, tigr4 as non-enzymatic.  Blasted ecoli b1002 against 
#   tigr4 and found no hits.
#
#   Not including in model.

#5.4.2.2
#   biocyc does not have enzyme for 19f. 
#   blasted SP_1498 against 19f.  Found phosphomannomutase with 99% percent 
#   identify:  SPT_1435.

#   Misannotation.  Assigning SPT_1435 as homolog to SP_1498 as a phospho-
#   glucomutase.
Reaction('PHOSPHOGLUCMUT-RXN',
         reactants=['GLC-1-P'],
         reversible='REVERSIBLE',
         products=['ALPHA-GLC-6-P'],
         minors=[],
         ec=['EC-5.4.2.5', 'EC-5.4.2.2'],
         biocyc='PHOSPHOGLUCMUT-RXN',
         biocyc_modified=True)
EnzymeAssociation(['EC-5.4.2.5', 'EC-5.4.2.2'], 'SP_1498') # tigr4
EnzymeAssociation(['EC-5.4.2.5', 'EC-5.4.2.2'], 'SPD_1326') # d39
EnzymeAssociation(['EC-5.4.2.5', 'EC-5.4.2.2'], 'SPT_1435') # d39
Homolog(['SP_1498'], ['SPD_1326'], ['SPT_1435'])

#2.7.1.2
#  biocyc has two enzymes for 19f:  SPT_1614 and SPT_0692.
#  SPT_0692 is the identical glucokinase 99%PI, zero gaps by blast
#  SPT_1614 is false positive -- 28%PI, 10% gaps
#
#  Misannotation -- SPT_1614 is not a glucokinase
Reaction('ALPHA-GLUCOKIN-RXN',
         reactants=['ALPHA-GLUCOSE', 'ATP'],
         reversible='LEFT-TO-RIGHT',
         products=['ALPHA-GLC-6-P', 'ADP', 'PROTON'],
         minors=['ATP', 'ADP', 'PROTON'],
         ec=['EC-2.7.1.2'],
         biocyc='GLUCOKIN-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-2.7.1.2', 'SPT_0692') # t19f
EnzymeAssociation('EC-2.7.1.2', 'SP_0668') # tigr4
EnzymeAssociation('EC-2.7.1.2', 'SPD_0580') # d39
Homolog(['SPT_0692'], ['SP_0668'], ['SPD_0580'])

Reaction('BETA-GLUCOKIN-RXN',
         reactants=['BETA-GLUCOSE', 'ATP'],
         reversible='LEFT-TO-RIGHT',
         products=['BETA-GLC-6-P', 'ADP', 'PROTON'],
         minors=['ATP', 'ADP', 'PROTON'],
         ec=['EC-2.7.1.2'],
         biocyc='GLUCOKIN-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-2.7.1.2', 'SPT_0692') # t19f
EnzymeAssociation('EC-2.7.1.2', 'SP_0668') # tigr4
EnzymeAssociation('EC-2.7.1.2', 'SPD_0580') # d39
Homolog(['SPT_0692'], ['SP_0668'], ['SPD_0580'])

#5.1.3.3
#  change to reflect alpha/beta glucose differences
Reaction('ALDOSE-1-EPIMERASE-RXN',
         reactants=['ALPHA-GLUCOSE'],
         reversible='REVERSIBLE',
         products=['BETA-GLUCOSE'],
         minors=[],
         ec=['EC-5.1.3.3'],
         biocyc='ALDOSE-1-EPIMERASE-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-5.1.3.3', 'SPT_0103') # t19f
EnzymeAssociation('EC-5.1.3.3', 'SP_0066') # tigr4
EnzymeAssociation('EC-5.1.3.3', 'SPD_0071') # d39
Homolog(['SPT_0103'], ['SP_0066'], ['SPD_0071'])

#5.3.1.9
#  change to reflect alpha/beta glucose differences
Reaction('G6P-FRUC-ISOM-ALPHA-RXN',
         reactants=['ALPHA-GLC-6-P'],
         reversible='REVERSIBLE',
         products=['FRUCTOSE-6P'],
         minors=[],
         ec=['EC-5.3.1.9'],
         biocyc='RXN-6182',
         biocyc_modified=True)

Reaction('G6P-FRUC-ISOM-BETA-RXN',
         reactants=['BETA-GLC-6-P'],
         reversible='REVERSIBLE',
         products=['FRUCTOSE-6P'],
         minors=[],
         ec=['EC-5.3.1.9'],
         biocyc='PGLUCISOM-RXN',
         biocyc_modified=True)

#  Biocyc uses 5.1.3.15 as the epimerase, while kegg lists 5.3.1.9 as also
#  performing this reaction -- as a non-enzymatic, spontaneous reaction.
#  This rxn is enzyme-associated in ecoli (b1780, yeaD) D-hexose-6-phosphate
#  epimerase.  Blasting this against spn does not yield any hits.
#
#  Do not include 5.1.3.15 in the model, but assign this functionality to
#  5.3.1.9.
Reaction('G6P-EPIMERASE-RXN',
         reactants=['ALPHA-GLC-6-P'],
         reversible='REVERSIBLE',
         products=['BETA-GLC-6-P'],
         minors=[],
         ec=['EC-5.3.1.9'],
         biocyc='GLUCOSE-6-PHOSPHATE-1-EPIMERASE-RXN',
         biocyc_modified=True)

EnzymeAssociation('EC-5.3.1.9', 'SPT_2081') # t19f
EnzymeAssociation('EC-5.3.1.9', 'SP_2070') # tigr4
EnzymeAssociation('EC-5.3.1.9', 'SPD_1897') # d39
Homolog(['SPT_2081'], ['SP_2070'], ['SPD_1897'])

#2.7.1.41 -- not in biocyc or kegg
#3.1.3.9 -- not in biocyc or kegg

#3.2.1.86 -- not including since only related to Arbutin/Salicin transport

#2.7.1.11
#AUTOADD 6PFRUCTPHOS-RXN
Reaction('6PFRUCTPHOS-RXN',
         reactants=['ATP', 'FRUCTOSE-6P'],
         reversible='LEFT-TO-RIGHT',
         products=['PROTON', 'ADP', 'FRUCTOSE-16-DIPHOSPHATE'],
         minors=['ATP', 'ADP', 'PROTON'],
         ec=['EC-2.7.1.11'],
         biocyc='6PFRUCTPHOS-RXN')
EnzymeAssociation('EC-2.7.1.11', 'SPT_1303') # t19f
EnzymeAssociation('EC-2.7.1.11', 'SP_0896') # tigr4
EnzymeAssociation('EC-2.7.1.11', 'SPD_0789') # d39
Homolog(['SPT_1303'], ['SP_0896'], ['SPD_0789'])

#3.1.3.11
#  F1,6P phosphatase II from bsu (BSU37090, glpX) not found in spn.
#  F1,6P phosphatase I  from bsu (BSU40190, fbp) not found in spn.
#
#  This enzyme is not present in spn.

#4.1.2.13
#AUTOADD F16ALDOLASE-RXN
Reaction('F16ALDOLASE-RXN',
         reactants=['FRUCTOSE-16-DIPHOSPHATE'],
         reversible='REVERSIBLE',
         products=['DIHYDROXY-ACETONE-PHOSPHATE', 'GAP'],
         minor=[],
         ec=['EC-4.1.2.13'],
         biocyc='F16ALDOLASE-RXN')

#  biocyc did not have reversibility for this reaction; reversible in kegg.
Reaction('RXN-8631',
         reactants=['FRU1P'],
         reversible='REVERSIBLE',
         products=['DIHYDROXY-ACETONE-PHOSPHATE', 'GLYCERALD'],
         minors=[],
         ec=['EC-4.1.2.13'],
         biocyc='RXN-8631',
         biocyc_modified=True)

EnzymeAssociation('EC-4.1.2.13', 'SPT_0631') # t19f
EnzymeAssociation('EC-4.1.2.13', 'SP_0605') # tigr4
EnzymeAssociation('EC-4.1.2.13', 'SPD_0526') # d39
Homolog(['SPT_0631'], ['SP_0605'], ['SPD_0526'])

#5.3.1.1
#AUTOADD TRIOSEPISOMERIZATION-RXN
Reaction('TRIOSEPISOMERIZATION-RXN',
         reactants=['GAP'],
         reversible='REVERSIBLE',
         products=['DIHYDROXY-ACETONE-PHOSPHATE'],
         minors=[],
         ec=['EC-5.3.1.1'],
         biocyc='TRIOSEPISOMERIZATION-RXN')
EnzymeAssociation('EC-5.3.1.1', 'SPT_1514') # t19f
EnzymeAssociation('EC-5.3.1.1', 'SP_1574') # tigr4
EnzymeAssociation('EC-5.3.1.1', 'SPD_1404') # d39
Homolog(['SPT_1514'], ['SP_1574'], ['SPD_1404'])

#1.2.1.12
#  Biocyc has no hit for t19f, and two for tigr4 (SP_1119 & SP_2012).
#  Bsu has two glyceraldehyde 3-phosphate dehydrogenases:
#     BSU29020 (gapB) -- only hit is SP_2012
#     BSU33940 (gapA) -- only hit is SP_2012
#  SP_1119 hits BSU02470 (ycbD) and BSU07350 (yfmT), both are aldehyde
#  dehydrogenases (1.2.1.26 and 1.2.1.3).
#
#  Blasted SP_2012 against t19f, found exact match for SPT_2008.
#
#  SP_1119 is mis-annotated and should be associated with 1.2.1.9?
#  SPT_2008 is the t19f equivalent.
Reaction('GAPOXNPHOSPHN-RXN',
         reactants=['GAP', 'Pi', 'NAD'],
         reversible='REVERSIBLE',
         products=['PROTON', 'DPG', 'NADH'],
         minors=['Pi', 'NAD', 'PROTON', 'NADH'],
         pairs=[('GAP', 'DPG'), ('NAD', 'NADPH')],
         ec=['EC-1.2.1.12'],
         biocyc='GAPOXNPHOSPHN-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-1.2.1.12', 'SP_2012') # tigr4
EnzymeAssociation('EC-1.2.1.12', 'SPD_1823') # d39
EnzymeAssociation('EC-1.2.1.12', 'SPT_2008') # t19f
Homolog(['SP_2012'], ['SPD_1823'], ['SPT_2008'])

#1.2.1.9
#  t19f
#     SPT_1165 -- match in kegg
#  d39
#     SPD_1823 -- annotated to (gapdh)
#     SPD_1004 -- match in kegg (gapN)
#  tigr4
#     SP_1119 -- match in kegg
#     SP_2012 -- annotated to 1.2.1.12 (gapdh)
#  SPT_1165, SP_1119, and SPD_1004 and perfect matches.
#  SP_1119 does not hit SPD_1823 or SP_2012
#
#  SPD_1823 and SP_2012 are misannotated and not associated with 1.2.1.9.
#  No biocyc reversibility; kegg says irreversible.
Reaction('1.2.1.9-RXN',
         reactants=['GAP', 'NADP', 'WATER'],
         reversible='LEFT-TO-RIGHT',
         products=['PROTON', 'G3P', 'NADPH'],
         minors=['NADP', 'WATER', 'PROTON', 'NADPH'],
         pairs=[('GAP', 'G3P'), ('NADP', 'NADPH')],
         ec=['EC-1.2.1.9'],
         biocyc='1.2.1.9-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-1.2.1.9', 'SPT_1165') # t19f
EnzymeAssociation('EC-1.2.1.9', 'SP_1119') # tigr4
EnzymeAssociation('EC-1.2.1.9', 'SPD_1004') # d39
Homolog(['SPT_1165'], ['SP_1119'], ['SPD_1004'])

#2.7.2.3
#AUTOADD PHOSGLYPHOS-RXN
Reaction('PHOSGLYPHOS-RXN',
         reactants=['G3P', 'ATP'],
         reversible='REVERSIBLE',
         products=['DPG', 'ADP'],
         ec=['EC-2.7.2.3'],
         biocyc='PHOSGLYPHOS-RXN')
EnzymeAssociation('EC-2.7.2.3', 'SPT_0536') # t19f
EnzymeAssociation('EC-2.7.2.3', 'SP_0499') # tigr4
EnzymeAssociation('EC-2.7.2.3', 'SPD_0445') # d39
Homolog(['SPT_0536'], ['SP_0499'], ['SPD_0445'])

#5.4.2.11
#  5.4.2.1 was split into 5.4.2.11 and 5.4.2.12.  5.4.2.11 is glycerate-2,3P2
#  dependent.  These enzymes can also catalyze 5.4.2.4 and 3.1.3.13, although
#  the rates may differ for all three reactions.
Reaction('3PGAREARR-DEP-RXN',
         reactants=['2-PG'],
         reversible='REVERSIBLE',
         products=['G3P'],
         cofactors=['23-DIPHOSPHYGLYCERATE'],
         minors=[],
         ec=['EC-5.4.2.12'],
         biocyc='3PGAREARR-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-5.4.2.11', 'SPT_1595') # t19f
EnzymeAssociation('EC-5.4.2.11', 'SP_1655') # tigr4
EnzymeAssociation('EC-5.4.2.11', 'SPD_1468') # d39
Homolog(['SPT_1595'], ['SP_1655'], ['SPD_1468'])

#5.4.2.4
#  No reversibility by biocyc; kegg says reversible.
#  See comments for 5.4.2.11.
Reaction('BISPHOSPHOGLYCERATE-MUTASE-RXN',
         reactants=['DPG'],
         reversible='REVERSIBLE',
         products=['PROTON', '23-DIPHOSPHOGLYCERATE'],
         minors=['PROTON'],
         ec=['EC-5.4.2.4'],
         biocyc='BISPHOSPHOGLYCERATE-MUTASE-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-5.4.2.4', 'SPT_1595') # t19f
EnzymeAssociation('EC-5.4.2.4', 'SP_1655') # tigr4
EnzymeAssociation('EC-5.4.2.4', 'SPD_1468') # d39

#3.1.3.13
#  Biocyc uses the same enzymes as for the glycerate-2,3P2 independent rxn,
#  but it should use the dependent ones.
#
#  Change annotation to match 5.4.2.11 rather than 5.4.2.12.
#  Changed biocyc reversibility from PHYSIOL-LEFT-TO-RIGHT to LEFT-TO-RIGHT.
Reaction('BISPHOSPHOGLYCERATE-PHOSPHATASE-RXN',
         reactants=['WATER', '23-DIPHOSPHOGLYCERATE'],
         reversible='LEFT-TO-RIGHT',
         products=['Pi', 'G3P'],
         minors=['WATER', 'Pi'],
         ec=['EC-3.1.3.13'],
         biocyc='BISPHOSPHOGLYCERATE-PHOSPHATASE-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-3.1.3.13', 'SPT_1595') # t19f
EnzymeAssociation('EC-3.1.3.13', 'SP_1655') # tigr4
EnzymeAssociation('EC-3.1.3.13', 'SPD_1468') # d39

#5.4.2.12
#  Biocyc and kegg agree on annotation except SPT_0062, which biocyc adds for
#  t19f.
#  SPT_0062 is annotates as "phosphoglycerate mutase family protein" with
#  low similarity to SPT_1220 (E=0.027).  No hits to SPT_1595 or SPT_0286.
#  Kegg does not include SPT_0062 for 5.4.2.12.
#
#  No evidence that enzymes form complex.  Assume isozymes.
#
#  Requires Mn2+ cofactor. [PMID:10764795]
#  Removed annotation between SPT_0062 and 5.4.2.12.
Reaction('3PGAREARR-IND-RXN',
         reactants=['2-PG'],
         reversible='REVERSIBLE',
         products=['G3P'],
         cofactors=['MN'],
         minors=[],
         ec=['EC-5.4.2.12'],
         biocyc='3PGAREARR-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-5.4.2.12', SPT_0286 | SPT_1220) # t19f
EnzymeAssociation('EC-5.4.2.12', SP_0240 | SP_0984) # tigr4
EnzymeAssociation('EC-5.4.2.12', SPD_0222 | SPD_0870) # d39
Homolog(['SPT_0286', 'SPT_1220'], 
        ['SP_0240', 'SP_0984'],
        ['SPD_0222', 'SPD_0870'])

#4.2.1.11
#AUTOADD 2PGADEHYDRAT-RXN
Reaction('2PGADEHYDRAT-RXN',
         reactants=['2-PG'],
         reversible='REVERSIBLE',
         products=['PHOSPHO-ENOL-PYRUVATE', 'WATER'],
         minors=['WATER'],
         ec=['EC-4.2.1.11'],
         biocyc='2PGADEHYDRAT-RXN')
EnzymeAssociation('EC-4.2.1.11', 'SPT_1173') # t19f
EnzymeAssociation('EC-4.2.1.11', 'SP_1128') # tigr4
EnzymeAssociation('EC-4.2.1.11', 'SPD_1012') # d39
Homolog(['SPT_1173'], ['SP_1128'], ['SPD_1012'])

#2.7.1.40
#AUTOADD PEPDEPHOS-RXN
Reaction('PEPDEPHOS-RXN',
         reactants=['PYRUVATE', 'ATP'],
         reversible='RIGHT-TO-LEFT',
         products=['PROTON', 'PHOSPHO-ENOL-PYRUVATE', 'ADP'],
         minors=['ATP', 'ADP', 'PROTON'],
         pairs=[('ATP', 'ADP')],
         ec=['EC-2.7.1.40'],
         biocyc='PEPDEPHOS-RXN')
EnzymeAssociation('EC-2.7.1.40', 'SPT_1302') # t19f
EnzymeAssociation('EC-2.7.1.40', 'SP_0897') # tigr4
EnzymeAssociation('EC-2.7.1.40', 'SPD_0790') # d39
Homolog(['SPT_1302'], ['SP_0897'], ['SPD_0790'])

#1.1.1.27
#AUTOADD L-LACTATE-DEHYDROGENASE-RXN
Reaction('L-LACTATE-DEHYDROGENASE-RXN',
         reactants=['L-LACTATE', 'NAD'],
         reversible='RIGHT-TO-LEFT',
         products=['PYRUVATE', 'NADH', 'PROTON'],
         minors=['NAD', 'NADPH', 'PROTON'],
         pairs=[('NAD', 'NADPH')],
         ec=['EC-1.1.1.27'],
         biocyc='L-LACTATE-DEHYDROGENASE-RXN')
EnzymeAssociation('EC-1.1.1.27', 'SPT_1008') # t19f
EnzymeAssociation('EC-1.1.1.27', 'SP_1220') # tigr4
EnzymeAssociation('EC-1.1.1.27', 'SPD_1078') # d39
Homolog(['SPT_1008'], ['SP_1220'], ['SPD_1078'])

#4.1.1.31
#  Kegg map only shows 4.1.1.32 and 4.1.1.49, which go in opposite direction.
#AUTOADD PEPCARBOX-RXN
Reaction('PEPCARBOX-RXN',
         reactants=['Pi', 'OXALACETIC_ACID'],
         reversible='RIGHT-TO-LEFT',
         products=['PHOSPHO-ENOL-PYRUVATE', 'HCO3'],
         minors=['Pi', 'HCO3'],
         ec=['EC-4.1.1.31'],
         biocyc='PEPCARBOX-RXN',
         biocyc_modified=True)
EnzymeAssociation('EC-4.1.1.31', 'SPT_1111') # t19f
EnzymeAssociation('EC-4.1.1.31', 'SP_1068') # tigr4
EnzymeAssociation('EC-4.1.1.31', 'SPD_0953') # d39
Homolog(['SPT_1111'], ['SP_1068'], ['SPD_0953'])

#1.2.7.1
#  Included in biocyc but non-enzymatic.  Not in kegg.

#1.2.4.1


