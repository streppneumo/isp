
import lxml
import lxml.objectify as objectify

import StringIO
import hashlib
import os
import urllib2


class Logger(object):
    show_log = True

    @staticmethod
    def log(fmt, **kwargs):
        if Logger.show_log:
            print fmt.format(**kwargs)


def log(fmt, **kwargs):
    Logger.log(fmt, **kwargs)


class Query(object):
    use_cache = True
    cache_dir = '/Users/jensen/Dropbox/bc/isp/cache'
    translate_tags = True  # convert hyphens to underscores in tag names

    def __init__(self, url):
        self.url = url
        self.tree = None
        self.root = None
        self.sent = False
        self.hash = hashlib.sha1(self.url).hexdigest()
        self.cached_filename = os.path.join(Query.cache_dir, self.hash + '.xml')

    @property
    def is_cached(self):
        return os.path.isfile(self.cached_filename)

    def send(self):
        log("sending Query for {url}", url=self.url)
        if Query.use_cache:
            if not self.is_cached:
                log("   no cache file for query")
                # create the cache file
                with open(self.cached_filename, 'w+') as f:
                    f.write(urllib2.urlopen(self.url).read())
                    log("   cache file {filename} created", filename=self.cached_filename)
            self.tree = objectify.parse(self.cached_filename)   # read the cached file
            log("   Query loaded from file {filename}", filename=self.cached_filename)

        else:
            # get directly from URL
            self.tree = objectify.parse(self.url)
            log("   data fetched from URL {url}", url=self.url)

        if Query.translate_tags:
            xml_string = lxml.etree.tostring(self.tree)
            doc = lxml.etree.XML(xml_string)
            for e in doc.xpath('//*[contains(local-name(),"-")]'):
                e.tag = e.tag.replace('-', '_')
            self.tree = objectify.parse(StringIO.StringIO(lxml.etree.tostring(doc)))

        self.root = self.tree.getroot()
        self.sent = True


def quick_query(url):
    query = Query(url)
    query.send()
    if query.root.tag == 'ptools-xml' or query.root.tag == 'ptools_xml':
        return query.root
    else:
        log("ERROR:  bad response from query {url}", url=url)

DEFAULT_SPECIES = 'SPNE170187'

def get_object(name, species=DEFAULT_SPECIES):
    url = 'http://websvc.biocyc.org/getxml?{species}:{name}'.format(species=species, name=name)
    return quick_query(url)

def get_objects(function, name, species=DEFAULT_SPECIES):
    url = 'http://websvc.biocyc.org/apixml?fn={fn}&id={species}:{name}&detail=full'
    return quick_query(url.format(fn=function, name=name, species=species))

def get_genes(name, species=DEFAULT_SPECIES):
    return get_objects('genes-of-reaction', name, species)

def get_reaction(name, species=DEFAULT_SPECIES):
    rxn = get_object(name, species)
    reactants = [l.Compound.get("frameid") for l in rxn.Reaction.left]
    products = [r.Compound.get("frameid") for r in rxn.Reaction.right]
    ec = str(rxn.Reaction.ec_number).rstrip()
    gpr = get_genes(name, species)
    genes = [g.common_name for g in gpr.Gene]

    log("Results for reaction {rxn}:", rxn=name)
    log("   Reactants:")
    for r in reactants:
        log("      "+r)
    log("   Products:")
    for p in products:
        log("      "+p)
    log("   EC Number: {ec}", ec=ec)
    log("   Genes:")
    for g in genes:
        log("      "+g)


if __name__ == '__main__':
    #query = Query("http://websvc.biocyc.org/apixml?fn=enzymes-of-reaction&id=SPNE170187:PEPDEPHOS-RXN")
    #query.send()
    #print query.root.tag
    get_reaction("PEPDEPHOS-RXN")