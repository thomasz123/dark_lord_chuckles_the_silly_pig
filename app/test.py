import sqlite3
import flask
import pandas as pd

sex=True
pollution=True
smoke=True
alc=True
options = [sex,pollution,smoke,alc]
   
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

df = df[df['user'] == "12345678"]
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
# print(df)
DB_FILE_STROKE="lung.db"
db3 = sqlite3.connect(DB_FILE_STROKE)
c3 = db3.cursor()

table_stroke = c3.execute("SELECT * FROM lung;").fetchall()
db3.commit()
db3.close()
lung_df = pd.DataFrame(table_stroke, columns=['id','age','gender','pollution','alc','smoke','level'])
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

risk = len(lung_df_high) + 0.5*len(lung_df_mid)

print("your overall probability of getting a stroke is " + str(round((100*risk/len(lung_df)),2)) + "%")

lung_df=lung_df.sort_values(by=['age'])
print(lung_df)
ages=lung_df['age'].unique()
age_prob={}
if user_age < 22:
    for x in range(user_age,22):
        age_prob[x] = 0
for x in ages:
    lung_age = lung_df.loc[lung_df['age'] == x]
    lung_age_high = lung_age.loc[lung_age['level'] == 'High']
    lung_age_mid = lung_age.loc[lung_age['level'] == 'Medium']
    r = len(lung_age_high) + 0.5*len(lung_age_mid)
    age_prob[x] = round((100*r/len(lung_age)),2)
print(age_prob)

# # acquihire.loc[(acquihire["last_funding_on"] <= expiration) & 
# # (acquihire["total_funding_usd"] < 15000000) & (acquihire['ics_percentile'] >= 0.8) & 
# # (acquihire['last_funding_on'] >= added_expiration) , "aqui-hire"] = True
# print(user)