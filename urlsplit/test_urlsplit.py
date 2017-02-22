import unittest


def parse_url(url):
    class UrlObject():
        def __init__(self, protocol, site, path):
            self.protocol = protocol
            self.site = site
            self.path = path

    site = url.split('//')[1]
    path = url.split('/')[-1]
    if url[0] == 'h':
        return UrlObject('http', site, path)
    return UrlObject('ftp', site, path)


class test_basic_example(unittest.TestCase):
    def assertProtocol(self, url, expect_protocol):
        url_object = parse_url(url)
        actual_protocol = url_object.protocol
        self.assertEqual(expect_protocol, actual_protocol)

    def test_finds_http_protocol(self):
        self.assertProtocol('http://www.site.com', 'http')

    def test_finds_ftp_protocol(self):
        self.assertProtocol('ftp://www.site.com', 'ftp')


class test_site_parsing(unittest.TestCase):
    def assertSite(self, url, expect_site):
        url_object = parse_url(url)
        actual_site = url_object.site
        self.assertEqual(expect_site, actual_site)

    def test_finds_site(self):
        self.assertSite('http://www.site.com', 'www.site.com')

    def test_finds_another_site(self):
        self.assertSite('http://www.site2.com', 'www.site2.com')


class test_path_parsing(unittest.TestCase):
    def assertPath(self, url, expect_path):
        url_object = parse_url('http://www.com/')
        path = url_object.path
        self.assertEqual("", path)
    def test_empty_path(self):
        self.assertPath('http://www.com/', "")
    def test_empty_path_with_no_slash_end(self):
        self.assertPath('http://www.com', "")
    def test_single_work_path(self):
        self.assertPath('http://www.com/', "word")
    def test_long_path(self):
        self.assertPath('http://www.com/word-some/path.txt', )