from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster


class UrlDao:
    def __init__(self, hosts, port, keyspace, username, password):
        self._keyspace = keyspace
        self._hosts = hosts
        self._port = port
        self._username = username
        self._password = password

    def _get_session(self):
        auth_provider = PlainTextAuthProvider(
            username=self._username, password=self._password)
        cluster = Cluster(self._hosts, port=self._port, auth_provider=auth_provider)
        return cluster.connect(self._keyspace)

    def save_long_url(self, short_url, long_url):
        session = self._get_session()
        insert_statement = """
        INSERT INTO urls (short_url, long_url)
        VALUES (%s, %s)
        """
        session.execute(insert_statement, (short_url, long_url))

    def get_long_url(self, short_url):
        session = self._get_session()
        rows = select_statement = """
        SELECT long_url FROM urls where short_url = %s
        """
        rows = session.execute(select_statement, short_url)
        print(rows)
