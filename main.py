from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)
checklist = ["Item 1", "Item 2", "Item 3"]  # Initial checklist items


@app.route('/')
def home():


    return render_template('home.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/journal')
def journal():
    return render_template('journal.html')

@app.route('/schedule',methods=['GET','POST'])
def schedule():
    if request.method=='POST':
        add=True
        while add==True:
          conn=sqlite3.connect('schedule.db')
          cur=conn.cursor()

          event=request.form['event']
          date=request.form['date']
          time=request.form['time']
          location=request.form['location']

          cur.execute(""" CREATE TABLE IF NOT EXISTS schedule(Sid INTEGER PRIMARY KEY,
                                                         event TEXT,
                                                         location TEXT,
                                                         date TEXT,
                                                         time TEXT)""")

          cur.execute("""INSERT INTO schedule(event,location,date,time)
                    VALUES(?,?,?,?);""",(event,location,date,time))
          add=False
          conn.commit()
        cur.execute("""SELECT * FROM schedule;""")
        rows=cur.fetchall()
        conn.close()           
        return render_template('schedule.html',rows=rows)



    return render_template('schedule.html')


@app.route('/wotd', methods=['GET','POST'])
def wotd():
    if request.method=='POST':
        
        return render_template('wotd.html', checklist=checklist)
    return render_template('wotd.html', checklist=checklist)

app.run()
