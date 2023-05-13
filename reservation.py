from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/cusres')
def cusres():
   return render_template('cusres.html')


@app.route('/staffinfo',methods = ['POST', 'GET'])
def staffinfo():
   if request.method == 'POST':
      try:
         CusName = request.form['CusName']
         CusDate = request.form['CusDate']
         CusTime = request.form['CusTime']
         CusParty = request.form['CusParty']
         
         with sql.connect("cucina.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO reservations (CusName,CusDate,CusTime,CusParty) VALUES ('{0}','{1}','{2}','{3}')".format(CusName,CusDate,CusTime,CusParty)
            cur.execute(cmd)
            
            con.commit()
            msg = "Reservation Successfully Created"
      except:
         con.rollback()
         msg = "An Error Occurred While Creating The Reservation, Please Try Again!"
         
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("cucina.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from reservations")
   
   rows = cur.fetchall(); 
   return render_template("staffinfo.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
