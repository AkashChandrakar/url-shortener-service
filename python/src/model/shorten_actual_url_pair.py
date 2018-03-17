

class ShortenActualUrlPair:
    """
    The ShortenActualUrlPair class that has the shorten url and the original url.
    """

    def __init__(self, original_url, shorten_url):
        """
        The parametrised constructor for ShortenActualUrlPair.
        :param original_url: the original_url
        :param shorten_url: the shorten_url
        """
        self._original_url = original_url
        self._shorten_url = shorten_url

    def get_shorten_url(self):
        """
        The getter method to return shorten url.
        :return: the shorten url
        """
        return self._shorten_url

    def get_actual_url(self):
        """
        The getter method to return original url.
        :return: the original url
        """
        return self._original_url

