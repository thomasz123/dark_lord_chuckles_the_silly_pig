# Health and Diet Recommendations by Dark Lord Chuckles The Silly Pig

## Roles
* Thomas Zhang (PM) - Flask, JS (logging in system, graph visuals, tying all of the parts together)
* Lauren Lee - Database/SQLite (storing CSV data, calculating stroke and lung cancer values)
* Diana Akhmedova - API, Database/SQLite, Bootstrap, HTML/CSS/JS (managing/storing/displaying API data, graph visuals, linking HTML pages)

## Description of Website/App
* The purpose of our website is to use provided data about a person's health to create visualizations. The visualizations include various line graphs that help the user detect their health trend. The user is able to choose which factors affect the values on each line graph, and receieve a percentage of how likely they are to develop a stroke and/or lung cancer. The website also provides diet recommendations using the EDAMAM API.

## APIs Used
* [EDAMAM Recipe API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_recipies.md)

## Data
### Description
* This dataset is used to predict a patient's likelyhood to get a stroke based on factors like gender, age, BMI, and smoking status. 
### Source
* [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

### Description
* This dataset provides information on patients with lung cancer like their age, smoking status, gender, and air pollution level.
### Source
* [Lung Cancer Prediction Dataset](https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link)

## Launch Codes
### How to Clone/Install
1. Create a virtual environment
```
python -m venv pig
source pig/bin/activate
```

2. Install packages
```
pip install -r requirements.txt
```

3. Clone repo using SSH or HTTPS
```
git clone git@github.com:thomasz123/dark_lord_chuckles_the_silly_pig.git
```
```
git clone https://github.com/thomasz123/dark_lord_chuckles_the_silly_pig.git
```

4. Get the ID and Key from the EDAMAM Recipe API website<br>
   (a) Go to the [EDAMAM Recipe API](https://developer.edamam.com/edamam-docs-recipe-api) website and create an account<br>
   (b) Go to your Dashboard and click on "Applications"<br>
   (c) Under Recipe Search API, press "View"<br>
   (d) Paste the Application ID into "key_api0" in the app/keys folder<br>
   (e) Paste the Application Key into "key_api1" in the app/keys folder

### How to Run
1. cd into app directory
```
cd app
```
2. Start Flask server 
```
python __init__.py
```
3. Go to ```http://127.0.0.1:5000/``` in browser
