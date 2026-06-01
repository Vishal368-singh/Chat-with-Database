import os
import google.generativeai as genai
from dotenv import load_dotenv
from typer import prompt

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question: str):
    prompt = f"""
    You are a PostgreSQL expert.

    Database Schema:

    Table: weatherdata.district_wise_7dayfc_severity
    

    Columns:
    inserted_at
    days
    state
    state_code
    district
    temp_min
    temp_max
    humidity
    rain_precip
    wind_speed
    
    Rules:
    1. Return ONLY executable PostgreSQL SQL.
    2. Do NOT use markdown.
    3. Do NOT wrap with ```sql.
    4. Do NOT explain anything.
    5. Return only the query.

    Question:
    {question}

    Return only SQL.
"""     
    response = model.generate_content(prompt)

    return response.text.strip()