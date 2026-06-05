from utils.llm import model
from utils.prompt_builder import build_sql_prompt

def generate_sql(question, schema):

    prompt = build_sql_prompt(
        question=question,
        schema=schema
    )

    response = model.generate_content(prompt)
    
    print(f"Generated SQL: {response.text.strip()}")
    return response.text.strip()