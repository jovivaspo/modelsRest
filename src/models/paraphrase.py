from sentence_transformers import SentenceTransformer, util
import torch
from transformers import PegasusForConditionalGeneration, AutoTokenizer
import pylev


model_simil = SentenceTransformer('bert-base-nli-mean-tokens')
model_paraphrase = 'tuner007/pegasus_paraphrase'


torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = AutoTokenizer.from_pretrained(model_paraphrase)
model = PegasusForConditionalGeneration.from_pretrained(model_paraphrase).to(torch_device)

###Parafraseador
def get_response(input_text,num_return_sequences,num_beams):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=250, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=250,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text


###Devuelve la distacia a nivel de palabra entre el texto original y el parafraseo
def get_distance(src_txt, paraphrased_txt):
    """Returns levenschtein distance at word level between src_text and paraphrase"""
    return pylev.levenschtein(src_txt.split(), paraphrased_txt.split())

#Devuelve el coseno de similitud
def get_similarity(src_txt, paraphrased_txt):
    """Returns cosine similarity between source and paraphrase sentence vectors"""
    src_txt_encoded = model_simil.encode(src_txt, convert_to_tensor=True)
    paraphrased_txt_encoded = model_simil.encode(paraphrased_txt, convert_to_tensor=True)
    return util.pytorch_cos_sim(src_txt_encoded , paraphrased_txt_encoded).item()

def paraphrase_control(text):

    num_beams = 10
    num_return_sequences = 10
    
    outputs=get_response(text,num_return_sequences,num_beams)
    results = list()

    for output in outputs:
        distance = get_distance(text,output)
        simil = get_similarity(text,output)
        results.append({
            "distance":distance,
            "simil": simil,
            "phrase": output
        })
    
    ###Tomamos la oración con mayor distancia y con simil mayor o igual que 0.8

    results = sorted(results, key=lambda x: x['distance'], reverse=True)
    result_end = results[0]

    if(result_end["simil"]<0.85):
        for i in range(1,10):
             ###print(results[i])
            if results[i]["simil"]>=0.85:
                result_end = results[i]
                break

    return result_end

