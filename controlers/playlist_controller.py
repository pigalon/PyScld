from flask import Blueprint, Flask, render_template, json, jsonify, make_response
from decorator import load_client_sc, load_db, current_app

from services.FavoritesManager import FavoritesManager
from services.PlaylistsManager import PlaylistsManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('../config.py')

playlist_page = Blueprint('playlist_page', __name__,
                        template_folder='../templates')

@playlist_page.route('/playlist/test')
def test(name=None):
    return render_template('test.html')

@playlist_page.route('/api/playlists/db/me/count')
@load_client_sc
@load_db
def get_my_playlists_count_from_db():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    count = PlaylistsManager().getPlaylistsCountFromDB(user_id=me_id)
    return make_response(jsonify({'count':count}))

@playlist_page.route('/api/playlists/sc/me/count')
@load_client_sc
@load_db
def get_my_playlists():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    count = PlaylistsManager().getPlaylistsCountFromSCUser(user_id=me_id)
    return make_response(jsonify({'count': count}))


@playlist_page.route('/api/playlists/db/me')
@load_db
def get_my_playlists_from_db():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    list = PlaylistsManager().getJsonPlayslistFromDB(user_id=me_id)
    return make_response(jsonify(list))

@playlist_page.route('/api/playlists/init/me')
@load_client_sc
@load_db
def write_my_playlists():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    list = PlaylistsManager().getJsonPlayslistFromDB(user_id=me_id)
    return PlaylistsManager().savePlaylists(playlistsComplete=list)

