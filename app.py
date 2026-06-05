from fastapi import FastAPI, logger
from db import  check_connection, execute_query
from schemas import   QueryRequest
from services.text_to_sql_service import text_to_sql
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI SQL Generator Running"}

@app.post("/generate-sql")
def generate(request: QueryRequest):

    sql = text_to_sql(request.question, check_connection())
    response = execute_query(sql)
    return {
        "question": request.question,
        "generated_sql": sql,
        "response": response
    }
    
if __name__ == "__main__":
    print("Starting on port 9000...")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=6000,
        reload=True
    )