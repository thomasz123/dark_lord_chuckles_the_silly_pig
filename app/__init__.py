import random
from flask import Flask, redirect, render_template, request, session, url_for
app = Flask(__name__) 

@app.route("/")       
def auth():
    # print("the __name__ of this module is... ")
    # print(__name__)
    return render_template('auth.html')


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

#  <p>Use the arrow keys to navigate through the maze!</p>                                                                         <canvas id="maze"></canvas>                                                                                             <script src="maze.js"></script>                                                                                 </div>                                                                                                             
#  <script type="text/javascript" src="{{ url_for('static', filename='js/maze.js') }}"></script> 
#  <script src="maze.js"></script>