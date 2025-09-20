from fastapi import FastAPI

app = FastAPI()
# create decorator function
@app.get("/hello")
async def hello():
    return "Hello Deepseeds!"

"""uvicorn app:app --reload" "where 'app' b4 : is filename, 'app' after : is class name, --reload reloads browser automatically"""

@app.get("/sentiment-analysis")
def analyze_sentiment():
    # after logic here
    # then return the data
    return {
        "sentiment_score":"score-0.7",
        "platform":"huggingface",
        "sentiment":"Positive",
        "model":"distilbert-id"
    }

# create a point: that returns information about you(name, email, favmeal, age)
# TOPIC2: PATH PARAMETERS

@app.get("/sentiment/{text}")
def analyze_sentiment(text):
    if text.lower() in ["good", "nice", "great"]:
        return {
            "sentiment":"positive",
            "score":"positive score",
            "model":"model"
        }
    else:
        return {
            "sentiment":"negative",
            "score":"negative score",
            "model":"model"
        }