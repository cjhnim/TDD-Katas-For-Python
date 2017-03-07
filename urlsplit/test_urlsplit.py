import unittest
from parse_url import parse_url


class test_basic_example(unittest.TestCase):
    def assertProtocol(self, url, expect_protocol):
        url_object = parse_url(url)
        actual_protocol = url_object.protocol
        self.assertEqual(expect_protocol, actual_protocol)

    def test_finds_http_protocol(self):
        self.assertProtocol('http://www.site.com', 'http')

    def test_finds_ftp_protocol(self):
        self.assertProtocol('ftp://www.site.com', 'ftp')

    def test_finds_custom_protocol(self):
        self.assertProtocol('custom://www.site.com', 'custom')

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
        url_object = parse_url(url)
        actual_path = url_object.path
        self.assertEqual(expect_path, actual_path)

    def test_empty_path(self):
        self.assertPath('http://www.com/', "")

    def test_empty_path_with_no_slash_end(self):
        self.assertPath('http://www.com', "")

    def test_single_word_path(self):
        self.assertPath('http://www.com/word', "word")

    def test_long_path(self):
        self.assertPath('http://www.com/word-some/path.txt', "word-some/path.txt")
