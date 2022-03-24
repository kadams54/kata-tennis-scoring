from enum import Enum

class Score(Enum):
    LOVE = 0
    FIFTEEN = 15
    THIRTY = 30
    FOURTY = 40

def start():
    return {'player1': Score.LOVE, 'player2': Score.LOVE}
