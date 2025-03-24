from classes.bracket import Bracket


def test_get_round_1_matchups():
    bracket = Bracket()
    bracket.build_matchups()
    matchups = bracket.get_round_1_matchups()
    assert len(matchups) == 4


def test_get_round_2_matchups():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_bracket()
    matchups = bracket.get_round_2_matchups()
    assert len(matchups) == 4


def test_get_round_3_matchups():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_bracket()
    matchups = bracket.get_round_3_matchups()
    assert len(matchups) == 4


def test_get_round_4_matchups():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_bracket()
    matchups = bracket.get_round_4_matchups()
    assert len(matchups) == 4
