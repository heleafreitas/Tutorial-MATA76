import sqlite3

DB_PATH = "../todolist.sqlite"

QUERY_CREATE_TABLE_ACTIVITIES = """CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            description TEXT, 
            date DATE,
            start_time TIME,
            end_time TIME,
            status TEXT)"""

QUERY_INSERT_TABLE_ACTIVITIES = """
    INSERT INTO activities(name, description, date, start_time, end_time, status)
    VALUES
"""

def create_connection(db_file) -> sqlite3.Connection:
    conn = None
    conn = sqlite3.connect(db_file)

    return conn

def execute_query(query : str, data : tuple = None) -> None:
    conn = create_connection(DB_PATH)
    cur = conn.cursor()
    if data:
        cur.execute(query, data)
    else:
        cur.execute(query)
    conn.commit()

def select_from_table(table_name : str = None, custom_query : str = None) -> list[tuple]:
    conn = create_connection(DB_PATH)
    cur = conn.cursor()
    if not custom_query:
        cur.execute(f"SELECT * FROM {table_name}")
    else:
        print(custom_query)
        cur.execute(custom_query)

    rows = cur.fetchall()

    return rows

if __name__ == '__main__':
    select_from_table(table_name='activities')

# ---------------  create ---------------
#c.execute("INSERT INTO activities (name, description, date, start_time, end_time, status) VALUES ('Alberto', 'Banco de dados do tutorial', '2023-09-16', '09:00:00', '09:30:00', 'feito')")


# --------------- read ---------------
'''c.execute("SELECT * FROM activities")
rows = c.fetchall()
for row in rows:
    print(row)'''


# --------------- update ---------------

# Update a specific row
#c.execute("UPDATE activities SET status='started' WHERE rowid=1")

# Update multiple rows  
#c.execute("UPDATE activities SET status='finished' WHERE date='2023-02-15'")


# --------------- delete ---------------

# Delete by name
#c.execute("DELETE FROM activities WHERE name='Alberto'")

# Delete all unfinished activities
#c.execute("DELETE FROM activities WHERE status='not started'")