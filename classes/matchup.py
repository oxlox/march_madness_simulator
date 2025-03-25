import random
from math import ceil


class Matchup:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.winner = None
        self.score_team1 = None
        self.score_team2 = None

    def simulate_game(self):
        team_1_prob = 1 / (self.team1.seed + 1) * 100
        team_2_prob = 1 / (self.team2.seed + 1) * 100
        prob_total = team_1_prob + team_2_prob
        result = random.randint(0, ceil(prob_total))
        if result < team_1_prob:
            self.winner = self.team1
            self.score_team1 = random.randint(45, 100)
            self.score_team2 = random.randint(40, self.score_team1 - 1)
        else:
            self.winner = self.team2
            self.score_team2 = random.randint(45, 100)
            self.score_team1 = random.randint(40, self.score_team2 - 1)

    def pre_game_str(self):
        return f"{self.team1} vs {self.team2}"

    def __str__(self):
        return f"{self.team1}: {self.score_team1} vs {self.team2}: {self.score_team2}"
