
class ShortenActualUrlPairKey:
    """
    The ShortenActualUrlPairKey class used to get the ShortenActualUrlPair.
    """

    def __init__(self, key):
        self._shorten_url = key

    def get_shorten_url(self):
        """
        The getter method to return shorten_url.
        :return: the shorten_url
        """
        return self._shorten_url

