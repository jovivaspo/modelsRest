from flask import  request, jsonify, abort
from src.models.analyse_sentiment import analyse
from src.function_jwt import validate_token
from flask_restx import Namespace, Resource, fields


api = Namespace("Analysis", description="Sentiment analysis", path="/analyse")

text_model = api.model("Text",{
    'text':fields.String(required=True, description="Text to analyse"),

})

result_model = api.model("Result",{
  'label':fields.String(required=True, description="Positive or negative"),
  'score':fields.String(required=True, description="Scoring of the analysis 0-1")
})

@api.before_request
def verify_token():
    try:
        token = request.headers['Authorization'].split(" ")[1]
        return validate_token(token)
    except KeyError:
        response = jsonify({"message":"Token required"})
        response.status_code = 400
        abort(response)



@api.route("/analyse", methods = ["POST"])
class Register(Resource):
  '''Login in the Api and receive token'''
  @api.expect(text_model)
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  def analyse_sentiment():
    try:
        text = request.json['text']
        return analyse(text)

    except KeyError:
            response = jsonify({"menssage":"Field text is required"})
            response.status_code = 400
            abort(response)


