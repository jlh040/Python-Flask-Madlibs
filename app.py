from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x74kj5'

debug = DebugToolbarExtension(app)

@app.route('/home')
def show_form():
    return render_template('home.html')