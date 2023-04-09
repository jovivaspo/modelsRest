from src.models.keywords import keywords
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from flask import request
import re

api = Namespace("keywords", description="Extracts keywords from a given text.")

text_model = api.model("Text_With_Keywords",{
    'text':fields.String(required=True, description="Text to extracts keywords"),

})

result_model = api.model("Result_Keywords",{
  'keywords':fields.List(fields.String),
})

@api.route("/", methods = ["POST"])
class Translate(Resource):
  '''
  Extract keywords
  '''

  @api.expect(text_model)
  @api.response(500,"Error to extract keywords")
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  @jwt_required()
  def post(self):
    try:
        text = request.json['text']

        if text == "" or text == " ":
           api.abort(400, "Text is required")

        list_keywords = keywords(text)
        return {"keywords": list_keywords},200
       
      
    except:
            api.abort(500, "Error to extract keywords")


