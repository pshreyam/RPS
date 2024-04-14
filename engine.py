import random
from enum import Enum
from typing import Tuple


class Move(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Result(str, Enum):
    WIN = "User Won."
    LOSS = "User Lost."
    TIE = "Tie."


AVAILABLE_MOVES = [Move.ROCK, Move.SCISSORS, Move.PAPER]


def generate_computer_move() -> Move:
    computer_move = random.choice(AVAILABLE_MOVES)
    return computer_move


def compute_result(user_move: Move, computer_move: Move):
    if user_move == computer_move:
        return Result.TIE

    if (
        (user_move == Move.ROCK and computer_move == Move.SCISSORS) or
        (user_move == Move.PAPER and computer_move == Move.ROCK) or
        (user_move == Move.SCISSORS and computer_move == Move.PAPER)
    ):
        return Result.WIN

    return Result.LOSS


def play(user_move: str) -> Tuple[str, str]:
    computer_move = generate_computer_move()
    result = compute_result(user_move=user_move, computer_move=computer_move)
    return result, computer_move
