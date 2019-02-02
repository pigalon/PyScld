from flask import Blueprint, Flask, render_template, json, jsonify, make_response
from decorator import load_client_sc, load_db, current_app

from services.UsersManager import UsersManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('../config.py')

user_page = Blueprint('user_page', __name__,
                        template_folder='../templates')

@user_page.route('/api/followings/db/me/count')
@load_db
def get_my_followings_count_from_db():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    count = UsersManager().getFollowingsCountFromDB(user_id=me_id)
    return make_response(jsonify({'count':count}))

@user_page.route('/api/followings/db/me')
@load_db
def get_my_followings_from_db():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    list = UsersManager().getJsonFollowingsFromDB(user_id=me_id)
    return make_response(jsonify(list))

@user_page.route('/api/followings/sc/me')
@load_client_sc
def get_my_followings_from_sc():
    me_id = app.config["SC_MY_ID"]
    print(str(me_id))
    list = UsersManager().getJsonFollowingsFromSC(user_id=me_id)
    return make_response(jsonify(list))