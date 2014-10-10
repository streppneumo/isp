
from pprint import pprint

from primitives import *


def is_indented(line):
    return len(line) > len(line.lstrip())


def is_empty(line):
    is_comment = line.lstrip().startswith('#')
    is_blank = len(line.lstrip()) == 0
    return is_comment or is_blank


def parse_sub_line(line):
    pieces = line.split()
    key = pieces[0]
    values = []
    if pieces[1] == '$':
        values = Verbatim(" ".join(pieces[2:]))
    else:
        in_paren = False
        group = []
        for val in pieces[1:]:
            if val.startswith('('):
                in_paren = True
                val = val[1:]
            if val.endswith(')'):
                group.append(val[:-1])
                values.append(group)
                group = []
                in_paren = False
            else:
                if in_paren:
                    group.append(val)
                else:
                    values.append(val)
    return key, values


def load_reaction_file(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]
    pairs = []
    current_head = None
    current_subs = []
    for line in lines:
        if is_empty(line):
            continue
        if not is_indented(line):
            if current_head is not None:
                subs = dict([parse_sub_line(l) for l in current_subs])
                pairs.append((current_head, subs))
            current_head = line
            current_subs = []
        else:
            current_subs.append(line)
    return pairs


if __name__ == '__main__':
    pprint(load_reaction_file('/Users/jensen/Dropbox/bc/isp/model/metabolism/preparsed/arginineprolinemetabolism'))
