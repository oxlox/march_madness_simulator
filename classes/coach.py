class Coach:
    def __init__(self, team_id):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.team_id = team_id

    def generate_first_name(self):
        return ""

    def generate_last_name(self):
        return ""
