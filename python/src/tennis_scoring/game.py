from enum import Enum

class Player(Enum):
    ONE = 1
    TWO = 2

class Score(Enum):
    LOVE = 0
    FIFTEEN = 15
    THIRTY = 30
    FOURTY = 40

def start():
    return {
        Player.ONE: Score.LOVE,
        Player.TWO: Score.LOVE,
        'winner': None
    }

def score(current_score):
    scores = list(Score)
    return scores[scores.index(current_score) + 1]
