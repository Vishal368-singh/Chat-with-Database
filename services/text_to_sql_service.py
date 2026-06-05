from utils.schema_loader import get_schema
from utils.sql_generator import generate_sql
from utils.sql_validator import validate_sql

def text_to_sql(question, conn):

    schema = get_schema(conn)

    sql = generate_sql(
        question=question,
        schema=schema
    )

    print(f"Generated SQL: {sql}")
    validate_sql(sql)

    return sql