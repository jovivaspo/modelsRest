from keybert import KeyBERT
import re
from unicodedata import normalize

kw_model = KeyBERT(model="distiluse-base-multilingual-cased-v2")

def keywords(text):
    list_keywords = kw_model.extract_keywords(text)
    list_normalized = list()
   
    for key in list_keywords:
      
# -> NFD y eliminar diacríticos
      s = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", key[0]), 0, re.I)

# -> NFC
      s = normalize( 'NFC', s)
      list_normalized.append(s)

    return list_normalized