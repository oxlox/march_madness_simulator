import random
from classes.team import Team
from classes.matchup import Matchup
from definitions import ROOT_DIR
from enum import Enum
from math import floor


class ConferenceName(Enum):
    WEST = 1
    PRAIRIE = 2
    NORTHEAST = 3
    SOUTH = 4


class Conference:
    def __init__(self, conference_name):
        self.conference_id = conference_name.value
        self.name = conference_name.name
        self.teams = self.initialize_teams()
        self.matchup_tree = []

    def print_teams(self):
        print(f"=== {self.name} ===")
        for conference_team in self.teams:
            print(f"{conference_team}")

    def initialize_teams(self):
        # Create all teams at once, so that school locations don't get re-used.
        # Team mascost/names can be re-used, as happens irl
        teams_in_conference = []
        available_schools = []
        available_names = []
        with open(
            f"{ROOT_DIR}/data/conference_location_names_{self.name}.txt", "r"
        ) as team_location_file:
            for line in team_location_file:
                available_schools.append(line)
        with open(f"{ROOT_DIR}/data/school_team_names.txt", "r") as team_name_file:
            for line in team_name_file:
                available_names.append(line)

        for i in range(0, 16):
            location_index = random.randint(0, len(available_schools) - 1)
            location = available_schools.pop(location_index)
            location = str.strip(location)
            team_name = available_names[random.randint(0, len(available_names) - 1)]
            team_name = str.strip(team_name)
            new_team = Team(location, team_name, i + 1, (i + 1) * self.conference_id)
            new_team.set_starters()
            teams_in_conference.append(new_team)

        return teams_in_conference

    def build_conference_tree(self):
        # first, create the first round matchups
        for i in range(0, floor(len(self.teams) / 2)):
            new_matchup = Matchup(self.teams[i], self.teams[len(self.teams) - (i + 1)])
            new_matchup.simulate_game()
            self.matchup_tree.append(new_matchup)

        for i in range(0, 8, 2):
            new_matchup = Matchup(
                self.matchup_tree[i].winner,
                self.matchup_tree[len(self.matchup_tree) - (i + 1)].winner,
            )
            new_matchup.simulate_game()
            self.matchup_tree.append(new_matchup)

        for i in range(8, len(self.matchup_tree) - 1, 2):
            new_matchup = Matchup(
                self.matchup_tree[i].winner,
                self.matchup_tree[len(self.matchup_tree) - (i + 1)].winner,
            )
            new_matchup.simulate_game()
            self.matchup_tree.append(new_matchup)

        new_matchup = Matchup(
            self.matchup_tree[-2].winner, self.matchup_tree[-1].winner
        )
        new_matchup.simulate_game()
        self.matchup_tree.append(new_matchup)

    def simulate_conference(self):
        for matchup in self.matchup_tree:
            matchup.simulate_game()

    def print_matchup_tree(self):
        for matchup in self.matchup_tree:
            if self.matchup_tree.index(matchup) == 8:
                print("Round of 32")
            elif self.matchup_tree.index(matchup) == 12:
                print("Sweet 16")
            elif self.matchup_tree.index(matchup) == 14:
                print("Round of 8")
            elif self.matchup_tree.index(matchup) == 15:
                print("Final 4")
            print(matchup)
