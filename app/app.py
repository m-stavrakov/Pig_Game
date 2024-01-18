from flask import Flask, render_template, jsonify
from pig_game import roll_dice, play_game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll():
    value = roll_dice()
    return jsonify({'value': value})

if __name__ == '__main__':
    players = int(input("Enter the number of players (2-4): "))
    if 2 <= players >= 4:
        max_score, winning_idx = play_game(players)
        print(f"Player number {winning_idx} is the winner with a score of: {max_score}")
    else:
        print("Must be between 2 - 4 players.")

    app.run(debug=True)