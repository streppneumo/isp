
from pprint import pprint
import collections

import re
import keyword


GENE_OUTPUT_FILENAME = "OUT_genes.py"
OPERON_OUTPUT_FILENAME = "OUT_operons.py"

GENE_INPUT_FILENAME = "spne487213cyc/genes.dat"
OPERON_INPUT_FILENAME = "spne487213cyc/transunits.dat"

SHOW_SINGLE_OPERONS = False

# ================= parsing functions ====================

def parse_line(line):
    # "KEY1 - VALUE1"
    left, _, right = line.rstrip().partition(' - ')
    return left, right


def parse_group(lines):
    # [ [(k1,v1), (k2,v2), ...], ... ]
    d = dict()
    for name, value in lines:
        #name, value = parse_line(line)
        if name in d:
            if isinstance(d[name], list):
                d[name].append(value)
            else:
                d[name] = [d[name], value]
        else:
            d[name] = value
    return d


def normalize_lists(groups):
    # if any key contains a list in any group, set corresponding entries
    # in all groups to be a list
    keys = set()
    plural = set()
    for group in groups:
        keys = keys | set(group.keys())
        plural = plural | set([k for k in group if isinstance(group[k], list)])
    for group in groups:
        for key in keys:
            if key not in group:
                group[key] = None
        for key in plural:
            if group[key] is None:
                group[key] = []
            elif not isinstance(group[key], list):
                group[key] = [group[key]]
    return groups


def load_dat_file(filename):
    with open(filename) as f:
        groups = []
        current = []
        for line in f:
            if line.startswith('#'):
                continue
            if line.startswith('//'):
                groups.append(current)
                current = []
            else:
                current.append(parse_line(line.rstrip()))
    return normalize_lists([parse_group(group) for group in groups])


def load_col_file(filename, sep="\t"):
    with open(filename) as f:
        groups = []
        for line in f:
            if line.startswith('#'):
                continue
            headings = line.rstrip().split(sep)
            break
        for line in f:
            pairs = zip(headings, line.rstrip().split(sep))
            groups.append([(k, v) for k, v in pairs if v])
    return normalize_lists([parse_group(group) for group in groups])


def to_dict(data, key='UNIQUE-ID'):
    return {d[key] : d for d in data}


def is_unsafe_name(s):
    if keyword.iskeyword(s):
        return True
    else:
        return re.match('^[A-Za-z_]\w*$', s) is None


def to_safe_name(s, prefix='x'):
    s = s.replace(' ', '_')
    s = s.replace('-', '_')
    if not s[0].isalpha():
        s = prefix + s
    if is_unsafe_name(s):
        return "# UNSAFE NAME '{name}'".format(name=s)
    else:
        return s

# ================= main program ====================

gene_data = to_dict(load_dat_file(GENE_INPUT_FILENAME))
operon_data = load_dat_file(OPERON_INPUT_FILENAME)

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



