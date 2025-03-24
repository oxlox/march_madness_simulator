from classes.coach import Coach
from classes.player import Player


class Team:
    def __init__(self, school_location, school_team_name, seed=1, team_id=1):
        self.team_id = team_id
        self.location = school_location
        self.name = school_team_name
        self.seed = seed
        self.players = self.generate_players()
        self.coach = self.generate_coach()
        self.starters = []

    def __str__(self):
        return f"{self.seed} - {self.location} {self.name}"

    def generate_players(self):
        players = []
        for i in range(0, 12):
            new_player = Player(self.team_id)
            players.append(new_player)
        return players

    def generate_coach(self):
        new_coach = Coach(self.team_id)
        return new_coach

    def set_starters(self):
        starter_positions_filled = []
        for player in self.players:
            if player.position not in starter_positions_filled:
                player.set_starter()
                starter_positions_filled.append(player.position)
                self.starters.append(player)

            if len(starter_positions_filled) == 5:
                break
        while len(starter_positions_filled) < 5:
            for player in self.players:
                if player not in self.starters:
                    starter_positions_filled.append(player.position)
                    self.starters.append(player)
