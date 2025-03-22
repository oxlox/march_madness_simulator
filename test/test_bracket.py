from classes.bracket import Bracket


def test_initialize_teams():
    bracket = Bracket()
    assert len(bracket.teams) == 64


def test_bracket_location_uniqueness():
    bracket = Bracket()
    locations = set()
    for team in bracket.teams:
        locations.add(team.location)
    assert len(locations) == 64
