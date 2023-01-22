from flask import  jsonify, request
from src.function_jwt import write_token, validate_token
from os import getenv
from flask_restx import Namespace, Resource, fields

api = Namespace("Auth", description="Login", path="/login")

user_model = api.model("User",{
    'username':fields.String(required=True, description="Name of the user"),
    'password':fields.String(required=True, description="Password of the user")
})

token_model = api.model("Token",{
    'token':fields.String(description='Access Token')
})

@api.route("/login", methods=["POST"])
class Register(Resource):
  '''Login in the Api and receive token'''
  @api.expect(user_model)
  @api.response(401,"Wrong credentials")
  @api.marshal_with(token_model)
  def login():
    try:
        data = request.get_json()
        if data['username'] == getenv("USERNAME_APP") and data['password'] == getenv("PASSWORD_APP"):
            return write_token(data)
        response = jsonify({"message":"Username or password not correct"})
        response.status_code = 401
        return response
    except:
        response = jsonify({"message":"Username and password are required"})
        response.status_code = 401
        return response

   

    




