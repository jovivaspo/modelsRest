from src.models.paraphrase import paraphrase_control
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from flask import request


api = Namespace("paraphrase", description="Paraphrase a given text.")

text_model = api.model("Text_To_Paraphrase",{
    'text':fields.String(required=True, description="Text to paraphrase"),
})

result_model = api.model("Result_Paraphrase",{
  'text_paraphrased':fields.String(required=True, description="Text paraphrased"),
})

@api.route("/", methods = ["POST"])
class Translate(Resource):
  '''
  Paraphrase Text
  '''

  @api.expect(text_model)
  @api.response(500,"Error to paraphrase")
  @api.response(400,"Text is required")
  @api.marshal_with(result_model)
  @jwt_required()
  def post(self):
    try:
        text = request.json['text']
       

        if text == "" or text == " ":
           api.abort(400, "Text is required")

        phrase = paraphrase_control(text)

        return {"text_paraphrased": phrase['phrase']},200
      
    except:
            api.abort(500, "Error to paraphrase")


