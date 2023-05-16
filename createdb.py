import mysql.connector as sql

conn = sql.connect(host="localhost", user="finalproj", password="ubuntu")
cur = conn.cursor()

cmd = "CREATE DATABASE cucina_db"
cur.execute(cmd)
conn.close()
