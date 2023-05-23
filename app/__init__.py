import random
import sqlite3
import pandas as pd
import requests
from flask import Flask, redirect, render_template, request, session, url_for

# sqlite
DB_FILE_1 = "userinfo.db"
db1 = sqlite3.connect(DB_FILE_1, check_same_thread=False)
c1 = db1.cursor()

DB_FILE_2 = "stroke_question.db"
db2 = sqlite3.connect(DB_FILE_2, check_same_thread=False)
c2 = db2.cursor()

DB_FILE_lung = "lung_question.db"
db_lung = sqlite3.connect(DB_FILE_lung, check_same_thread=False)
c_lung = db_lung.cursor()

# user login table
command1 = "create table IF NOT EXISTS login(user TEXT, password TEXT)"
c1.execute(command1)
db1.commit()

command2 = "create table IF NOT EXISTS stroke_question(user TEXT, name TEXT, height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, heart INTEGER, smokes TEXT);"
c2.execute(command2)
db2.commit()

command_lung = "create table IF NOT EXISTS lung_question(user TEXT, name TEXT, height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, alcohol INTEGER, pollution INTEGER, smokes TEXT);"
c_lung.execute(command_lung)
db_lung.commit()

# flask
app = Flask(__name__)
app.secret_key = 'a\8$x5T!H2P7f\m/rwd[&'

# replace file paths with your own
data = pd.read_csv('data/archive/healthcare-dataset-stroke-data.csv')

# drop irrelevent columns
data=data.drop(columns=['hypertension','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level'])

# write modified csv into a file
data.to_csv("stroke.csv", index=False)

# edamam recipe api
def recipe_search(ingredient):
    app_id = ''
    app_key = ''

    try:
        with open("keys/key_api0", "r") as f:
            app_id = f.read()
    except:
        print("NO ID")
    
    try:
        with open("keys/key_api1", "r") as f:
            app_key = f.read()
    except:
        print("NO KEY")

    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id,app_key))
    data = result.json()
    return data['hits']


# --- LOGIN ------------------------------------------------------------------------------------------------------
@app.route("/")
def index():
    # if there is a session in place, divert the user to the main page
    if 'username' in session:
        return redirect("/home")
    else:
        return render_template('login.html', login="Not logged in!")


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


# --- HOME ------------------------------------------------------------------------------------------------------
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


# --- QUESTIONNAIRE ------------------------------------------------------------------------------------------------
@app.route("/strokequestions")
def questions():
    print("***********************")
    print(request.method)
    return render_template('stroke_question.html')


@app.route("/strokequestions", methods = ['GET', 'POST'])
def questionVals():
    print(request.method)
    print("))))))))))))))))))))))))")
    _name = request.form['name']
    _height = request.form['height']
    _weight = request.form['weight']
    _sex = request.form['sex']
    _age = request.form['age']
    _heart = request.form['heart']
    _smoke = request.form['smoke']

    # replaces values when new answers are submited
    c2.execute("DELETE FROM stroke_question WHERE user = (?)", (session['username'],))
    c2.execute("INSERT INTO stroke_question VALUES (?,?,?,?,?,?,?,?);", (session['username'], _name, _height, _weight, _sex, _age, _heart, _smoke))
    print("test)*****************************")
    print( c2.execute("SELECT name, height, weight, sex, age, heart, smokes FROM stroke_question WHERE user = (?)", (session['username'],) ).fetchall())
    
    db2.commit()
    return redirect("/strokeresults")


@app.route("/lungcancerquestions", methods = ['GET', 'POST'])
def lungVals():
    print(request.method)
    print("))))))))))))))))))))))))")
    _name = request.form['name']
    _height = request.form['height']
    _weight = request.form['weight']
    _sex = request.form['sex']
    _age = request.form['age']
    _alcohol = request.form['alcohol']
    _smoke = request.form['smoke']
    _pollution = request.form['pollution']

    # replaces values when new answers are submited
    c_lung.execute("DELETE FROM lung_question WHERE user = (?)", (session['username'],))
    c_lung.execute("INSERT INTO lung_question VALUES (?,?,?,?,?,?,?,?,?);", (session['username'], _name, _height, _weight, _sex, _age, _alcohol, _pollution,_smoke))
    print("test)*****************************")
    print( c_lung.execute("SELECT name, height, weight, sex, age, alcohol, smokes FROM lung_question WHERE user = (?)", (session['username'],) ).fetchall())
    
    db_lung.commit()
    return redirect("/strokeresults")


# --- RESULTS ------------------------------------------------------------------------------------------------------
@app.route("/results")
def test_questions():
    return render_template('results.html')


@app.route("/results", methods = ['GET', 'POST'])
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
    if len(df) == 0:
        return render_template('results.html', status="Please fill out the questionnaire first!", status1="<br><hr><br>")

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
    if user_heart == "no":
        user_heart = 0
    else:
        user_heart = 1
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
        overall = "Your overall probability of getting a stroke is " + "0%"
    else:
        overall="Your overall probability of getting a stroke is " + str(round((100*len(stroke_df_yes)/len(stroke_df)),2)) + "%"

    stroke_df=stroke_df.sort_values(by=['age'])
    stroke_df=stroke_df.loc[stroke_df["age"] >= 1]
    print(stroke_df)

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
    x_vals = list(age_prob.keys())
    y_vals = list(age_prob.values())
    
    #Lung Chart Values
    sex=None
    pollution=None
    smoke=None
    alc=None
    options = [sex,pollution,smoke,alc]

    if request.method == 'POST':
        if request.form.get('sex2'):
            _sex = request.form['sex2']
            options[0] = _sex
        if request.form.get('airpollution2'):
            pollution = request.form['airpollution2']
            options[1] = pollution
        if request.form.get('smoking2'):
            _smokingstatus = request.form['smoking2']
            options[2] = _smokingstatus
        if request.form.get('alcoholuse2'):
            alc = request.form['alcoholuse2']
            options[3] = alc

    DB_FILE_2 = "lung_question.db"
    db2 = sqlite3.connect(DB_FILE_2, check_same_thread=False)
    c2 = db2.cursor()
    data = c2.execute("SELECT * FROM lung_question").fetchall()
    db2.commit()
    db2.close()

    data_mod=[]
    for x in data:
        data_mod.append(list(x))

    df = pd.DataFrame(data_mod, columns =['user','name','height','weight','sex','age','alcohol', 'pollution', 'smokes'])
    df = df[df['user'] == session['username']]
    if len(df) == 0:
        return render_template('results.html', status="Please fill out the questionnaire first!", status1="<br><hr><br>")
    # print(df)
    
    user = df.iloc[0][0]
    user_name = df.iloc[0][1]
    user_height = df.iloc[0][2]
    user_weight = df.iloc[0][3]
    user_sex = df.iloc[0][4]
    if user_sex == "female":
        user_sex = 2
    else:
        user_sex = 1
    user_age = df.iloc[0][5]
    user_alc = df.iloc[0][6]
    user_pollution = df.iloc[0][7]
    user_smoke = int(df.iloc[0][8])

    #print(user_smoke)
    #print(df)
    DB_FILE_STROKE="lung.db"
    db3 = sqlite3.connect(DB_FILE_STROKE)
    c3 = db3.cursor()

    table_lung = c3.execute("SELECT * FROM lung;").fetchall()
    db3.commit()
    db3.close()

    lung_df = pd.DataFrame(table_lung, columns=['id','age','gender','pollution','alc','smoke','level'])
    #print(lung_df)
    for x in range(4):
        if options[x] != None:
            if x == 0:
                lung_df = lung_df.loc[lung_df['gender'] == user_sex ]
            if x == 1:
                lung_df = lung_df.loc[(lung_df['pollution'] >= user_pollution-2) & (lung_df['pollution'] <= user_pollution+2)]
            if x == 2:
                lung_df = lung_df.loc[(lung_df['smoke'] >= user_smoke-2) & (lung_df['smoke'] <= user_smoke+2)]
            if x == 3:
                lung_df = lung_df.loc[(lung_df['alc'] >= user_alc-2) & (lung_df['alc'] <= user_alc+2)]

    print(lung_df)
    lung_df_mid = lung_df.loc[lung_df['level'] == "Medium"]
    lung_df_high = lung_df.loc[lung_df['level'] == "High"]

    risk = len(lung_df_high) + 0*len(lung_df_mid)
    overall1 = ("Your overall probability of getting lung cancer is " + str(round((100*risk/len(lung_df)),2)) + "%")

    lung_df=lung_df.sort_values(by=['age'])
    print(lung_df)
    ages=lung_df['age'].unique()
    age_prob1={}
    if user_age < 22:
        for x in range(user_age,22):
            age_prob1[x] = 0
    for x in ages:
        lung_age = lung_df.loc[lung_df['age'] == x]
        lung_age_high = lung_age.loc[lung_age['level'] == 'High']
        lung_age_mid = lung_age.loc[lung_age['level'] == 'Medium']
        r = len(lung_age_high) + 0*len(lung_age_mid)
        age_prob1[x] = round((100*r/len(lung_age)),2)
        
    x_vals1 = list(age_prob1.keys())
    y_vals1 = list(age_prob1.values())

    ### COPIED TO DISPLAY TABLE
    DB_FILE_STROKE_QUESTION="stroke_question.db"
    db4 = sqlite3.connect(DB_FILE_STROKE_QUESTION)
    c4 = db4.cursor()
    table_question = c4.execute("SELECT name, height, weight, sex, age, heart, smokes FROM stroke_question WHERE user = (?)", (session['username'],) ).fetchall()
    print(table_question)

    # bmi = weight (lb) / [height (in)]2 x 703
    weight = c4.execute("select weight from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
    print(weight)
    height = c4.execute("select height from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
    bmi = weight / (height * height) * 703
    bmi = round(bmi, 2)

    db4.commit()
    db4.close()

    ### COPIED TO DISPLAY TABLE
    DB_FILE_LUNG="lung.db"
    db_LUNG = sqlite3.connect(DB_FILE_LUNG)
    c_LUNG = db_LUNG.cursor()
    
    table_lung = c_LUNG.execute("SELECT * FROM lung;").fetchall()
    db_LUNG.commit()
    db_LUNG.close()

    DB_FILE_LUNG_QUESTION="lung_question.db"
    db_LUNGQ = sqlite3.connect(DB_FILE_LUNG_QUESTION)
    c_LUNGQ = db_LUNGQ.cursor()
    table_question_lung = c_LUNGQ.execute("SELECT name, height, weight, sex, age, alcohol, pollution, smokes FROM lung_question WHERE user = (?)", (session['username'],) ).fetchall()
    print(table_question_lung)

    bmi_lung=None

    if table_question_lung != []:
        # bmi = weight (lb) / [height (in)]2 x 703
        weight1 = c_LUNGQ.execute("select weight from lung_question where user = (?)", (session['username'],)).fetchall()[0][0]
        print(weight1)
        height1 = c_LUNGQ.execute("select height from lung_question where user = (?)", (session['username'],)).fetchall()[0][0]
        bmi_lung = weight1 / (height1 * height1) * 703
        bmi_lung = round(bmi_lung, 2)

    db_LUNGQ.commit()
    db_LUNGQ.close()
    return render_template('results.html', overall=overall, overall1=overall1, all=age_prob, all1=age_prob1, x=x_vals, y=y_vals, x1=x_vals1, y1=y_vals1, ques=table_question, ques1=table_question_lung, bmi=bmi)


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

    bmi=None

    if table_question != []:
        # bmi = weight (lb) / [height (in)]2 x 703
        weight = c4.execute("select weight from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
        print(weight)
        height = c4.execute("select height from stroke_question where user = (?)", (session['username'],)).fetchall()[0][0]
        bmi = weight / (height * height) * 703
        bmi = round(bmi, 2)

    db4.commit()
    db4.close()

    ### COPIED TO DISPLAY TABLE
    DB_FILE_LUNG="lung.db"
    db_LUNG = sqlite3.connect(DB_FILE_LUNG)
    c_LUNG = db_LUNG.cursor()
    
    table_lung = c_LUNG.execute("SELECT * FROM lung;").fetchall()
    db_LUNG.commit()
    db_LUNG.close()

    DB_FILE_LUNG_QUESTION="lung_question.db"
    db_LUNGQ = sqlite3.connect(DB_FILE_LUNG_QUESTION)
    c_LUNGQ = db_LUNGQ.cursor()
    table_question_lung = c_LUNGQ.execute("SELECT name, height, weight, sex, age, alcohol, pollution, smokes FROM lung_question WHERE user = (?)", (session['username'],) ).fetchall()
    print(table_question_lung)

    bmi_lung=None

    if table_question_lung != []:
        # bmi = weight (lb) / [height (in)]2 x 703
        weight1 = c_LUNGQ.execute("select weight from lung_question where user = (?)", (session['username'],)).fetchall()[0][0]
        print(weight1)
        height1 = c_LUNGQ.execute("select height from lung_question where user = (?)", (session['username'],)).fetchall()[0][0]
        bmi_lung = weight1 / (height1 * height1) * 703
        bmi_lung = round(bmi_lung, 2)

    db_LUNGQ.commit()
    db_LUNGQ.close()
    return render_template('results.html', disp=table_stroke, disp1=table_lung, ques=table_question, ques1=table_question_lung, bmi=bmi, bmi1=bmi_lung)


# --- RECOMMENDATIONS -----------------------------------------------------------------------------------------------
@app.route("/recommendations")
def recommendations():
    return render_template('recommendations.html')


@app.route('/search', methods=['GET', 'POST'])
def searchFood():
    if request.method == 'POST':
        DB_FILE_food = "food.db"
        db_food = sqlite3.connect(DB_FILE_food, check_same_thread=False)
        c_food = db_food.cursor()

        command_food = "create table IF NOT EXISTS food(user TEXT, label TEXT, calories INTEGER, mealtype TEXT, cuisinetype TEXT, url TEXT, image TEXT);"
        c_food.execute(command_food)
        c_food.execute("DELETE FROM food WHERE user = (?)", (session['username'],))

        searchItem = request.form['search']
        results = recipe_search(searchItem)

        for result in results:
            recipe = result['recipe']
            label = recipe['label']
            calories = round(int(recipe['calories']))
            mealType = recipe['mealType'][0]
            cuisineType = recipe['cuisineType'][0]
            url = recipe['url']
            image = recipe['image']
            c_food.execute("INSERT INTO food VALUES (?,?,?,?,?,?,?);", (session['username'], label, calories, mealType, cuisineType, url, image))
        
        table_food = c_food.execute("SELECT * FROM food;").fetchall()
        db_food.commit()
        db_food.close()
    return render_template('recommendations.html', food=table_food)

        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()