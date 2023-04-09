from flask import  jsonify, request
from os import getenv
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token

api = Namespace("login", description="Login in the Api and receive token")

user_model = api.model("User",{
    'username':fields.String(required=True, description="Name of the user"),
    'password':fields.String(required=True, description="Password of the user")
})

token_model = api.model("Token",{
    'access_token':fields.String(description='Access Token')
})

@api.route("/", methods=["POST"])
class Login(Resource):
  '''
  Login in the Api and receive token
  '''

  @api.expect(user_model)
  @api.response(401,"Wrong credentials")
  @api.response(400,"Bad Request")
  @api.marshal_with(token_model)
  def post(self):
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    if username is "" or password is "":
        api.abort(400, "Bad request")

    if  username == getenv("USERNAME_APP") and  password == getenv("PASSWORD_APP"):
        access_token = create_access_token(identity=data['username'])
        return {"access_token": access_token}, 200
    
    api.abort(401,"Wrong credentials")
   

    




