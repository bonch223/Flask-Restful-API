import sqlite3

conn = sqlite3.connect('./Section_5/code/data.db')
cursor = conn.cursor()

create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table_users)

create_table_items = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table_items)

conn.commit()
conn.close()