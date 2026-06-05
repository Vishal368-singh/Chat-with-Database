
def get_schema(conn, schema_name="weatherdata"):
    
    sql = """
    SELECT
        table_name,
        column_name
    FROM information_schema.columns
    WHERE table_schema = %s
    ORDER BY table_name, ordinal_position
    """

    cur = conn.cursor()
    cur.execute(sql, (schema_name,))

    schema = {}

    for table, column in cur.fetchall():
        schema.setdefault(table, []).append(column)

    cur.close()

    return schema