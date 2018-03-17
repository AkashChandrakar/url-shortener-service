from abc import ABC, abstractmethod


class ShortenActualUrlPairDao(ABC):
    """
    An ShortenActualUrlPairDao datastore class provide an abstraction on top of storage mechanisms for storing
    ShortenActualUrlPairs. It abstracts the clients to know anything about how ShortenActualUrlPair are stored.
    """

    def __init__(self):
        pass

    @abstractmethod
    def get_shorten_actual_url_pair(self, shorten_actual_url_pair_key):
        """
        The get method is used to get an ShortenActualUrlPair using ShortenActualUrlPairKey if it exists.

        :param shorten_actual_url_pair_key: the shorten_actual_url_pair_key used to get an shorten_actual_url_pair
        :return: the shorten_actual_url_pair if it exists otherwise None
        """
        pass

    @abstractmethod
    def create_shorten_actual_pair(self, shorten_actual_pair):
        """
        The create method is used to store the ShortenActualUrlPairKey if it does not exists.

        :param shorten_actual_pair:
        :return:
        :raises StorageSaveException if the method fails to store an ShortenActualUrlPairKey
                and DuplicateKeyException if the key already exist.
        """
        pass

