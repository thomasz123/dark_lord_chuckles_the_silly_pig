import random
from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__) 

@app.route("/")       
def auth():
    # print("the __name__ of this module is... ")
    # print(__name__)
    return render_template('auth.html')

# @app.route("/login")
# def login():
#     if 'username' in session: #if there is a session going on, will direct to home page
#         return render_template('home.html')
#     return render_template('login.html')  #if no session, will prompt to login

# @app.route("/register")
# def register():
    

# @app.route("/verifylogin", methods = ['GET', 'POST'])
# def login():
#     if (table_handler.user_check(request.form["username"]) == True):
#         if (table_handler.password_check(request.form["username"], request.form["password"]) == True):
#             session['username'] = request.form['username']
#             return redirect('/')
#         else:
#             flash("Invalid username/password", "danger")
#             return render_template('login.html')
#     else: 
#         flash("Please enter your username/password", "danger")
#         return render_template('login.html')

# @app.route("/registrate", methods = ['GET', 'POST'])
# def registration():
#     if (table_handler.registrate(request.form["createusername"], request.form["createpassword"]) == False):
#         flash("That username is already taken", "danger")
#         return render_template('register.html')
#     else:
#         flash("Successfully signed up!", "success")
#         return render_template('login.html')
        
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#  <p>Use the arrow keys to navigate through the maze!</p>                                                                         <canvas id="maze"></canvas>                                                                                             <script src="maze.js"></script>                                                                                 </div>                                                                                                             
#  <script type="text/javascript" src="{{ url_for('static', filename='js/maze.js') }}"></script> 
#  <script src="maze.js"></script>