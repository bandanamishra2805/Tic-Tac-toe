import tictactoe

def test_winner_row():
    board = ["X","X","X"," "," "," "," "," "," "]
    assert tictactoe.winner(board) == "X"

def test_full_board_draw():
    board = ["X","O","X","X","O","O","O","X","X"]
    assert tictactoe.winner(board) is None
    assert tictactoe.is_full(board) is True
