import random
import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for
#import utl.tables as tables

DB_FILE = "question.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)
c = db.cursor()

command = "create table IF NOT EXISTS questionnaire(height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, eathealthy INTEGER, allergies INTEGER, exercise INTEGER, meditation INTEGER, sleep INTEGER, checkups INTEGER, stroke INTEGER, onediabetes INTEGER, twodiabetes INTEGER, alcohol INTEGER, drugs INTEGER, disorders INTEGER, feelhealthy INTEGER);"
c.execute(command)
db.commit()

app = Flask(__name__) 

#tables.setup()

# @app.route("/")       
# def auth(): 
#     if not 'username' in session:
#         return render_template('home.html')
#     else:
#         return render_template('auth.html')

# @app.route("/login")
# def login():
#     if 'username' in session: #if there is a session going on, will direct to home page
#         return render_template('home.html')
#     return render_template('login.html')  #if no session, will prompt to login

# @app.route("/register", methods = ['GET', 'POST'])
# def register():

@app.route("/")
def idk():
    return render_template('questionnaire.html')

@app.route("/questionnaire", methods = ['GET', 'POST'])
def questionVals():
    _height = request.form['height']
    _weight = request.form['weight']
    _sex = request.form['sex']
    _age = request.form['age']
    _eathealthy = request.form['eathealthy']
    _allergies = request.form['allergies']
    _exercise = request.form['exercise']
    _meditation = request.form['meditation']
    _sleep = request.form['sleep']
    _checkups = request.form['checkups']
    _stroke = request.form['stroke']
    _onediabetes = request.form['onediabetes']
    _twodiabetes = request.form['twodiabetes']
    _alcohol = request.form['alcohol']
    _drugs = request.form['drugs']
    _disorders = request.form['disorders']
    _feelhealthy = request.form['feelhealthy']

    c.execute("INSERT INTO questionnaire VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (_height, _weight, _sex, _age, _eathealthy, _allergies, _exercise, _meditation, _sleep, _checkups, _stroke, _onediabetes, _twodiabetes, _alcohol, _drugs, _disorders, _feelhealthy))
    db.commit()

    return render_template('questionnaire.html', height=_height, weight=_weight, sex=_sex, age=_age, eathealthy=_eathealthy, allergies=_allergies, exercise=_exercise, meditation=_meditation, sleep=_sleep, checkups=_checkups, stroke=_stroke, onediabetes=_onediabetes, twodiabetes=_twodiabetes, alcohol=_alcohol, drugs=_drugs, disorders=_disorders, feelhealthy=_feelhealthy)


# @app.route("/verifylogin", methods = ['GET', 'POST'])
# def login():
#     if (table_handlerpinegistrate(request.form["createusername"], request.form["createpassword"]) == False):
#         flash("That username is already taken", "danger")
#         return render_template('register.html')
#     else:
#         flash("Successfully signed up!", "success")
#         return render_template('login.html')
        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#  <p>Use the arrow keys to navigate through the maze!</p>                                                                         <canvas id="maze"></canvas>                                                                                             <script src="maze.js"></script>                                                                                 </div>                                                                                                             
#  <script type="text/javascript" src="{{ url_for('static', filename='js/maze.js') }}"></script> 
#  <script src="maze.js"></script>