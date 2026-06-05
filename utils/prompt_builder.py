def build_sql_prompt(question, schema):
    schema_text = ""

    for table, columns in schema.items():
        schema_text += f"\nTable: {table}\n"
        schema_text += "\n".join(columns)
        schema_text += "\n"

    return f"""
        You are an expert PostgreSQL SQL generator.

        Database Schema:

        {schema_text}

        Rules:

     Rules:

        1. Generate ONLY valid PostgreSQL SELECT queries.
        2. Return ONLY SQL. No markdown, comments, explanations, or surrounding text.
        3. Use ONLY the tables and columns explicitly listed in the schema provided.
        4. Every table reference MUST use the exact schema-qualified name:
        weatherdata.<table_name>
        5. Never use the public schema.
        6. Never invent, infer, rename, or assume table names.
        7. Never invent, infer, rename, or assume column names.
        8. Before generating SQL, verify that every table and column used exists in the provided schema.
        9. If the requested information cannot be answered using the provided schema, return exactly:
        SELECT 'INSUFFICIENT_SCHEMA_INFORMATION' AS error;
        10. If multiple tables are required, use only joins that can be inferred from the provided schema.
        11. Do not use tables or columns that are not explicitly listed.
        12. Prefer the simplest valid query that answers the question.
        13. Use PostgreSQL syntax only.
        14. Preserve exact table names and column names as provided in the schema.
        15. Do not guess. When uncertain, return:
        SELECT 'INSUFFICIENT_SCHEMA_INFORMATION' AS error;
 
        Question:
        {question}

        Return only SQL.
        """