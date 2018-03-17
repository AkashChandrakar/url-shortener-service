from random import choice
from string import digits, ascii_lowercase, ascii_uppercase

from python.src.constants.constant import Constant
from python.src.model.shorten_actual_url_pair_key import ShortenActualUrlPairKey


class UrlShortener:
    """
    The UrlShortener class act as a bridge between the UrlShortenServiceActivity
    and the ShortenActualUrlPairDao class.
    """
    def __init__(self, shorten_actual_url_pair_dao):
        self.shorten_actual_url_pair_dao = shorten_actual_url_pair_dao

    def get_url(self, shorten_url):
        """

        :param shorten_url:
        :return:
        """
        shorten_actual_url_pair_key = ShortenActualUrlPairKey()
        shorten_actual_url_pair = shorten_actual_url_pair_dao.get_shorten_actual_url_pair()

    def save_url(self, actual_url):


    def generate_shorten_url(self):
        """
        Return the shorten url of fixed length
        :return: the shorten url
        """
        return self._generate_random_string(Constant.STRING_LENGTH_SIX)

    def _generate_random_string(self, length):
        """
        Generates a random string of 'length' long using characters,
        A-Z, a-z and 0-9.

        :rtype: string
        :param length: the length of the random string that needs to be generated.
        :return: the length long random string
        """
        random_string_chars = digits + ascii_uppercase + ascii_lowercase
        random_string = "".join([choice(random_string_chars) for i in range(length)])
        return random_string
