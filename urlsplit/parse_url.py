def parse_url(url):
    class UrlObject():
        def __init__(self, protocol, site, path):
            self.protocol = protocol
            self.site = site
            self.path = path

    def parse_site_and_path(site_and_path):
        path_split = site_and_path.split('/')
        site, path_list = path_split[0], path_split[1:]
        return site, "/".join(path_list)

    protocol, site_and_path = url.split('://')
    site, path = parse_site_and_path(site_and_path)

    return UrlObject(protocol, site, path)
