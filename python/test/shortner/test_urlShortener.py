from unittest import TestCase, mock
from python.src.shortner.url_shortener import UrlShortener

class TestUrlShortener(TestCase):

    def setUp(self):
        self.url_shortener = UrlShortener()

    @mock.patch('random.choice')
    def test_generate_shorten_url(self, choice_mock):
        choice_mock.return_value = 'A2TQa7'
        shorten_url = self.url_shortener.generate_shorten_url()
        self.assertEqual(len(shorten_url), 6, "generated shorten_url_must be of length 6")
        #self.assertEqual(shorten_url, 'A2TQa7', "failed to generate random string")

    def tearDown(self):
        self.url_shortener = None

