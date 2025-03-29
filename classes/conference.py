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
    
    def get_team(self, team_id):
        if team_id < 1:
            return None
        if team_id > 64:
            return None
        for team in self.teams:
            if team.team_id == team_id:
                return team
        return None

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

    def sort_bracket(self):
        sorted_teams = [None] * 16
        for i in range(0, len(self.teams)):
            if i == 0:
                sorted_teams[0] = self.teams[i]
            elif i == 1:
                sorted_teams[15] = self.teams[i]
            elif i == 2:
                sorted_teams[8] = self.teams[i]
            elif i == 3:
                sorted_teams[6] = self.teams[i]
            elif i == 4:
                sorted_teams[4] = self.teams[i]
            elif i == 5:
                sorted_teams[10] = self.teams[i]
            elif i == 6:
                sorted_teams[12] = self.teams[i]
            elif i == 7:
                sorted_teams[2] = self.teams[i]
            elif i == 8:
                sorted_teams[13] = self.teams[i]
            elif i == 9:
                sorted_teams[3] = self.teams[i]
            elif i == 10:
                sorted_teams[11] = self.teams[i]
            elif i == 11:
                sorted_teams[5] = self.teams[i]
            elif i == 12:
                sorted_teams[7] = self.teams[i]
            elif i == 13:
                sorted_teams[9] = self.teams[i]
            elif i == 14:
                sorted_teams[14] = self.teams[i]
            else:
                sorted_teams[1] = self.teams[i]
        return sorted_teams


    def build_conference_tree(self):
        self.teams = self.sort_bracket()
        # first, create the first round matchups
        for i in range(0, 16, 2):
            new_matchup = Matchup(self.teams[i], self.teams[i + 1])
            new_matchup.simulate_game()
            self.matchup_tree.append(new_matchup)

        for i in range(0, 8, 2):
            new_matchup = Matchup(
                self.matchup_tree[i].winner,
                self.matchup_tree[i + 1].winner,
            )
            new_matchup.simulate_game()
            self.matchup_tree.append(new_matchup)

        for i in range(8, len(self.matchup_tree) - 1, 2):
            new_matchup = Matchup(
                self.matchup_tree[i].winner,
                self.matchup_tree[i + 1].winner,
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
