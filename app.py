"""Define two routes, one to input the answers for the story
and the other to actually show the story.
"""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x74kj5'

debug = DebugToolbarExtension(app)

@app.route('/home')
def show_form():
    """Get the list of prompts and render the homepage."""    
    our_prompts = story.prompts

    return render_template('home.html', our_prompts = our_prompts)

@app.route('/story')
def show_story():
    """Make a dictionary where the keys are the prompts and the 
    values are the answers for the prompts.
    """
    answer = {}
    for key in request.args:
        answer[key] = request.args[key]
    return render_template('story.html', story = story.generate(answer))