from flask import Flask, render_template, request
from tic_tac_toe.game import TicTacToe

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game', methods=['POST'])
def start_game():
    num_players = int(request.form['num_players'])
    player_names = [request.form[f'player{i+1}'] for i in range(num_players)]
    grid_size = int(request.form['grid_size'])

    # Initialize game
    game = TicTacToe(num_players, player_names, grid_size)

    # Start the game and handle logic
    # Implement the game logic here

    return "Game started"


if __name__ == '__main__':
    app.run(debug=True)
