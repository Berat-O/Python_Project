import copy
from math import inf

X = "X"
O = "O"
EMPTY = None

class TicTacToe:
    def __init__(self):
        """
        Initialize the Tic-Tac-Toe game board and set up initial conditions.
        """
        self.board = self.initial_state()

    def initial_state(self):
        """
        Returns the starting state of the board.
        """
        return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    def current_player(self):
        """
        Returns the player who has the next turn on the board.
        """
        x_count = sum(row.count(X) for row in self.board)
        o_count = sum(row.count(O) for row in self.board)
        return X if x_count <= o_count else O

    def available_actions(self):
        """
        Returns a set of all possible actions (i, j) available on the board.
        """
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == EMPTY]

    def apply_action(self, action):
        """
        Returns a new board after applying the given action (i, j).
        """
        i, j = action
        new_board = copy.deepcopy(self.board)
        if new_board[i][j] == EMPTY:
            new_board[i][j] = self.current_player()
            return new_board
        else:
            raise ValueError("Invalid action")

    def check_winner(self):
        """
        Returns the winner of the game, if there is one.
        """
        # Check rows, columns, and diagonals
        lines = (
            self.board +  # Rows
            [list(col) for col in zip(*self.board)] +  # Columns
            [[self.board[i][i] for i in range(3)]] +  # Main diagonal
            [[self.board[i][2 - i] for i in range(3)]]  # Anti-diagonal
        )

        for line in lines:
            if line[0] == line[1] == line[2] and line[0] is not None:
                return line[0]
        return None

    def is_terminal(self):
        """
        Returns True if the game is over (either a win or a tie), False otherwise.
        """
        return self.check_winner() is not None or all(
            cell != EMPTY for row in self.board for cell in row
        )

    def utility(self):
        """
        Returns 1 if X wins, -1 if O wins, 0 otherwise.
        """
        winner = self.check_winner()
        if winner == X:
            return 1
        elif winner == O:
            return -1
        else:
            return 0

    def minimax(self):
        """
        Returns the optimal move for the current player using the minimax algorithm.
        """
        if self.is_terminal():
            return None

        current = self.current_player()

        if current == X:
            best_value = -inf
            best_move = None
            for action in self.available_actions():
                new_board = TicTacToe()
                new_board.board = self.apply_action(action)
                value = new_board.min_value()
                if value > best_value:
                    best_value = value
                    best_move = action
            return best_move

        else:
            best_value = inf
            best_move = None
            for action in self.available_actions():
                new_board = TicTacToe()
                new_board.board = self.apply_action(action)
                value = new_board.max_value()
                if value < best_value:
                    best_value = value
                    best_move = action
            return best_move

    def max_value(self):
        """
        Returns the maximum value for the minimax algorithm.
        """
        if self.is_terminal():
            return self.utility()

        value = -inf
        for action in self.available_actions():
            new_board = TicTacToe()
            new_board.board = self.apply_action(action)
            value = max(value, new_board.min_value())
        return value

    def min_value(self):
        """
        Returns the minimum value for the minimax algorithm.
        """
        if self.is_terminal():
            return self.utility()

        value = inf
        for action in self.available_actions():
            new_board = TicTacToe()
            new_board.board = self.apply_action(action)
            value = min(value, new_board.max_value())
        return value

# Example usage
if __name__ == "__main__":
    game = TicTacToe()
    
    while not game.is_terminal():
        if game.current_player() == X:
            move = game.minimax()
            if move:
                game.board = game.apply_action(move)
        else:
            # Simulate O's move (could be replaced with user input)
            move = game.minimax()
            if move:
                game.board = game.apply_action(move)

        for row in game.board:
            print(row)
        print()

    winner = game.check_winner()
    if winner:
        print(f"The winner is {winner}")
    else:
        print("It's a tie!")
