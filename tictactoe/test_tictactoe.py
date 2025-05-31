from tictactoe import *

def test_player_turn():
    board = [[X, O, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert player(board) == X
    print("Test passed: player turn logic is correct.")

test_player_turn()
