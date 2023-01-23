from src.models.analyse_sentiment import analyse
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from flask import request

api = Namespace("analyse", description="Sentiment analysis")

text_model = api.model("Text",{
    'text':fields.String(required=True, description="Text to analyse"),

})

result_model = api.model("Result",{
  'label':fields.String(required=True, description="Positive or negative"),
  'score':fields.String(required=True, description="Scoring of the analysis 0-1")
})

@api.route("/", methods = ["POST"])
class Analyse(Resource):
  '''
  Login in the Api and receive token
  '''

  @api.expect(text_model)
  @api.response(500,"Error to analyse")
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  @jwt_required()
  def post(self):
    try:
        print("Hola")
        text = request.json['text']

        if text == "" or text == " ":
           api.abort(400, "Text is required")

        result = analyse(text)

        return result, 200
      
    except KeyError:
            api.abort(500, "Error to analyse")


