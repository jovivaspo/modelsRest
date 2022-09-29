from flask import Blueprint, request, jsonify, abort
from models.analyse_sentiment import analyse
from function_jwt import validate_token

route_analyse = Blueprint("route_analyse", __name__)

@route_analyse.before_request
def verify_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        return validate_token(token)
    except KeyError:
        response = jsonify({"message":"Token required"})
        response.status_code = 400
        abort(response)



@route_analyse.route("/analyse", methods = ["POST"])
def analyse_sentiment():
    try:
        text = request.json['text']
        return analyse(text)

    except:
        response = jsonify({"menssage":"Field text is required"})
        response.status_code = 400
        abort(response)


