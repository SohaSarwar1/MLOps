from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

@app.get("/translate")
def translate(text: str):
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
    translation = translator(text, max_length=40)[0]["translation_text"]
    return {"translation": translation}
