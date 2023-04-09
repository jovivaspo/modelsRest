from flask import Flask, jsonify
from dotenv import load_dotenv
from os import getenv
from src.config import config
from flask_jwt_extended import JWTManager
from src.api import blueprint

def create_app():

    app = Flask(__name__)

    load_dotenv()

    config_name = getenv("CONFIG")

    app.config.from_object(config.get(config_name or 'default'))

    app.register_blueprint(blueprint)

    
    jwt = JWTManager()
    jwt.init_app(app)

    #Routes:
    @app.route("/")
    def index():
        return jsonify({"message":"Welcome to ModelsRest!"})

    #Error handler
    @app.errorhandler(404)
    def error(e):
        return jsonify({"message":"Not Found!"}), 404

    return app


   


