from pydantic import BaseModel
import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)
   
def execute_query(sql):

    cur = conn.cursor()

    try:
        print("\nExecuting SQL:")
        print(sql)

        cur.execute(sql)

        columns = [desc[0] for desc in cur.description]

        rows = cur.fetchall()

        result = [
            dict(zip(columns, row))
            for row in rows
        ]

        return result

    except Exception as e:

        conn.rollback()

        print("\nDATABASE ERROR:")
        print(type(e).__name__)
        print(str(e))

        raise

    finally:
        cur.close()