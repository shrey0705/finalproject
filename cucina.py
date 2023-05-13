import sqlite3

conn = sqlite3.connect('cucina.db')

print("Opened database successfully!")

conn.execute('CREATE TABLE reservations (CusName TEXT NOT NULL, CusDate DATE NOT NULL, CusTime TIME NOT NULL, CusParty INTEGER NOT NULL)')

print ("Table created successfully")

conn.close
