from classes.conference import Conference, ConferenceName


class Bracket:
    def __init__(self):
        self.conferences = self.initialize_conferences()

    def initialize_conferences(self):
        conferences = []
        for conference_name in ConferenceName:
            new_conference = Conference(conference_name)
            conferences.append(new_conference)

        return conferences

    def build_matchups(self):
        for conference in self.conferences:
            conference.build_conference_tree()

    def simulate_conferences(self):
        for conference in self.conferences:
            conference.simulate_conference()

    def print_bracket(self):
        for conference in self.conferences:
            print(f"=== {conference.name} ===")
            conference.print_matchup_tree()
