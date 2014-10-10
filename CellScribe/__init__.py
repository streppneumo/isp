"""
Describe whole-cell biology.

Modules
-------

foundation:
    Model objects are either Primitive or Composite.  Primitive objects are the
    basic units of cell biology (metabolites, genes, etc.).  Composite objects
    are assembled from one or more other objects.  Examples of Composite
    objects are reactions (containing multiple metabolites) and gene
    associations (containing a reaction and at least one gene).

    Some objects are Named and are associated with a unique string identifier.
    All Primitive objects, but only some Composite objects, are Named.

registry:
    After objects are created, they must stored in the model's registry.  If an
    object is never registered, it will not be included in the model.  Objects
    are registered in two ways:

    1. Named objects (and by extension, Primitive objects) are registered
    automatically when the Named or Primitive constructors are called.

    2. Composite objects can register themselves by subclassing Registered and
    calling self.register().  If a Composite object is Named, it is best to
    register by calling Named.__init__().  Any Composite object that is part
    of a registered Composite object will be anonymously registered; it is not
    necessary to separately register these objects.  In general, Composite
    objects only need to be registered if they are not named and do not a
    member of any other registered Composite object.

logic:





"""

from expression import (Gene,
                        Pseudogene,
                        RNA,
                        Protein,
                        Complex,
                        Operon)

from reaction import (Metabolite,
                      Reaction,
                      MinorSuggestion,
                      MinorSuggestions,
                      PairSet)

from location import Location

from association import GeneAssociation

from logic import (If,
                   Iff)

from model import Model


