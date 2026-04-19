from fastapi import FastAPI
from agents.tutor import tutor_agent
from agents.quiz import quiz_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "working"}   # ⚠️ keep unchanged

@app.get("/tutor")
def tutor(topic: str):
    return {"response": tutor_agent(topic)}

@app.get("/quiz")
def quiz(topic: str):
    return {"questions": quiz_agent(topic)}
