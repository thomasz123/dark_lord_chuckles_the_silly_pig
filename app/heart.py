import pandas as pd 
import sqlite3

#replace file paths with your own
data = pd.read_csv('data/archive/healthcare-dataset-stroke-data.csv')

#drop irrelevent columns
data=data.drop(columns=['hypertension','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level'])

#plot male and female lines showing correlation between age and __

DB_FILE="heart.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute("create table if not exists heart(id INTEGER, gender TEXT, age INTEGER, disease INTEGER, bmi INTEGER, status TEXT, stroke INTEGER);")
    #c.execute("create table if not exists questionnaire(height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, eathealthy INTEGER, allergies INTEGER, exercise INTEGER, meditation INTEGER, sleep INTEGER, checkups INTEGER, stroke INTEGER, onediabetes INTEGER, twodiabetes INTEGER, alcohol INTEGER, drugs INTEGER, disorders INTEGER, feelhealthy INTEGER);")
    #c.execute("insert into questionnaire values(160, 110, 1, 17, 7, 1, 3, 0, 9, 2, 0, 1, 0, 1, 0, 1, 5);")
data.to_sql('heart',db,if_exists='replace',index=False)
#write modified csv into a file
data.to_csv("heart_disease.csv", index=False)

table = c.execute("SELECT * FROM heart;").fetchall()
print(table)
db.commit()
db.close()

