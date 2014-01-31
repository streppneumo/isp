__author__ = 'Corey'

from CellScribe import *


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


atp = Metabolite("atp")
adp = Metabolite("adp")
