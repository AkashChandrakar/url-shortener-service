import json
import os

from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

cassandra_hosts = json.loads(os.environ.get('CASSANDRA_HOSTS', '["127.0.0.1"]'))
cassandra_port = int(os.environ.get('CASSANDRA_PORT', '9042'))
cassandra_keyspace = os.environ.get('CASSANDRA_KEYSPACE', 'urlshortner')
cassandra_username = os.environ.get('CASSANDRA_USERNAME', 'cassandra')
cassandra_password = os.environ.get('CASSANDRA_PASSWORD', 'cassandra')


def create_keyspace():
    auth_provider = PlainTextAuthProvider(
        username=cassandra_username, password=cassandra_password)
    cluster = Cluster(cassandra_hosts, cassandra_port, auth_provider=auth_provider)
    session = cluster.connect()
    session.execute("""
                         CREATE KEYSPACE urlshortner
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
                        """)


def create_table():
    auth_provider = PlainTextAuthProvider(
        username=cassandra_username, password=cassandra_password)
    cluster = Cluster(cassandra_hosts, cassandra_port, auth_provider=auth_provider)
    session = cluster.connect(cassandra_keyspace)
    session.execute("""
                    CREATE TABLE urls (
                        short_url text PRIMARY KEY,
                        long_url text
                    )
                    """)


if __name__ == "__main__":
    create_keyspace()
    create_table()
