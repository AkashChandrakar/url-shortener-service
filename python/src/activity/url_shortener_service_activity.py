

class UrlShortenServiceActivity:
    """
    The UrlShortenServiceActivity class serves as an orchestrator
    to route get and create requests from client.
    """

    def __init__(self, url_shortener):
        self.url_shortener = url_shortener

    def get_url(self, shorten_url):
        self.url_shortener.get_url(shorten_url)

    def save_url(self, actual_url):
        self.url_shortener.save_url(actual_url)

