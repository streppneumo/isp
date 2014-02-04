
import lxml
import lxml.objectify as objectify
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

        self.root = self.tree.getroot()
        self.sent = True


if __name__ == '__main__':
    query = Query("http://websvc.biocyc.org/apixml?fn=enzymes-of-reaction&id=SPNE170187:PEPDEPHOS-RXN")
    query.send()
    print query.root.tag
