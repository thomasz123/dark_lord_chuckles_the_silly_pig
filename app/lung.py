import pandas as pd 
import sqlite3

#replace file paths with your own
data = pd.read_csv('data/archive/cancer_patient_data_sets.csv')

#drop irrelevent columns
data=data.drop(columns=['Patient Id', 'Dust Allergy', 'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease', 'Balanced Diet', 'Obesity', 'Passive Smoker', 'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing', 'Swallowing Difficulty', 'Clubbing of Finger Nails', 'Frequent Cold', 'Dry Cough', 'Snoring'])

DB_FILE="lung.db"
db = sqlite3.connect(DB_FILE)
c = db.cursor()
c.execute("CREATE TABLE if not exists lung(id INTEGER, age INTEGER, gender INTEGER, airpollution INTEGER, alcoholuse INTEGER, smoking INTEGER, level TEXT);")
data.to_sql('lung',db,if_exists='replace',index=False)
#write modified csv into a file
data.to_csv("lung_cancer.csv", index=False)

table = c.execute("SELECT * FROM lung;").fetchall()
print(table)
db.commit()
db.close()