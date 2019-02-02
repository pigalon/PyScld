from flask import Blueprint, Flask, render_template, session, g, current_app, redirect, url_for, escape,request, json, jsonify
from flask_cors import CORS
from decorator import load_client_sc, load_db
from soundcld.SoundcloudAccess import SoundcloudAccess

#from .arangodb.DatabaseAdb import DatabaseAdb
from controlers.playlist_controller import playlist_page
from controlers.user_controller import user_page
from services.FavoritesManager import FavoritesManager
from services.PlaylistsManager import PlaylistsManager
# 21381146

app = Flask(__name__,instance_relative_config=True, template_folder='web/templates', static_folder='web/static')
app.register_blueprint(playlist_page)
app.register_blueprint(user_page)
app.config.from_object('config')
app.config.from_pyfile('config.py')




cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#client_sc = SoundcloudAccess.instance().get_client_sc()
#ardb = DatabaseAdb(app.config["DB_NAME"]).getDb()

@app.route('/')
@load_client_sc
@load_db
def index():
    #client_sc=get_client_sc()
    #db = initDB()
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    delta = FavoritesManager().getFavoritesCountDelta(me_id)
    print(str(delta))
    return render_template('index.html')

@app.route('/testdt')
def testdt():
    return render_template('test.html')

@app.route('/tables')
def porfolio(name=None):
    return render_template('tables.html')

@app.route('/about/')
def about(name=None):
    return render_template('about.html')

@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html')

@app.route('/test/')
def test():
    my_dict = {"title": "Bayside", "genre": "Alternative"}
    return json.dumps(my_dict)

@app.route('/api/test')
def random_number():
    response = {
        'band': "test---"
    }
    return jsonify(response)



if __name__ == "__main__":
    #db = DatabaseAdb()
    print("server is running on localhost!! " + app.config["MY_EMAIL"] + " - " + app.config["APY_KEY"])
    app.run(debug=True)
    ctx = app.app_context()
    ctx.push()
    #g.client_sc = soundcloud.Client(client_id=app.config["APY_KEY"])
    #g.db = initDB()

    