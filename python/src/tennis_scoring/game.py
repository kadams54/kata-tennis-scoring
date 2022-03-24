from enum import Enum

class Score(Enum):
    LOVE = 0
    FIFTEEN = 15
    THIRTY = 30
    FOURTY = 40


class Player(Enum):
    ONE = 'Player 1'
    TWO = 'Player 2'

def start():
    return {Player.ONE: Score.LOVE, Player.TWO: Score.LOVE, 'winner': None}
