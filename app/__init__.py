import random
import sqlite3
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

command2 = "create table IF NOT EXISTS questionnaire(height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, eathealthy INTEGER, allergies INTEGER, exercise INTEGER, meditation INTEGER, sleep INTEGER, checkups INTEGER, stroke INTEGER, onediabetes INTEGER, twodiabetes INTEGER, alcohol INTEGER, drugs INTEGER, disorders INTEGER, feelhealthy INTEGER);"
c2.execute(command2)
db2.commit()

# flask
app = Flask(__name__)
app.secret_key = 'a\8$x5T!H2P7f\m/rwd[&'

#tables.setup()

@app.route("/")
def index():
    # if there is a session in place, divert the user to the main page
    if 'username' in session:
        return redirect("/home")
    else:
        return render_template('login.html', login="Not logged in!")

@app.route('/home', methods=['GET', 'POST'])
def authenticate():

    ##### ACCOUNT INFO CHECK
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

########################### LOGGING IN SYSTEM ###########################
@app.route("/register")
def register():
    return render_template('register.html')

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

    c2.execute("INSERT INTO questionnaire VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (_height, _weight, _sex, _age, _eathealthy, _allergies, _exercise, _meditation, _sleep, _checkups, _stroke, _onediabetes, _twodiabetes, _alcohol, _drugs, _disorders, _feelhealthy))
    db2.commit()

    return render_template('results.html')


@app.route("/results")
def results():
    return render_template('results.html')


@app.route("/recommendations")
def recommendations():
    return render_template('recommendations.html')

        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#  <p>Use the arrow keys to navigate through the maze!</p>                                                                         <canvas id="maze"></canvas>                                                                                             <script src="maze.js"></script>                                                                                 </div>                                                                                                             
#  <script type="text/javascript" src="{{ url_for('static', filename='js/maze.js') }}"></script> 
#  <script src="maze.js"></script>