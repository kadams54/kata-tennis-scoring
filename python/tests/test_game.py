from tennis_scoring.game import start, Score, Player

def test_start():
    assert start() == {
        Player.ONE: Score.LOVE, Player.TWO: Score.LOVE, 'winner': None}
