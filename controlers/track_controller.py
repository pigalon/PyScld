from flask import Blueprint, Flask, render_template, json, jsonify, make_response
from decorator import load_client_sc, load_db, current_app

from services.TracksManager import TracksManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('../config.py')

track_page = Blueprint('track_page', __name__,
                        template_folder='../templates')