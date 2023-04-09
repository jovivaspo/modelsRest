from src.models.summarize import summarize
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from flask import request


api = Namespace("summarize", description="Summarizes a given text.")

text_model = api.model("Text_To_Summarize",{
    'text':fields.String(required=True, description="Text to summarize"),
})

result_model = api.model("Result_Summarize",{
  'text_summarised':fields.String(required=True, description="Text summarised"),
})

@api.route("/", methods = ["POST"])
class Translate(Resource):
  '''
  Summarize Text
  '''

  @api.expect(text_model)
  @api.response(500,"Error to summarize")
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  @jwt_required()
  def post(self):
    try:
        text = request.json['text']
       

        if text == "" or text == " ":
           api.abort(400, "Text is required")

        sum = summarize(text)

       
        return {"text_summarised": sum},200
      
    except:
            api.abort(500, "Error to summarize")


