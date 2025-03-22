from classes import team


def test_initialize_teams():
    assert len(team.initialize_teams()) == 64
