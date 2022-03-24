from tennis_scoring.game import start, Score

def test_start():
    assert start() == {'player1': Score.LOVE, 'player2': Score.LOVE}
