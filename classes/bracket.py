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
