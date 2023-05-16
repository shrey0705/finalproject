import mysql.connector as sql

conn = sql.connect(host="localhost", user="root", password="Shr3y3sh")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE USER 'finalproj'@'localhost' IDENTIFIED BY 'ubuntu';"
cur.execute(cmd)

cmd = "GRANT ALL PRIVILEGES ON *.* TO 'finalproj'@'localhost' WITH GRANT OPTION;"
cur.execute(cmd)

cmd = "FLUSH PRIVILEGES;"
cur.execute(cmd)

conn.close()
