import random
import sqlite3
import pandas as pd
from flask import Flask, redirect, render_template, request, session, url_for
#import utl.tables as tables

# sqlite
DB_FILE_1 = "userinfo.db"
db1 = sqlite3.connect(DB_FILE_1, check_same_thread=False)
c1 = db1.cursor()

DB_FILE_2 = "stroke_question.db"
db2 = sqlite3.connect(DB_FILE_2, check_same_thread=False)
c2 = db2.cursor()

# user login table
command1 = "create table IF NOT EXISTS login(user TEXT, password TEXT)"
c1.execute(command1)
db1.commit()

command2 = "create table IF NOT EXISTS stroke_question(user TEXT, name TEXT, height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, heart INTEGER, smokes TEXT);"
c2.execute(command2)
db2.commit()

# flask
app = Flask(__name__)
app.secret_key = 'a\8$x5T!H2P7f\m/rwd[&'

#replace file paths with your own
data = pd.read_csv('data/archive/healthcare-dataset-stroke-data.csv')

#drop irrelevent columns
data=data.drop(columns=['hypertension','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level'])

#write modified csv into a file
data.to_csv("stroke.csv", index=False)


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


@app.route("/strokequestions")
def questions():
    print("***********************")
    print(request.method)
    return render_template('stroke_question.html')

@app.route("/test")
def test_questions():
    return render_template('test.html')
@app.route("/test", methods = ['GET', 'POST'])
def test():
    sex=None
    bmi=None
    smoke=None
    heart=None
    options = [sex,bmi,smoke,heart]

    if request.method == 'POST':
        if request.form.get('sex1'):
            _sex = request.form['sex1']
            options[0] = _sex
        if request.form.get('bmi1'):
            _bmi = request.form['bmi1']
            options[1] = _bmi
        if request.form.get('smokingstatus1'):
            _smokingstatus = request.form['smokingstatus1']
            options[2] = _smokingstatus
        if request.form.get('heartdisease1'):
            _heartdisease = request.form['heartdisease1']
            options[3] = _heartdisease
    DB_FILE_2 = "stroke_question.db"
    db2 = sqlite3.connect(DB_FILE_2, check_same_thread=False)
    c2 = db2.cursor()
    data = c2.execute("SELECT * FROM stroke_question").fetchall()
    db2.commit()
    db2.close()

    data_mod=[]
    for x in data:
        data_mod.append(list(x))

    df = pd.DataFrame(data_mod, columns =['user','name','height','weight','sex','age','heart', 'smoking status'])
    df = df[df['user'] == session['username']]
    user = df.iloc[0][0]
    user_name = df.iloc[0][1]
    user_height = df.iloc[0][2]
    user_weight = df.iloc[0][3]
    user_sex = df.iloc[0][4]
    if user_sex == "female":
        user_sex = 'Female'
    else:
        user_sex = "Male"
    user_age = df.iloc[0][5]
    user_heart = df.iloc[0][6]
    user_bmi = user_weight/(user_height*user_height)*703
    user_smoke = df.iloc[0][7]

    DB_FILE_STROKE="stroke.db"
    db3 = sqlite3.connect(DB_FILE_STROKE)
    c3 = db3.cursor()

    table_stroke = c3.execute("SELECT * FROM stroke;").fetchall()
    db3.commit()
    db3.close()
    stroke_df = pd.DataFrame(table_stroke, columns=['id','gender','age','heart','bmi','status','stroke'])
    for x in range(4):
        if options[x] != None:
            if x == 0:
                stroke_df = stroke_df.loc[stroke_df['gender'] == user_sex ]
            if x == 1:
                stroke_df = stroke_df.loc[(stroke_df['bmi'] >= user_bmi-10) & (stroke_df['bmi'] <= user_bmi+10)]
            if x == 2:
                stroke_df = stroke_df.loc[stroke_df['status'] == user_smoke]
            if x == 3:
                stroke_df = stroke_df.loc[stroke_df['heart'] == user_heart]

    stroke_df_yes = stroke_df.loc[stroke_df['stroke'] == 1]
    if len(stroke_df) == 0:
        overall = "your overall probability of getting a stroke is " +  "0%"
    else:
        overall="your overall probability of getting a stroke is " + str(round((100*len(stroke_df_yes)/len(stroke_df)),2)) + "%"


    stroke_df=stroke_df.sort_values(by=['age'])
    ages=stroke_df['age'].unique()
    age_prob={}
    for x in ages:
        stroke_age = stroke_df.loc[stroke_df['age'] == x]
        stroke_age_yes = stroke_age.loc[stroke_age['stroke'] == 1]
        if len(stroke_age) == 0:
            age_prob[x] = 0
        else:
            age_prob[x] = round((100*len(stroke_age_yes)/len(stroke_age)),2)
    print(age_prob)
    return render_template('test.html', overall = overall, all=age_prob)


@app.route("/strokequestions", methods = ['GET', 'POST'])
def questionVals():
    print(request.method)
    print("))))))))))))))))))))))))")
   # if request.method == 'GET':
    _name = request.form['name']
    _height = request.form['height']
    _weight = request.form['weight']
    _sex = request.form['sex']
    _age = request.form['age']
    # _eathealthy = request.form['eathealthy']
    # _allergies = request.form['allergies']
    # _exercise = request.form['exercise']
    # _meditation = request.form['meditation']
    # _sleep = request.form['sleep']
    # _checkups = request.form['checkups']
    _heart = request.form['heart']
    _smoke = request.form['smoke']
    # _twodiabetes = request.form['twodiabetes']
    # _alcohol = request.form['alcohol']
    # _drugs = request.form['drugs']
    # _disorders = request.form['disorders']
    # _feelhealthy = request.form['feelhealthy']

    #should replace values when new answers are submited
    c2.execute("DELETE FROM stroke_question WHERE user = (?)", (session['username'],))
    c2.execute("INSERT INTO stroke_question VALUES (?,?,?,?,?,?,?,?);", (session['username'], _name, _height, _weight, _sex, _age, _heart,_smoke))
    print("test)*****************************")
    print( c2.execute("SELECT name, height, weight, sex, age, heart, smokes FROM stroke_question WHERE user = (?)", (session['username'],) ).fetchall())
    db2.commit()
    
    return redirect("/strokeresults")
   # return render_template('stroke_question.html')


@app.route("/strokeresults", methods = ['GET', 'POST'])
def results():
    DB_FILE_STROKE="stroke.db"
    db3 = sqlite3.connect(DB_FILE_STROKE)
    c3 = db3.cursor()
    c3.execute("create table if not exists stroke(id INTEGER, gender TEXT, age INTEGER, disease INTEGER, bmi INTEGER, status TEXT, stroke INTEGER);")

    data.to_sql('stroke',db3,if_exists='replace',index=False)
    
    table_stroke = c3.execute("SELECT * FROM stroke;").fetchall()
    db3.commit()
    db3.close()

    DB_FILE_STROKE_QUESTION="stroke_question.db"
    db4 = sqlite3.connect(DB_FILE_STROKE_QUESTION)
    c4 = db4.cursor()
    table_question = c4.execute("SELECT name, height, weight, sex, age, heart, smokes FROM stroke_question WHERE user = (?)", (session['username'],) ).fetchall()
    print(table_question)
    # db4.commit()
    # db4.close()

    # bmi = weight (lb) / [height (in)]2 x 703
    weight = c4.execute("select weight from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
    print(weight)
    height = c4.execute("select height from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
    bmi = weight / (height * height) * 703
    #TO DO: Add username as a parameter to questionnaire to display only their results
    db4.commit()
    db4.close()
    return render_template('results.html', disp=table_stroke, ques=table_question, bmi=bmi)


@app.route("/recommendations")
def recommendations():
    return render_template('recommendations.html')

        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()