# URL shortener service https://common-shrew.herokuapp.com

## Build instructions

First, make sure to have virtualenv installed. If it isn't installed already, this should do the trick:
```
pip install virtualenv
or
sudo easy_install -U virtualenv
```

create a new virtual environment, and activate it:
```
virtualenv venv
source venv/bin/activate
```

Install required dependencies
```
pip install -r requirements.txt
```

Create the schema
```
python manage.py migrate
```

Run the server
```
FLASK_APP=server.py flask run
```
