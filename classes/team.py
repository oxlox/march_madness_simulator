class Team:
    def __init__(self, school_location, school_team_name, seed=1):
        self.location = school_location
        self.name = school_team_name
        self.seed = seed

    def __str__(self):
        return f"{self.location} {self.name}"
