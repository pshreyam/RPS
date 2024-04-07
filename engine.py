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


def play(user_move: str) -> Tuple[str, str]:
    available_moves = [Move.ROCK, Move.SCISSORS, Move.PAPER]
    computer_move = random.choice(available_moves)

    if user_move == computer_move:
        return Result.TIE, computer_move

    result = Result.LOSS

    if (
        (user_move == Move.ROCK and computer_move == Move.SCISSORS) or
        (user_move == Move.PAPER and computer_move == Move.ROCK) or
        (user_move == Move.SCISSORS and computer_move == Move.PAPER)
    ):
        result = Result.WIN

    return result, computer_move
