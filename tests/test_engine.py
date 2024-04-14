from engine import generate_computer_move, AVAILABLE_MOVES, compute_result, Move, Result


def test_generate_computer_move():
    computer_move = generate_computer_move()
    assert computer_move in AVAILABLE_MOVES


def test_compute_result():
    assert compute_result(user_move=Move.ROCK, computer_move=Move.ROCK) == Result.TIE
    assert compute_result(user_move=Move.ROCK, computer_move=Move.PAPER) == Result.LOSS
    assert compute_result(user_move=Move.ROCK, computer_move=Move.SCISSORS) == Result.WIN

    assert compute_result(user_move=Move.PAPER, computer_move=Move.ROCK) == Result.LOSS
    assert compute_result(user_move=Move.PAPER, computer_move=Move.PAPER) == Result.TIE
    assert compute_result(user_move=Move.PAPER, computer_move=Move.SCISSORS) == Result.LOSS

    assert compute_result(user_move=Move.SCISSORS, computer_move=Move.ROCK) == Result.LOSS
    assert compute_result(user_move=Move.SCISSORS, computer_move=Move.PAPER) == Result.WIN
    assert compute_result(user_move=Move.SCISSORS, computer_move=Move.SCISSORS) == Result.TIE
