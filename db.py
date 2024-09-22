import sqlite3

con = sqlite3.connect("maya.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primay key ,name VARCHAR(100) , )"