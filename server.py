import random
import string

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from cassandra_client import CassandraConfig
from cassandra_client import UrlDao

app = Flask(__name__)
APP_URL = 'https://common-shrew.herokuapp.com/'

url_dao = UrlDao(CassandraConfig)


def gen_random_string(length=9):
    return ''.join(random.SystemRandom()
                   .choice(string.ascii_uppercase + string.digits
                           + string.ascii_lowercase) for _ in range(length))


@app.route('/', methods=['GET'])
def home():
    print('Get homepage')
    return render_template('home.html')


@app.route('/shorten', methods=['GET'])
def shorten_url():
    long_url = request.args.get('longUrl')
    print('Shorten long url: {}'.format(long_url))
    short_url_id = gen_random_string()
    url_dao.save_long_url(long_url=long_url, short_url_id=short_url_id)
    return APP_URL + short_url_id


@app.route('/<short_url_id>', methods=['GET'])
def get_long_url(short_url_id):
    print('Fetch long url for short_url_id: {}'.format(short_url_id))
    long_url = url_dao.get_long_url(short_url_id)
    if long_url is None:
        return render_template('404.html')
    return redirect(long_url, 301)
