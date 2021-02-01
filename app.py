from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'x74kj5'

debug = DebugToolbarExtension(app)

@app.route('/home')
def show_form():
    ans = {'place': 'london', 'noun': 'Bird', 'verb': 'jump', 'adjective': 'funny',
     'plural_noun': 'cars'}
    our_prompts = story.prompts

    return render_template('home.html', our_prompts = our_prompts)

@app.route('/story')
def show_story():
    answer = {}
    for prompt in story.prompts:
        answer[prompt] = request.args[prompt]
    return render_template('story.html', story = story.generate(answer))