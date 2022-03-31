from tennis_scoring.game import (Player, Score, score, start)

def test_start():
    game = start()
    assert game[Player.ONE] == Score.LOVE
    assert game[Player.TWO] == Score.LOVE
    assert game['winner'] == None

def test_score():
    game = start()
    current_score = game[Player.ONE]
    new_score = score(current_score)
    assert new_score.value > current_score.value
