from functools import wraps
from flask import Flask, flash, g, current_app
import soundcloud
from arango_orm import Database
from arango import ArangoClient


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

def get_client_sc():
    client_sc=getattr(g, 'client_sc', None)
    if(client_sc is None):
       g.client_sc = soundcloud.Client(client_id=app.config["APY_KEY"])#SoundcloudAccess(api_key=app.config["APY_KEY"]).get_client_sc()
    return g.client_sc 

def initDB():
    db=getattr(g, 'db', None)
    if(db is None):
        client = ArangoClient(protocol='http', host='localhost', port=8529)
        test_db = client.db('soundcloud', username='root', password='')
        g.db = Database(test_db)
    return g.db

def load_client_sc(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        get_client_sc()
        print("Init sc called!!!!!!!!!!" + str(len(args)))
        return func(*args, **kwargs)

    return decorated_function

def load_db(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        initDB()
        print("Init db called!!!!!!!!!!")
        return func(*args, **kwargs)

    return decorated_function

