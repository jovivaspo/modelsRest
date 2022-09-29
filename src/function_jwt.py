from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify,abort

def expire_date(min):
    now = datetime.now()
    new_date = now + timedelta(minutes=min)
    return new_date

def write_token(data):
    token = encode(payload={"password":data['password'], "exp": expire_date(10)}, key=getenv("SECRET_KEY"), algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token):
    try:
        decoded_token =  decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])

    except exceptions.ExpiredSignatureError:
         response = jsonify({"message":"Token Expired"})
         response.status_code = 401
         abort(response)
    
    except exceptions.DecodeError:
        response = jsonify({"message":"Invalid token"})
        response.status_code = 401
        abort(response)
      

    
   
