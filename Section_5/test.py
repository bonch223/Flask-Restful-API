import sqlite3 

conn = sqlite3.connect('./Section_5/code/data.db')

cursor = conn.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

users = [
    (1, 'admin0', '1234'),
    (2, 'admin1', '1234'),
    (3, 'admin2', '1234'),
    (4, 'admin3', '1234')
]

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

conn.commit()
conn.close()