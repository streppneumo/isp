
from pprint import pprint, pformat

import pythoncyc
from pythoncyc.PToolsFrame import PFrame

pgdb = dict()
pgdb['tigr4'] = pythoncyc.select_organism('spne170187')
pgdb['d39'] = pythoncyc.select_organism('spne373153')
pgdb['t19f'] = pythoncyc.select_organism('spne487213')


def show_gpr(db, rxn):
    rframe = PFrame(rxn, db)
    if rframe is not None and rframe.enzymatic_reaction is not None:
        for er in rframe.enzymatic_reaction:
            erframe = PFrame(er, db)
            print "   " + er
            pframe = PFrame(erframe.enzyme, db)
            genes = [PFrame(g, db).accession_1 for g in pframe.gene]
            print "      " + erframe.enzyme + ' -- ' + " ".join(genes)


def show_gprs(rxn):
    for db in pgdb:
        print db
        show_gpr(pgdb[db], rxn)


def build_python_command(command, *args, **kwargs):
    args_str = [pformat(arg) for arg in args]
    kwargs_str = [k+'='+pformat(v) for (k, v) in kwargs.items()]

    one_liner = command + '(' + ", ".join(args_str + kwargs_str) + ')'
    if len(one_liner) <= 80:
        return one_liner

    indent = len(command) + 1
    s = command + '(' + (",\n"+(" "*indent)).join(args_str + kwargs_str) + ')'
    return s


def convert_biocyc_strs(strs):
    if type(strs) in (tuple, list):
        return [convert_biocyc_strs(s) for s in strs]
    elif type(strs) in (str, unicode):
        return str(strs.strip('|'))
    else:
        return strs


def build_python_command_biocyc(command, *args, **kwargs):
    args = convert_biocyc_strs(args)
    for k, v in kwargs.items():
        kwargs[k] = convert_biocyc_strs(v)
    return build_python_command(command, *args, **kwargs)


def get_genes(rxn):
    genes = dict()
    for db in pgdb:
        rframe = PFrame(rxn, pgdb[db])
        if rframe is None or rframe.enzymatic_reaction is None:
            continue
        for er in rframe.enzymatic_reaction:
            erframe = PFrame(er, pgdb[db])
            pframe = PFrame(erframe.enzyme, pgdb[db])
            genes[db] = [PFrame(g, pgdb[db]).accession_1 for g in pframe.gene]
    return genes


def biocyc_rxn_to_cellscribe(rxn):
    r = PFrame(rxn, pgdb['tigr4'])
    s = build_python_command_biocyc("Reaction",
                                    rxn,
                                    reactants=r.left,
                                    products=r.right,
                                    reversible=r.reaction_direction,
                                    ec=r.ec_number,
                                    biocyc=rxn) + "\n"
    genes = get_genes(rxn)
    ec = r.ec_number
    if len(ec) == 1:
        ec = ec[0]
    for db in genes:
        if genes[db]:
            g = genes[db]
            if len(g) == 1:
                g = g[0]
            s += build_python_command_biocyc("EnzymeAssociation",
                                             ec,
                                             g) + " # " + db + "\n"
    if any([len(g) for g in genes.values()]):
        s += build_python_command_biocyc("Homolog",
                                         *[x for x in genes.values() if x])
    return s


def start_shell(filename):
    input = "not !"
    rxn = None
    while input.rstrip() != "!":
        input = raw_input("> ").rstrip()
        if input == '.':
            f = open(filename, 'a')
            f.write("#AUTOADD " + rxn + "\n")
            f.write(biocyc_rxn_to_cellscribe(rxn))
            f.write("\n\n")
            f.close()
            print "Reaction " + rxn + " written to " + filename + "\n"
        elif input == '!':
            break
        else:
            rxn = input
            show_gprs(rxn)
            print " "
            print biocyc_rxn_to_cellscribe(rxn)
            print " "


if __name__ == "__main__":
    #show_gpr(pgdb['d39'], 'D-PPENTOMUT-RXN')
    #show_gprs('D-PPENTOMUT-RXN')
    #print biocyc_rxn_to_cellscribe('D-PPENTOMUT-RXN')
    start_shell("../model/metabolism/pathways/AminoAcids.py")


