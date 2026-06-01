from fastapi import FastAPI
from db import  execute_query
from schemas import   QueryRequest
from llm import generate_sql

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI SQL Generator Running"}

@app.post("/generate-sql")
def generate(request: QueryRequest):

    sql = generate_sql(request.question)
    print("Generated SQL:", sql)
    response = execute_query(sql)
    return {
        "question": request.question,
        "generated_sql": sql,
        "response": response
    }