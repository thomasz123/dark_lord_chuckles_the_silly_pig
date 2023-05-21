import sqlite3
import flask
import pandas as pd


sex=True
bmi=True
smoke=True
heart=None
options = [sex,bmi,smoke,heart]

    
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

df = df[df['user'] == "laurenlee"]
print(df)
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

print(df)
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
print("your overall probability of getting a stroke is " + str(round((100*len(stroke_df_yes)/len(stroke_df)),2)) + "%")

print(len(stroke_df_yes))
print(len(stroke_df))

stroke_df=stroke_df.sort_values(by=['age'])
ages=stroke_df['age'].unique()
age_prob={}
for x in ages:
    stroke_age = stroke_df.loc[stroke_df['age'] == x]
    stroke_age_yes = stroke_age.loc[stroke_age['stroke'] == 1]
    age_prob[x] = round((100*len(stroke_age_yes)/len(stroke_age)),2)
print(age_prob)




# acquihire.loc[(acquihire["last_funding_on"] <= expiration) & 
# (acquihire["total_funding_usd"] < 15000000) & (acquihire['ics_percentile'] >= 0.8) & 
# (acquihire['last_funding_on'] >= added_expiration) , "aqui-hire"] = True
print(user)