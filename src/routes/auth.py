from flask import Blueprint, jsonify, request
from src.function_jwt import write_token, validate_token
from os import getenv

routes_auth = Blueprint("routes_auth", __name__)

@routes_auth.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        if data['username'] == getenv("USERNAME_APP") and data['password'] == getenv("PASSWORD_APP"):
            return write_token(data)
        response = jsonify({"message":"Username or password not correct: ",
        "data":data,
        "username": getenv("USERNAME_APP"),
        "password":getenv("PASSWORD_APP")
        })
        response.status_code = 403
        return response
    except:
        response = jsonify({"message":"Username and password are required"})
        response.status_code = 403
        return response

   

    




