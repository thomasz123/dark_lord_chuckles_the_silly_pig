import pandas as pd 

#replace file paths with your own
data = pd.read_csv('dark_lord_chuckes_the_silly_pig/data/archive/healthcare-data-set-data.csv')

#drop irrelevent columns
data=data.drop(columns=['hypertension','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level'])

#plot male and female lines showing correlation between age and 

#write modified csv into a file
data.to_csv("heart_disease.csv", header=0)

