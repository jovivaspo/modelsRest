from flask import Flask, jsonify
from routes.auth import routes_auth
from routes.analyse import route_analyse
from dotenv import load_dotenv
from os import getenv


app = Flask(__name__)

load_dotenv()

#Set up config dev or prod
if getenv("CONFIG") == "DEV":
    # Using a development configuration
    app.config.from_object('config.DevConfig')
else:
    # Using a production configuration
    app.config.from_object('config.ProdConfig')


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


   


