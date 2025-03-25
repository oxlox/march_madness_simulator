from classes.team import Team


def test_roster_size():
    team = Team("location", "test", 1, 1)
    assert len(team.players) == 12


def test_num_starters():
    team = Team("location", "test", 1, 1)
    team.set_starters()
    assert len(team.starters) == 5

