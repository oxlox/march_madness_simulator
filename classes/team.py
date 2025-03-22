import random
from definitions import ROOT_PATH

def initialize_teams():
    # Create all teams at once, so that school locations don't get re-used.
    # Team mascost/names can be re-used, as happens irl
    teams_in_tournament = []
    available_schools = []
    available_names = []
    with open(f"{ROOT_PATH}/data/school_location_names.txt", "r") as team_location_file:
        for line in team_location_file:
            available_schools.append(line)
    with open(f"{ROOT_PATH}/data/school_team_names.txt", "r") as team_name_file:
        for line in team_name_file:
            available_names.append(line)

    for i in range(0,64):
        location_index = random.randint(0,len(available_schools)-1)
        location = available_schools.pop(location_index)
        team_name = available_names[random.randint(0, len(available_names)-1)]
        new_team = Team(location, team_name)
        teams_in_tournament.append(new_team)



class Team:
    def __init__(self, school_location, school_team_name):
        location = school_location
        name = school_team_name
    
    def __str__(self):
        return f"{self.location} {self.name}"
    


