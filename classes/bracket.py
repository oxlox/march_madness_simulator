import logging
import random
from classes import team
from definitions import ROOT_DIR

logger = logging.getLogger(__name__)


class Bracket:
    def __init__(self):
        self.teams = self.initialize_teams()

    def initialize_teams(self):
        # Create all teams at once, so that school locations don't get re-used.
        # Team mascost/names can be re-used, as happens irl
        teams_in_tournament = []
        available_schools = []
        available_names = []
        with open(
            f"{ROOT_DIR}/data/school_location_names.txt", "r"
        ) as team_location_file:
            for line in team_location_file:
                available_schools.append(line)
        with open(f"{ROOT_DIR}/data/school_team_names.txt", "r") as team_name_file:
            for line in team_name_file:
                available_names.append(line)

        for i in range(0, 64):
            location_index = random.randint(0, len(available_schools) - 1)
            location = available_schools.pop(location_index)
            location = str.strip(location)
            team_name = available_names[random.randint(0, len(available_names) - 1)]
            team_name = str.strip(team_name)
            new_team = team.Team(location, team_name)
            teams_in_tournament.append(new_team)

        return teams_in_tournament
