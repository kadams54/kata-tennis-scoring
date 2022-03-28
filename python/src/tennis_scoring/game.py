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
    player1_iterator = iter(Score)
    player2_iterator = iter(Score)
    return {
        Player.ONE: (next(player1_iterator), player1_iterator),
        Player.TWO: (next(player2_iterator), player2_iterator),
        'winner': None
    }

def score(game, player):
    (_, current_score_iter) = game[player]
    return next(current_score_iter)
