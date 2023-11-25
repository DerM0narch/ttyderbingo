from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import random
import json
import secrets
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe()

# Form for Bingo Configuration
class BingoForm(FlaskForm):
    seed = StringField("Seed")
    submit = SubmitField("Play")


def get_bingo_challenges(seed=""):
    if seed != "":
        random.seed(seed)

    # get all challenges
    with open('static/challenges.json') as f:
        challenges = json.load(f)

    # get 24 random challenges (excluding the 13th)
    bingo_grid_keys = random.sample(sorted(challenges.keys()), 24)

    # add the 13th challenge from static/locations.json
    with open('static/locations.json') as f:
        locations = json.load(f)
    
    # randomly select a location and add it as the 13th challenge
    random_location = random.choice(sorted(locations.keys()))
    bingo_grid_keys.insert(12, random_location)

    # create the final dictionary
    challenges.update(locations)
    bingo_grid = {key: challenges[key] for key in bingo_grid_keys}

    return bingo_grid



@app.route('/', methods=['GET', 'POST'])
def main():
    seed = None
    form = BingoForm()
    if form.validate_on_submit():
        seed = form.seed.data
        return render_template('bingo.html', bingo_grid_list=list(get_bingo_challenges(seed).items()))
    return render_template('index.html', seed=seed, form=form)


# @app.route("/bingo")
# def bingo():
#         # get the bingo challenges
#     bingo_grid = get_bingo_challenges()
#     bingo_grid_list = list(bingo_grid.items())

#     # render the template
#     return render_template('bingo.html', bingo_grid_list=bingo_grid_list)


@app.route('/changelog')
def changelog():
    return render_template('changelog.html')


if __name__ == "__main__":
    app.run(debug=True)