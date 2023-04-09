from src.models.translate import get_translation
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from flask import request
import re

api = Namespace("translate", description="Translates text by providing the target language.")

text_model = api.model("Text_To_Translate",{
    'text':fields.String(required=True, description="Text to translate"),
    'tgt': fields.String(required=True, description="Target language")

})

result_model = api.model("Result_Translate",{
  'text_translated':fields.String(required=True, description="Text translated"),
})

@api.route("/", methods = ["POST"])
class Translate(Resource):
  '''
  Translate text
  '''

  @api.expect(text_model)
  @api.response(500,"Error to translate")
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  @jwt_required()
  def post(self):
    try:
        text = request.json['text']
        tgt = request.json['tgt']

        if text == "" or text == " ":
           api.abort(400, "Text is required")

        text = re.split("(?<=[.?!]) +", text)

        if text[len(text)-1] == '':
            text.pop()

        text_translated = ""

        for sentence in text:
            translate = get_translation(sentence, tgt)
            text_translated = text_translated + translate

        text_translated = text_translated.replace('..', '.')
        return {"text_translated": text_translated},200
      
    except:
            api.abort(500, "Error to translate")


