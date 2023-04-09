from transformers import PegasusForConditionalGeneration, AutoTokenizer 

check_point = "google/pegasus-xsum"
tokenizer = AutoTokenizer.from_pretrained(check_point)
model = PegasusForConditionalGeneration.from_pretrained(check_point)

def summarize(text):
    max_length = 60
    tokens = tokenizer.encode(text, max_length=512, truncation=True, padding=False, return_tensors="pt")
    ids = model.generate(tokens, min_length=20, max_length=max_length)
    summary = tokenizer.decode(ids[0], skip_special_tokens=True)

    while len(summary) >= 250 and max_length > 20:
       print(len(summary), max_length)
       max_length-= 10
       tokens = tokenizer.encode(summary, max_length=512, truncation=True, padding=False, return_tensors="pt")
       ids = model.generate(tokens, min_length=20, max_length=max_length)
       summary = tokenizer.decode(ids[0], skip_special_tokens=True)

    return summary
