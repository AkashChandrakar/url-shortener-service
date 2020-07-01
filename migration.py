from cassandra_client import CassandraConfig
from cassandra_client import UrlDao

if __name__ == "__main__":
    url_dao = UrlDao(CassandraConfig)
    url_dao.create_keyspace()
    print(url_dao.create_table())
