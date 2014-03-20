
from pprint import pprint
import re
import keyword


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


if __name__ == '__main__':
    pprint(load_col_file('test/enzymes.col')[0:3])
