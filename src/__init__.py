from flask import Flask, jsonify
from src.routes.auth import routes_auth
from src.routes.analyse import route_analyse
from dotenv import load_dotenv
from os import getenv
from src.config import config

def create_app():

    app = Flask(__name__)

    load_dotenv()

    config_name = getenv("CONFIG")

    app.config.from_object(config.get(config_name or 'default'))

    #Routes:
    app.register_blueprint(routes_auth, url_prefix='/api')
    app.register_blueprint(route_analyse, url_prefix='/api')

    @app.route("/")
    def index():
        return jsonify({"message":"WELCOME TO SENTIMENT ANALYSIS!"})

    #Error handler
    @app.errorhandler(404)
    def error(e):
        return jsonify({"message":"Not Found!"}), 404

    return app


   


