import os

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster


class UrlDao:
    def __init__(self, config_dict):
        self._keyspace = config_dict['keyspace']
        self._username = config_dict['username']
        self._password = config_dict['password']
        self._cloud_config = config_dict['cloud_config']

    def _get_session(self):
        auth_provider = PlainTextAuthProvider(
            username=self._username, password=self._password)
        cluster = Cluster(cloud=self._cloud_config, auth_provider=auth_provider)
        return cluster.connect(self._keyspace)

    def save_long_url(self, short_url_id, long_url):
        session = self._get_session()
        insert_statement = """
        INSERT INTO urls (short_url_id, long_url)
        VALUES (%s, %s)
        """
        session.execute(insert_statement, (short_url_id, long_url))

    def get_long_url(self, short_url_id):
        session = self._get_session()
        rows = select_statement = """
        SELECT long_url FROM urls where short_url_id =%s
        """
        rows = session.execute(select_statement, (short_url_id,))
        if not rows:
            return None
        return rows[0].long_url

    def create_table(self):
        session = self._get_session()
        return session.execute("""
                        CREATE TABLE urls (
                            short_url_id text PRIMARY KEY,
                            long_url text
                        )
                        """)

    def delete_table(self):
        session = self._get_session()
        return session.execute("DROP TABLE urls")

    def create_keyspace(self):
        auth_provider = PlainTextAuthProvider(
            username=self._username, password=self._password)
        cluster = Cluster(cloud=self._cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        return session.execute("""CREATE KEYSPACE urlshortner
                WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
                            """)


CassandraConfig = {
    'keyspace': os.environ.get('CASSANDRA_KEYSPACE', 'urlshortner'),
    'username': os.environ.get('CASSANDRA_USERNAME', 'cassandra'),
    'password': os.environ.get('CASSANDRA_PASSWORD', 'cassandra'),
    'cloud_config': {
        'secure_connect_bundle': 'config/secure-connect-urlshortner.zip'
    }
}
