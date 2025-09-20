from fastapi import FastAPI
from transformers import pipeline
app = FastAPI()
sentiment_pipeline = pipeline("zero-shot-object-detection")

@app.get("/sentiment")
def sentiment_analysis(text:str):
    result = sentiment_pipeline(text)
    return {
        "text":text,
        "sentiment":result
    }