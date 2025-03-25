from classes.matchup import Matchup
from classes.team import Team


def test_matchup_simulation_score():
    team1 = Team("location", "test", 1, 1)
    team2 = Team("Otherloc", "test2", 2, 2)
    matchup = Matchup(team1, team2)
    matchup.simulate_game()
    if matchup.winner == team1:
        assert matchup.score_team1 > matchup.score_team2
    else:
        assert matchup.score_team2 > matchup.score_team1
