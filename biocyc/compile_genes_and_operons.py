
from pprint import pprint
from parsing import load_dat_file, to_dict, to_safe_name

gene_data = to_dict(load_dat_file("spne170187cyc/genes.dat"))
operon_data = load_dat_file("spne170187cyc/transunits.dat")

biocyc_to_accession = {k : v['ACCESSION-1'] for k, v in gene_data.items()}


with open("OUT_genes.py", 'w') as f:
    for k, d in gene_data.items():
        if d['ACCESSION-1']:
            varname = d['ACCESSION-1']
        else:
            varname = to_safe_name(k, prefix='g')
        biocycname = k

        template = '{v} = Gene("{v}", biocyc="{b}")'
        print >>f, template.format(v=varname, b=biocycname)

        if d['COMMON-NAME'] and d['COMMON-NAME'] != d['ACCESSION-1']:
            name = to_safe_name(d['COMMON-NAME'], prefix='g')
            print >>f, '{n} = {v}'.format(n=name, v=varname)


with open("OUT_operons.py", 'w') as f:
    for d in operon_data:
        vars = []
        for var in d['COMPONENTS']:
            if (var in biocyc_to_accession and
                        biocyc_to_accession[var] is not None):
                vars.append(biocyc_to_accession[var])
            else:
                vars.append(to_safe_name(var, prefix='g'))
        name = to_safe_name(d['UNIQUE-ID'])
        template = '{n} = Operon([{v}], biocyc="{u}")'
        print >>f, template.format(n=name, v=", ".join(vars), u=d['UNIQUE-ID'])

pprint(biocyc_to_accession)



