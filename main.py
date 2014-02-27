from CellScribe import *

# TYPE ANYTHING


extracellular = Location("Extracellular", 'e')
e = extracellular.localizer

cytoplasm = Location("Cytoplasm", 'c')
c = cytoplasm.localizer
Metabolite.default_location = cytoplasm


atp = Metabolite("atp")
adp = Metabolite("adp")
glucose = Metabolite("glucose")
glucose6phosphate = Metabolite("glucose6phosphate")

glucokinase = Reaction(name="glucosekinase",
                       reactants=glucose + atp,
                       products=glucose6phosphate + adp,
                       pairs=[(glucose, glucose6phosphate), (atp, adp)],
                       minors=[atp, adp])

SP_0068 = Gene("SP_0068")
glucokinase_GA = GeneAssociation(glucokinase, SP_0068)

glucose_transport1 = Reaction(name="glucose_transport1",
                              reactants=e(glucose) + atp,
                              products=glucose + adp,
                              pairs=[(atp, adp)],
                              minors=[atp, adp])

SP_1000 = Gene("SP_1000")
SP_1001 = Gene("SP_1001")
SP_1002 = Gene("SP_1002")

glucose_transport1_GA = GeneAssociation(glucose_transport1, SP_1000 & (SP_1001 | SP_1002))






if __name__ == "__main__":
    print glucokinase
    #print glucokinase_GA

    #print glucose_transport1
    #print glucose_transport1_GA
