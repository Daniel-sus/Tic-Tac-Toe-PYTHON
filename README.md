# Tic-Tac-Toe Game

This is a simple browser-based Tic-Tac-Toe game implemented in Python using Flask.

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

3. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

4. Fill in the `game-init.json` file with the desired game configuration. See below for the file structure.

## Configuration

The `game-init.json` file contains information about the number of players, their names, and the size of the game board. It should be structured as follows:

```json
{
    "num_players": 2,
    "player_names": ["Player 1", "Player 2"],
    "grid_size": 5,
    "player_symbols": {
        "Player 1": "#",
        "Player 2": "$"
    }
}
```
"num_players": Specifies the number of players for the game.

"player_names": Provides a list of player names. The number of names should match the number of players.

"grid_size": Determines the size of the game board. It represents the number of rows and columns in the grid.

"player_symbols" (optional): Maps player names to symbols. If provided, each player will be assigned the specified symbol. If not provided, symbols will be randomly assigned.
## Run

1. After configuring the game-init.json file, run the Flask application:

   ```
   python app.py
   ```
2. Open a web browser and navigate to http://localhost:5000 to play the game.


3. Follow the on-screen instructions to take turns making moves and enjoy the game!

