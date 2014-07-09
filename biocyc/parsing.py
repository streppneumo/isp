
from collections import defaultdict
from pprint import pprint
from warnings import warn


def consolidate_continued_lines(raw_lines):
    lines = []
    for line in raw_lines:
        if line.startswith('/') and line.rstrip() != '//':
            lines[-1] += line[1:]
        elif not line.startswith('#'):
            lines.append(line)
    return [line.rstrip() for line in lines]


def lines_to_records(lines):
    records = []
    current = []
    for line in lines:
        if line.rstrip() == '//':
            records.append(current)
            current = []
        else:
            current.append(line)
    return records


def consolidate_attributes(records):
    def consolidate(lines):
        sets = []
        attrs = []
        for i in range(len(lines)):
            if lines[i].startswith('^'):
                attrs.append((lines[i][1:], []))
            else:
                attrs = []
                sets.append((lines[i], attrs))
        return sets

    return [consolidate(record) for record in records]


class CycValue(object):
    def __init__(self, value, attributes=None, ref=None):
        self.value = value
        self.attributes = attributes
        self.ref = ref

    def __str__(self):
        return str(dict(value=self.value, attr=self.attributes, ref=self.ref))

    def __repr__(self):
        return str(self)


class PluralWarning(Warning):
    pass


class CycValueList(list):
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def check_length(self):
        if len(self.items) > 1:
            warn("Accessed property with multiple values.", PluralWarning)

    @property
    def ref(self):
        self.check_length()
        return self.items[0].ref

    @property
    def refs(self):
        return [item.ref for item in self.items]

    @property
    def value(self):
        self.check_length()
        return self.items[0].value

    @property
    def values(self):
        return [item.value for item in self.items]

    @property
    def attributes(self):
        self.check_length()
        return self.items[0].attributes

    # override for sequence type
    def append(self, obj):
        self.items.append(obj)

    def __len__(self):
        return self.items.__len__()

    def __getitem__(self, key):
        return self.items.__getitem__(key)

    def __setitem__(self, key, value):
        return self.items.__setitem__(key, value)

    def __delitem__(self, key):
        return self.items.__delitem__(key)

    def __iter__(self):
        return self.items.__iter__()

    def __reversed__(self):
        return self.items.__reversed__(self)

    def __contains__(self, item):
        return self.items.__contains__(item)

    def __getslice__(self, i, j):
        return self.items.__getslice__(i, j)

    def __setslice__(self, i, j, sequence):
        return self.items.__setslice__(i, j, sequence)

    def __delslice__(self, i, j):
        return self.items.__delslice__(i, j)


def parse_line(line):
    name, _, value = line.partition(' - ')
    return name, value


def parse_record(record):
    pairs = defaultdict(CycValueList)
    for line, attrs in record:
        name, value = parse_line(line)
        if not attrs:
            pairs[name].append(CycValue(value))
        else:
            pairs[name].append(CycValue(value, parse_record(attrs)))
    return dict(pairs)


def load_dat_file(filename):
    with open(filename) as f:
        records = lines_to_records(consolidate_continued_lines(f.readlines()))
        return [parse_record(r) for r in consolidate_attributes(records)]






if __name__ == '__main__':
    pprint(load_dat_file('spne170187cyc/reactions.dat')[0:4])