from flask import Flask, render_template, jsonify
from flask_cors import CORS
from pig_game import play_game

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll/<int:players>')
def roll(players):

    if 2 <= players <= 4:
        winner = play_game(players)
        return jsonify({'success': True, 'winner': winner})
    else:
        return jsonify({'success': False, 'error': 'Invalid number of players'})

if __name__ == '__main__':
    app.run(debug=True)