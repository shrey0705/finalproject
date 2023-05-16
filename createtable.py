import mysql.connector as sql
conn = sql.connect(host="localhost", user="finalproj", password="ubuntu", database="cucina_db")
cur = conn.cursor()
cmd = "CREATE TABLE reservations ( \
  CusName TEXT NOT NULL, \
  CusDate DATE NOT NULL, \
  CusTime TIME NOT NULL, \
  CusParty INTEGER NOT NULL)"
cur.execute(cmd)
conn.close()
