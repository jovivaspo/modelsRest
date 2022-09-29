from flask import abort, jsonify
from transformers import pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment-latest"

def analyse(text):
      try:
            if(text == ""):
                   response = jsonify({"menssage":"Field text is empty"})
                   response.status_code = 400
                   abort(response)
                  
            new_text = []

            for t in text.split(" "):
                  t = '@user' if t.startswith('@') and len(t) > 1 else t
                  t = 'http' if t.startswith('http') else t
                  new_text.append(t)

            text = " ".join(new_text)
            model_path = 'cardiffnlp/twitter-roberta-base-sentiment-latest'
            sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
            sentiment = sentiment_task(text)
            return sentiment

      except Exception as e:
            response = jsonify({"menssage":"Error to analysing"})
            response.status_code = 500
            abort(response)



