from tennis_scoring.game import (award_point, start, score, Player, Score)

def test_non_tied_game():
    game = start()
    while not game['winner']:
        scorer = Player.ONE
        game = award_point(game, scorer)
    assert game['winner'] == Player.ONE
