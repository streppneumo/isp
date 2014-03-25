
from pprint import pprint
import collections

from parsing import load_dat_file, to_dict, to_safe_name

GENE_OUTPUT_FILENAME = "OUT_genes.py"
OPERON_OUTPUT_FILENAME = "OUT_operons.py"
SHOW_SINGLE_OPERONS = False

gene_data = to_dict(load_dat_file("spne170187cyc/genes.dat"))
operon_data = load_dat_file("spne170187cyc/transunits.dat")

biocyc_to_accession = {k : v['ACCESSION-1'] for k, v in gene_data.items()}

pseudogenes = set()
for d in operon_data:
    pseuds = set([b for b in d['COMPONENTS'] if b not in biocyc_to_accession])
    pseudogenes = pseudogenes | pseuds


with open(GENE_OUTPUT_FILENAME, 'w') as f:
    common_names = collections.defaultdict(list)
    print >>f, "from CellScribe import Gene, Pseudogene\n"
    for key, d in gene_data.items():
        if d['ACCESSION-1']:
            var_name = d['ACCESSION-1']
            gene_name = var_name
        else:
            var_name = to_safe_name(key, prefix='g')
            gene_name = key
        biocyc_name = key

        template = '{v} = Gene("{g}", biocyc="{b}")'
        print >>f, template.format(v=var_name, g=gene_name, b=biocyc_name)

        if d['COMMON-NAME'] and d['COMMON-NAME'] != d['ACCESSION-1']:
            name = to_safe_name(d['COMMON-NAME'], prefix='g')
            common_names[name].append(var_name)

    print >>f, "\n"
    for name, var_names in common_names.items():
        var_name = " | ".join(var_names)
        print >>f, '{n} = {v}'.format(n=name, v=var_name)

    print >>f, "\n"
    template = '{v} = Pseudogene("{b}", biocyc="{b}")'
    for pseudo in pseudogenes:
        name = to_safe_name(pseudo, prefix='g')
        print >>f, template.format(v=name, b=pseudo)


with open(OPERON_OUTPUT_FILENAME, 'w') as f:
    import_file = GENE_OUTPUT_FILENAME[0:-3]  # strip ".py" extension
    print >>f, "from CellScribe import Operon"
    print >>f, "from {gf} import *\n".format(gf=import_file)
    for d in operon_data:
        vars = []
        for var in d['COMPONENTS']:
            if (var in biocyc_to_accession and
                    biocyc_to_accession[var] is not None):
                vars.append(biocyc_to_accession[var])
            else:
                vars.append(to_safe_name(var, prefix='g'))
        if SHOW_SINGLE_OPERONS or len(vars) > 1:
            name = to_safe_name(d['UNIQUE-ID'])
            template = 'Operon("{u}", [{v}], biocyc="{u}")'
            print >>f, template.format(v=", ".join(vars), u=d['UNIQUE-ID'])

#pprint(biocyc_to_accession)



