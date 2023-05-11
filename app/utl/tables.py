import sqlite3
DB_FILE="tables"

def setup():
    DB_FILE="question.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    #c.execute("create table if not exists users(username text primary key, password text);")
    #c.execute("create table if not exists questionnaire(height INTEGER, weight INTEGER, sex INTEGER, age INTEGER, eathealthy INTEGER, allergies INTEGER, exercise INTEGER, meditation INTEGER, sleep INTEGER, checkups INTEGER, stroke INTEGER, onediabetes INTEGER, twodiabetes INTEGER, alcohol INTEGER, drugs INTEGER, disorders INTEGER, feelhealthy INTEGER);")
    #c.execute("insert into questionnaire values(160, 110, 1, 17, 7, 1, 3, 0, 9, 2, 0, 1, 0, 1, 0, 1, 5);")
    db.commit()
    db.close()

def register():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    name = (username, )
    c.execute("select * from users where username = ?;", name)
    response = c.fetchall()
    # print(response)
    if (len(response) == 0):
        user = (username, password)
        c.execute("insert into users values (?, ?);", user)
        db.commit()
        db.close()
        return True
    db.commit()
    db.close()
    return False

def user_check(username):
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()

	name_tuple = (username, )
	c.execute("select * from users where username = ?;", name_tuple)
	response = c.fetchone()
	if (response == None):
		db.commit()
		db.close()
		return False
	db.commit()
	db.close()
	return True

def password_check(username, password):
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()

	name_tuple = (username, )
	c.execute("select password from users where username = ?;", name_tuple)
	response = c.fetchone()
	if (response != None and response[0] == password):
		db.commit()
		db.close()
		return True
	db.commit()
	db.close()
	return False

def display():
	DB_FILE="question.db"
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()
	print(c.execute("SELECT * FROM questionnaire;").fetchall())
	db.commit()
	db.close()


setup()
display()