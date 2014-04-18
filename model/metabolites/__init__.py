
from CellScribe import *

from aminoacids import *

atp = Metabolite("atp")
adp = Metabolite("adp")
amp = Metabolite("amp")
MinorSuggestions(atp, adp, amp)
PairSet(atp, adp, amp)

phosphate = Metabolite("phosphate", kegg="C00009")
diphosphate = Metabolite("diphosphate", kegg="C00013")
MinorSuggestions(phosphate, diphosphate)

h2o = Metabolite("h2o", kegg="C00001")
MinorSuggestion(h2o)




