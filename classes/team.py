class Team:
    def __init__(self, school_location, school_team_name):
        self.location = school_location
        self.name = school_team_name

    def __str__(self):
        return f"{self.location} {self.name}"
