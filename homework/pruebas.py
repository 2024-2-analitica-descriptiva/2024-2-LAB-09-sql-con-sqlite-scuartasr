import sqlite3

import pandas as pd  # type: ignore


def load_data():
    """Load data."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("tests/create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur

def test_08():
    """Test 08."""
    conn, _ = load_data()
    with open("homework/pregunta_08.sql", encoding="utf-8") as file:
        query = file.read()
    print(pd.read_sql_query(query, conn).to_dict())
    # assert pd.read_sql_query(query, conn).to_dict() == {
    #     "strftime('%Y', c23)": {0: "2016", 1: "2017", 2: "2018", 3: "2019"},
    #     "avg(c21)": {
    #         0: 564.4764285714285,
    #         1: 515.1563636363636,
    #         2: 557.5593749999999,
    #         3: 550.9985714285714,
    #     },
    # }

def test_11():
    """Test 11."""
    conn, _ = load_data()
    with open("homework/pregunta_11.sql", encoding="utf-8") as file:
        query = file.read()
    print(pd.read_sql_query(query, conn).to_dict())

def test_10():
    """Test 10."""
    conn, _ = load_data()
    with open("homework/pregunta_10.sql", encoding="utf-8") as file:
        query = file.read()
    print(pd.read_sql_query(query, conn).to_dict())

def test_12():
    """Test 12."""
    conn, _ = load_data()
    with open("homework/pregunta_12.sql", encoding="utf-8") as file:
        query = file.read()
    print(pd.read_sql_query(query, conn))

def test_13():
    """Test 13."""
    conn, _ = load_data()
    with open("homework/pregunta_13.sql", encoding="utf-8") as file:
        query = file.read()
    result = pd.read_sql_query(query, conn).to_dict()

    # Round the results to 2 decimal places
    result['avg(c12)'] = {k: round(v, 2) for k, v in result['avg(c12)'].items()}

    return result

def test_14():
    """Test 14."""
    conn, _ = load_data()
    with open("homework/pregunta_14.sql", encoding="utf-8") as file:
        query = file.read()
    result = pd.read_sql_query(query, conn).to_dict()

    # Round the results to 2 decimal places
    result['avg(c21)'] = {k: round(v, 2) for k, v in result['avg(c21)'].items()}

    return result


print(test_14())