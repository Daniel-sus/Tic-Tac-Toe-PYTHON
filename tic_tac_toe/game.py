import random


class TicTacToe:
    SYMBOLS = ['#', '@', '$', '%']

    def __init__(self, num_players, player_names, grid_size):
        self.validate_num_players(num_players)
        self.validate_grid_size(grid_size)
        self.num_players = num_players
        self.player_names = player_names
        self.grid_size = grid_size
        self.board = self.create_board(grid_size)
        self.player_symbols = self.assign_symbols()
        self.current_player_index = 0
        self.current_player = self.player_names[self.current_player_index]

    def validate_num_players(self, num_players):
        if not 2 <= num_players <= 4:
            raise ValueError("Number of players must be between 2 and 4.")

    def validate_grid_size(self, grid_size):
        if not 5 <= grid_size <= 25:
            raise ValueError("Grid size must be between 5 and 25.")

    def create_board(self, grid_size):
        return [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    def assign_symbols(self):
        symbols = random.sample(self.SYMBOLS, self.num_players)
        return {player: symbol for player, symbol in zip(self.player_names, symbols)}

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.player_symbols[self.current_player]
            if self.check_winner(row, col):
                return 'win', self.current_player
            elif self.check_board_full():
                return 'draw', None
            else:
                self.switch_player()
                return 'success', None
        else:
            return 'occupied', None

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        self.current_player = self.player_names[self.current_player_index]

    def check_winner(self, row, col):
        symbol = self.player_symbols[self.current_player]

        # Check horizontally
        if all(self.board[row][c] == symbol for c in range(self.grid_size)):
            return True

        # Check vertically
        if all(self.board[r][col] == symbol for r in range(self.grid_size)):
            return True

        # Check diagonally (top-left to bottom-right)
        if all(self.board[i][i] == symbol for i in range(self.grid_size)):
            return True

        # Check diagonally (top-right to bottom-left)
        if all(self.board[i][self.grid_size - 1 - i] == symbol for i in range(self.grid_size)):
            return True

        return False

    def check_board_full(self):
        return all(self.board[row][col] != ' ' for row in range(self.grid_size) for col in range(self.grid_size))
