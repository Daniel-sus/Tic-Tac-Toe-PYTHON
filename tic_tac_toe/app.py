import random
from game import TicTacToe
from pynput import keyboard
from pynput.keyboard import Key
from utils.selectFunctions import selectQuantityOfPlayers,selectPlayersNames,selectGridSize,selectPlayersSymbols
from utils.guiFunctions import print_board

# Game initialization 
print("Welcome to Tic Tac Toe game")
num_players = selectQuantityOfPlayers()
player_names = selectPlayersNames(num_players)
player_symbols = selectPlayersSymbols(player_names)
grid_size = selectGridSize()
current_player_index = random.randint(0, num_players-1)
game = TicTacToe(num_players, player_names, grid_size, current_player_index, player_symbols)
selectedCell = {"x": 0, "y": 0}
print_board(game.board, game.current_player, selectedCell)

def on_key_release(key):
    if key == Key.enter:
        result, winner, winning_cells = game.make_move(selectedCell["y"], selectedCell["x"])
        print_board(game.board, game.current_player, selectedCell)
        if winner:
            print()
            print()
            print()
            print("///////////////////////////")
            print("      WINNER: " + winner)
            print("///////////////////////////")
            print()
            print_board(game.board, game.current_player, selectedCell, winning_cells)
            exit()
    elif key == Key.right:
        print(" Right key pressed")
        if selectedCell["x"] < grid_size-1:
            selectedCell["x"] += 1
            print_board(game.board, game.current_player, selectedCell)
    elif key == Key.left:
        print(" Left key pressed")
        if selectedCell["x"] > 0:
            selectedCell["x"] -= 1
            print_board(game.board, game.current_player, selectedCell)
    elif key == Key.up:
        print(" Up key pressed")
        if selectedCell["y"] > 0:   
            selectedCell["y"] -= 1
            print_board(game.board, game.current_player, selectedCell)
    elif key == Key.down:
        print(" Down key pressed")
        if selectedCell["y"] < grid_size-1:
            selectedCell["y"] += 1
            print_board(game.board, game.current_player, selectedCell)
    elif key == Key.esc:
        exit()

    elif key in [Key.up, Key.down, Key.left, Key.right]:
        pass

with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()