# Health and Diet Recommendations by Dark Lord Chuckles The Silly Pig

## Roles
* Thomas Zhang (PM) - Flask, JS (logging in system, graph visuals, tying all of the parts together)
* Lauren Lee - Database/SQLite (storing CSV data, calculating stroke and lung cancer values)
* Diana Akhmedova - API, Bootstrap, HTML/CSS/JS (managing/storing/displaying API data, linking HTML pages, graph visuals)

## Description of Website/App
* The purpose of our website is to use provided data about a person's health to create visualizations. The visualizations include various line graphs that help the user detect their health trend. The user is able to choose which factors affect the values on each line graph, and receieve a percentage of how likely they are to develop a stroke and/or lung cancer. The website also provides diet recommendations using the EDAMAM API.

## APIs Used
* [EDAMAM Recipe API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_recipies.md)

## Data
### Description
* The dataset calculates the possibility of one having a heart attack using 14 attributes. This includes, age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, maximum heart rate achieved, and number of major vessels. In the dataset, the "target" field refers to the presence of heart disease in the patient, with 0 referrring to no or a lower chance of heart attack and 1 referring to a higher chance of heart attack.
### Source
* [Health care: Heart attack possibility](https://www.kaggle.com/datasets/nareshbhat/health-care-data-set-on-heart-attack-possibility)

### Description
* The dataset analyzes and evaluates workouts that one can do at the gym or at home to stay healthy. The exercises range from bodyweight to machine-based or dumbbell/barbell based. The dataset is useful in evaluating which exercise targets a specific muscle group the best and also provies visualizations of the exercise details. The csv file has more than 2500 rows of exercises.
### Source
* [Gym Exercise Dataset](https://www.kaggle.com/datasets/niharika41298/gym-exercise-data)

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
// ---------------------------- OR -----------------------------------------
git clone https://github.com/thomasz123/dark_lord_chuckles_the_silly_pig.git
```

4. Get the ID and key from the EDAMAM API website
    * Go to the [EDAMAM API](https://developer.edamam.com/edamam-docs-recipe-api) website and create an account
    * Go to your Dashboard and click on "Applications"
    * Under Recipe Search API, press "View"
    * Paste the Application ID into "key_api0" in the app/keys folder.
    * Paste the Application Key into "key_api1" in the app/keys folder.

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
