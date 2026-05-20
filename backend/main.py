from fastapi import FastAPI
from pydantic import BaseModel

from llm.generator import ask_healthcare_rag

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")

def ask_question(request: QueryRequest):

    result = ask_healthcare_rag(request.question)

    return result