from flask import Flask, jsonify
from src.api_auth import route_auth
from src.api_analyse import route_analyse
from dotenv import load_dotenv
from os import getenv
from src.config import config
from src.api_auth import api

def create_app():

    app = Flask(__name__)

    load_dotenv()

    config_name = getenv("CONFIG")

    app.config.from_object(config.get(config_name or 'default'))

    #Routes:
    app.register_blueprint(route_auth)
    app.register_blueprint(route_analyse)

    @app.route("/")
    def index():
        return jsonify({"message":"WELCOME TO SENTIMENT ANALYSIS!"})

    #Error handler
    @app.errorhandler(404)
    def error(e):
        return jsonify({"message":"Not Found!"}), 404

    return app


   


