from flask import Flask, render_template
import random
import json

app = Flask(__name__)

def get_bingo_challenges():
    # from static/challenges.json get 25 random challenges without duplicates the 13th challenge is pulled from static/locations.json

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



@app.route('/')
def main():
    # get the bingo challenges
    bingo_grid = get_bingo_challenges()
    bingo_grid_list = list(bingo_grid.items())

    # render the template
    return render_template('index.html', bingo_grid_list=bingo_grid_list)

@app.route('/changelog')
def changelog():
    return render_template('changelog.html')


if __name__ == "__main__":
    app.run(debug=True)