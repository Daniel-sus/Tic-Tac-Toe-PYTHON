from flask import Flask, render_template, request, jsonify
from game import TicTacToe

app = Flask(__name__)

num_players = 2  # Default number of players
player_names = ['Player 1', 'Player 2']  # Default player names
grid_size = 5  # Default grid size
game = None  # Initialize the game object


@app.route('/')
def index():
    global game
    game = TicTacToe(num_players, player_names, grid_size)  # Initialize the game
    return render_template('index.html', grid_size=grid_size, current_player=player_names[0])


@app.route('/make_move', methods=['POST'])
def make_move():
    global game
    if not game:
        return jsonify({'error': 'Game has not been initialized.'}), 500

    data = request.json
    row = data['row']
    col = data['col']
    result, winner, winning_cells = game.make_move(row, col)  # Include winning_cells in the response
    return jsonify({'result': result, 'winner': winner, 'winning_cells': winning_cells, 'current_player': game.current_player})


if __name__ == '__main__':
    app.run(debug=True)
