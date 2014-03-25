from CellScribe import *

extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm

#not code, just associations
SP_1961 beta_subunit
SP_1960 beta_prime_subunit  
SP_0236 alpha_subunit
SP_1737 omega_subunit
SP_0493 delta_subunit
