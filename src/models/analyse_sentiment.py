from flask import abort, jsonify
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax


MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def analyse(text):
      try:   
            new_text = []

            for t in text.split(" "):
                  t = '@user' if t.startswith('@') and len(t) > 1 else t
                  t = 'http' if t.startswith('http') else t
                  new_text.append(t)

            text = " ".join(new_text)

            encoded_input = tokenizer(text, return_tensors='pt')
            output = model(**encoded_input)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            ranking = np.argsort(scores)
            ranking = ranking[::-1]
            label = config.id2label[ranking[0]]
            score = scores[ranking[0]]
            result = {"label":label,
            "score": str(round(score,2))
            }
            
            return result

      except Exception as e:
            error = {"menssage":"Error to analysing"}
            return error
           
            



