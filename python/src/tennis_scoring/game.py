from enum import Enum

class Player(Enum):
    ONE = 1
    TWO = 2

class Score(Enum):
    LOVE = 0
    FIFTEEN = 15
    THIRTY = 30
    FOURTY = 40
    WINNER = 100

def start():
    return {
        Player.ONE: Score.LOVE,
        Player.TWO: Score.LOVE,
        'winner': None
    }

def award_point(game, player):
    new_score = score(game[player])
    winner = player if new_score == Score.WINNER else None
    return {**game, **{player: new_score, 'winner': winner}}

def score(current_score):
    scores = list(Score)
    return scores[scores.index(current_score) + 1]
