
from CellScribe import Metabolite

# inorganic minors
H2O = Metabolite("h2o")
PROTON = Metabolite("proton")

phosphate = Metabolite("phosphate")
pyrophosphate = Metabolite("pyrophosphate")
diphosphate = pyrophosphate

# high energy phosphates
ATP = Metabolite("atp")
ADP = Metabolite("adp")
AMP = Metabolite("amp")
GTP = Metabolite("gtp")
GDP = Metabolite("gdp")
GMP = Metabolite("gmp")
CTP = Metabolite("ctp")
CDP = Metabolite("cdp")
CMP = Metabolite("cmp")
TTP = Metabolite("ttp")
TDP = Metabolite("tdp")
TMP = Metabolite("tmp")

# carbohydrates
maltose = Metabolite("maltose")
maltodextrin = Metabolite("maltodextrin")
spermidine = Metabolite("spermidine", kegg="C00315")
putrescine = Metabolite("putrescine", kegg="C00134")
cellobiose = Metabolite("cellobiose", kegg="C00185")
chitobiose = Metabolite("chitobiose", kegg="C01674")
mannitol = Metabolite("manitol", kegg="C00392")
sucrose = Metabolite("sucrose", kegg="C00089")


# vitamins and cofactors
choline = Metabolite("choline", kegg="C00114")

# metals
zinc = Metabolite("zinc", kegg="C00038")
manganese = Metabolite("manganese", kegg="C00034")
