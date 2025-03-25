from classes.conference import Conference, ConferenceName

def test_team_location_uniqueness():
    name = ConferenceName(1)
    conference = Conference(name)
    conference.initialize_teams()
    team_locations = []
    for team in conference.teams:
        team_locations.append(team.location)
    assert len(set(team_locations)) == 16