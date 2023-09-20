import sqlite3

conn = sqlite3.connect('activities.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT,
            description TEXT, 
            date DATE,
            start_time TIME,
            end_time TIME,
            status TEXT)""")
'''
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

conn.commit()
conn.close()