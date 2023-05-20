import random
import sqlite3
import pandas as pd
from flask import Flask, redirect, render_template, request, session, url_for
#import utl.tables as tables

# sqlite
DB_FILE_1 = "userinfo.db"
db1 = sqlite3.connect(DB_FILE_1, check_same_thread=False)
c1 = db1.cursor()

DB_FILE_2 = "question.db"
db2 = sqlite3.connect(DB_FILE_2, check_same_thread=False)
c2 = db2.cursor()

# user login table
command1 = "create table IF NOT EXISTS login(user TEXT, password TEXT)"
c1.execute(command1)
db1.commit()

command2 = "create table IF NOT EXISTS questionnaire(user TEXT, name TEXT, height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, eathealthy INTEGER, allergies INTEGER, exercise INTEGER, meditation INTEGER, sleep INTEGER, checkups INTEGER, stroke INTEGER, onediabetes INTEGER, twodiabetes INTEGER, alcohol INTEGER, drugs INTEGER, disorders INTEGER, feelhealthy INTEGER);"
c2.execute(command2)
db2.commit()

# flask
app = Flask(__name__)
app.secret_key = 'a\8$x5T!H2P7f\m/rwd[&'

#heart
#replace file paths with your own
data = pd.read_csv('data/archive/healthcare-dataset-stroke-data.csv')

#drop irrelevent columns
data=data.drop(columns=['hypertension','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level'])


#plot male and female lines showing correlation between age and 


#tables.setup()


@app.route("/")
def index():
    # if there is a session in place, divert the user to the main page
    if 'username' in session:
        return redirect("/home")
    else:
        return render_template('login.html', login="Not logged in!")


# ACCOUNT INFO CHECK
@app.route('/home', methods=['GET', 'POST'])
def authenticate():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        c1.execute("SELECT password FROM login WHERE user = (?);", (username,))

        try:
            x = c1.fetchall()[0][0]
            if x != password:
                return render_template('login.html', login="Invalid Password!")
            session['username'] = username
        except:
            return render_template('login.html', login="Submitted username is not registered!")
    if 'username' not in session:
        return redirect("/")
    
    return render_template('home.html', status="Successfully logged in!")


# LOGGING IN SYSTEM
@app.route("/register")
def register():
    return render_template('register.html', status="Register here!")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    newUser = request.form['username']
    newPass = request.form['password']

    print(len(newUser))
    print(len(newPass))

    if len(newUser) < 8 or len(newPass) < 8 :
        return render_template('register.html', status="Username and Password must be at least 8 characters long!")

    c1.execute("SELECT * FROM login;")
    user_logins = c1.fetchall()

    for user in user_logins:
        if newUser == user[0]:
            return render_template('register.html', status="Submitted username is already in use.")

    c1.execute("INSERT INTO login VALUES (?,?);", (newUser, newPass))
    db1.commit()
    
    return render_template('login.html', login="New user has been created successfully! Log in with your new credentials!")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/questions")
def questions():
    return render_template('questionnaire.html')


@app.route("/questionnaire", methods = ['GET', 'POST'])
def questionVals():
    print(request.method)
    if request.method == 'POST':
        _name = request.form['name']
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

        #should replace values when new answers are submited
        c2.execute("DELETE FROM questionnaire WHERE user = (?)", (session['username'],))
        c2.execute("INSERT INTO questionnaire VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (session['username'], _name, _height, _weight, _sex, _age, _eathealthy, _allergies, _exercise, _meditation, _sleep, _checkups, _stroke, _onediabetes, _twodiabetes, _alcohol, _drugs, _disorders, _feelhealthy))
        db2.commit()
        
        return redirect(url_for('results'))
    return render_template('results.html')


@app.route("/results")
def results():
    DB_FILE_HEART="heart.db"
    db3 = sqlite3.connect(DB_FILE_HEART)
    c3 = db3.cursor()
    c3.execute("create table if not exists heart(id INTEGER, gender TEXT, age INTEGER, disease INTEGER, bmi INTEGER, status TEXT, stroke INTEGER);")

    data.to_sql('heart',db3,if_exists='replace',index=False)
    #write modified csv into a file
    data.to_csv("heart_disease.csv", index=False)

    table_heart = c3.execute("SELECT * FROM heart;").fetchall()
    db3.commit()
    db3.close()

    DB_FILE_QUESTION="question.db"
    db4 = sqlite3.connect(DB_FILE_QUESTION)
    c4 = db4.cursor()
    table_question = c4.execute("SELECT name, height, weight, sex, age, eathealthy, allergies, exercise, meditation, sleep FROM questionnaire WHERE user = (?)", (session['username'],) ).fetchall()
    db4.commit()
    db4.close()

    #TO DO: Add username as a parameter to questionnaire to display only their results

    return render_template('results.html', disp=table_heart, ques=table_question)


@app.route("/recommendations")
def recommendations():
    return render_template('recommendations.html')

        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()