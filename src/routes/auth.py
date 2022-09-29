from flask import Blueprint, jsonify, request
from function_jwt import write_token, validate_token
from os import getenv

routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data['username'] == getenv("USERNAME_APP") and data['password'] == getenv("PASSWORD_APP"):
        return write_token(data)

    response = jsonify({"message":"Username or password not correct"})
    response.status_code = 403
    return response


