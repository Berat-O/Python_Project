import tictactoe

def print_board(board):
    """
    Prints the board in a human-readable format.
    """
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell if cell is not None else " ", end=" | ")
        print("\n" + "-" * 13)


def get_human_move(board):
    """
    Prompts user to input a valid move.
    """
    while True:
        try:
            print("Enter row and column num")
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if (row, col) in tictactoe.actions(board):
                return (row, col)
            else:
                print("Invalid move. Try again.\n")
        except ValueError:
            print("Please enter valid integers.\n")


def main():
    board = tictactoe.initial_state()
    human_player = input("Do you want to play as X or O? ").strip().upper()

    if human_player not in ["X", "O"]:
        print("Invalid choice. Defaulting to X.")
        human_player = "X"

    ai_player = tictactoe.O if human_player == tictactoe.X else tictactoe.X

    while not tictactoe.terminal(board):
        print_board(board)
        current = tictactoe.player(board)

        if current == human_player:
            print(f"Your turn ({human_player})")
            move = get_human_move(board)
        else:
            print(f"AI is thinking... ({ai_player})")
            move = tictactoe.minimax(board)

        board = tictactoe.result(board, move)

    # Final board and result
    print_board(board)
    win = tictactoe.winner(board)
    if win is None:
        print("It's a draw!")
    elif win == human_player:
        print("You win!")
    else:
        print("AI wins!")


if __name__ == "__main__":
    main()
