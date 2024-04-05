from tic_tac_toe.game import TicTacToe

def test_initialization():
    game = TicTacToe(2, ['Player 1', 'Player 2'], 5)
    assert game.num_players == 2
    assert game.player_names == ['Player 1', 'Player 2']
    assert game.grid_size == 5
    assert len(game.board) == 5
    for row in game.board:
        assert len(row) == 5
        assert all(cell == ' ' for cell in row)
    assert len(game.player_symbols) == 2
    assert all(player in game.player_symbols for player in ['Player 1', 'Player 2'])
    assert all(symbol in TicTacToe.SYMBOLS for symbol in game.player_symbols.values())


def test_valid_grid_size():
    # Test with valid grid size (5)
    game = TicTacToe(2, ['Player 1', 'Player 2'], 5)
    assert game.grid_size == 5

    # Test with valid grid size (25)
    game = TicTacToe(2, ['Player 1', 'Player 2'], 25)
    assert game.grid_size == 25

def test_invalid_grid_size():
    # Test with invalid grid size (less than 5)
    try:
        game = TicTacToe(2, ['Player 1', 'Player 2'], 4)
    except ValueError as e:
        assert str(e) == "Grid size must be between 5 and 25."

    # Test with invalid grid size (greater than 25)
    try:
        game = TicTacToe(2, ['Player 1', 'Player 2'], 26)
    except ValueError as e:
        assert str(e) == "Grid size must be between 5 and 25."

def test_valid_num_players():
    # Test with valid number of players (2)
    game = TicTacToe(2, ['Player 1', 'Player 2'], 5)
    assert game.num_players == 2

    # Test with valid number of players (3)
    game = TicTacToe(3, ['Player 1', 'Player 2', 'Player 3'], 5)
    assert game.num_players == 3

    # Test with valid number of players (4)
    game = TicTacToe(4, ['Player 1', 'Player 2', 'Player 3', 'Player 4'], 5)
    assert game.num_players == 4

def test_invalid_num_players():
    # Test with invalid number of players (less than 2)
    try:
        game = TicTacToe(1, ['Player 1'], 5)
    except ValueError as e:
        assert str(e) == "Number of players must be between 2 and 4."

    # Test with invalid number of players (more than 4)
    try:
        game = TicTacToe(5, ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5'], 5)
    except ValueError as e:
        assert str(e) == "Number of players must be between 2 and 4."

# Add more test cases as needed
