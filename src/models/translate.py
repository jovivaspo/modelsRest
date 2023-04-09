from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForSeq2SeqLM.from_pretrained(model)

def get_translation(text,tgt):
    encoded = tokenizer(text, return_tensors='pt')
    output = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id[tgt],max_length=200)
    decoded = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    return decoded
