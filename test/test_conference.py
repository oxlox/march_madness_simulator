from classes.conference import Conference, ConferenceName

def test_team_location_uniqueness():
    for i in range(0, 10):
        name = ConferenceName(1)
        conference = Conference(name)
        conference.initialize_teams()
        team_locations = []
        for team in conference.teams:
            team_locations.append(team.location)
        assert len(set(team_locations)) == 16
        
def test_build_conference_tree():
    name = ConferenceName(2)
    conference = Conference(name)
    conference.initialize_teams()
    conference.build_conference_tree()
    assert len(conference.matchup_tree) == 15