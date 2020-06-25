import json
import os
import random
import string

from flask import Flask
from flask import render_template
from flask import request

from cassandra_client import UrlDao

app = Flask(__name__)
APP_URL = 'https://common-shrew.herokuapp.com/'

cassandra_hosts = json.loads(os.environ.get('CASSANDRA_HOSTS', '["127.0.0.1"]'))
cassandra_port = int(os.environ.get('CASSANDRA_PORT', '9042'))
cassandra_keyspace = os.environ.get('CASSANDRA_KEYSPACE', 'urlshortner')
cassandra_username = os.environ.get('CASSANDRA_USERNAME', 'cassandra')
cassandra_password = os.environ.get('CASSANDRA_PASSWORD', 'cassandra')

url_dao = UrlDao(cassandra_hosts, cassandra_port, cassandra_keyspace,
                 cassandra_username, cassandra_password)


def gen_random_string(length=9):
    return ''.join(random.SystemRandom()
                   .choice(string.ascii_uppercase + string.digits
                           + string.ascii_lowercase) for _ in range(length))


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/shorten', methods=['GET'])
def shorten_url():
    short_url = gen_random_string()
    url_dao.save_long_url(long_url=request.args.get('longUrl'), short_url=short_url)
    return APP_URL + short_url
