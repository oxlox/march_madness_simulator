from classes.bracket import Bracket



def test_get_round_1_matchups():
    bracket = Bracket()
    bracket.build_matchups()
    matchups = bracket.get_round_1_matchups()
    assert len(matchups) == 4
