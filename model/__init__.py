
from pprint import pprint

from CellScribe import *
from CellScribe.foundation import Added

model = Model("TIGR4")
Added.set_model(model)

from metabolism.transport import *

model.summary(showall=True)

#pprint(dir())
