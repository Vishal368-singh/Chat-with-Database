def validate_sql(sql):

    forbidden = [
        "DROP",
        "DELETE",
        "TRUNCATE",
        "ALTER",
        "UPDATE",
        "INSERT"
    ]

    upper_sql = sql.upper()

    for keyword in forbidden:
        if keyword in upper_sql:
            raise ValueError(
                f"Forbidden SQL detected: {keyword}"
            )

    return True