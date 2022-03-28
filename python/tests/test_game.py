from tennis_scoring.game import (Player, Score, score, start)

def test_start():
    assert start() == {
        Player.ONE: (Score.LOVE, iter(Score)),
        Player.TWO: (Score.LOVE, iter(Score)),
        'winner': None
    }

def test_score():
    game = start()
    (old_score, _) = game[Player.ONE]
    new_score = score(game, Player.ONE)
    assert new_score > old_score
