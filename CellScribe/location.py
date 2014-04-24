
class LocalizingError(Exception):
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return repr(self.obj) + " cannot be localized."


class Location(object):
    def __init__(self, name, abbreviation=None):
        self.name = name
        self.abbreviation = abbreviation

    def __str__(self):
        if self.abbreviation:
            return "{name}[{abbrev}]".format(name=self.name,
                                             abbrev=self.abbreviation)
        else:
            return self.name

    @property
    def suffix(self):
        if self.abbreviation:
            return "[" + self.abbreviation + "]"
        else:
            return "[" + self.name + "]"

    @property
    def localizer(self):
        def loc_aux(x):
            if not isinstance(x, Localizable):
                raise LocalizingError(x)
            else:
                return x.localize(self)
        return loc_aux


class Localizable(object):
    default_location = None

    # The default constructor is Localized, which is a subclass of
    # Localizable.  We set it below since these classes are mutually
    # recursive.
    localized_constructor = None

    def localize(self, location=None):
        if location is None:
            location = self.default_location
        return self.localized_constructor(self, location)


class Localized(Localizable):
    def __init__(self, obj, location):
        self.obj = obj
        self.location = location

    def localize(self, location=None):
        if location is None:
            return self
        else:
            return self.obj.localize(location)

    def __str__(self):
        return str(self.obj) + self.location.suffix


Localizable.localized_constructor = Localized  # see definition above


if __name__ == '__main__':
    class LocalizedMetabolite(Localized):
        def __init__(self, name):
            self.name = name


    class Metabolite(Localizable):
        localized_constructor = LocalizedMetabolite

        def __init__(self, name):
            self.name = name


    lm = LocalizedMetabolite("localmet")
    m = Metabolite("met")
    print lm
    print m
    print m.localize()


