import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """Returns the starting state of the board."""
    return [[EMPTY, EMPTY, EMPTY] for _ in range(3)]


def player(board):
    """Returns the player who has the next turn on the board."""
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """Returns a list of all possible actions (i, j) available on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY]


def result(board, action):
    """Returns the board that results from making move (i, j) on the board."""
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")
    
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """Returns the winner of the game, if there is one."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != EMPTY:
        return board[2][0]

    return None


def terminal(board):
    """Returns True if the game is over, False otherwise."""
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """Returns 1 if X has won, -1 if O has won, 0 otherwise."""
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0


def minimax(board):
    """Returns the optimal move for the current player on the board."""
    if terminal(board):
        return None

    if player(board) == X:
        return max_move(board)
    else:
        return min_move(board)


def max_move(board):
    """Finds the best move for player X."""
    best_value = -float('inf')
    best_action = None
    for action in actions(board):
        value = min_value(result(board, action))
        if value > best_value:
            best_value = value
            best_action = action
    return best_action


def min_move(board):
    """Finds the best move for player O."""
    best_value = float('inf')
    best_action = None
    for action in actions(board):
        value = max_value(result(board, action))
        if value < best_value:
            best_value = value
            best_action = action
    return best_action


def max_value(board):
    """Returns the maximum value (for X) of a move."""
    if terminal(board):
        return utility(board)
    value = -float('inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    """Returns the minimum value (for O) of a move."""
    if terminal(board):
        return utility(board)
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


if __name__ == "__main__":
    board = initial_state()
    while not terminal(board):
        move = minimax(board)
        board = result(board, move)
        print(f"Player {player(board)} made move: {move}")
        for row in board:
            print(row)
