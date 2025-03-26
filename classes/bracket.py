from classes.conference import Conference, ConferenceName
from classes.matchup import Matchup


class Bracket:
    def __init__(self):
        self.conferences = self.initialize_conferences()
        self.matchup_tree = []

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
        print("=== ROUND OF 4 ===")
        print(self.matchup_tree[0])
        print(self.matchup_tree[1])
        print("--- FINALS ---")
        print(self.matchup_tree[2])

    def simulate_bracket(self):
        self.simulate_conferences()
        conference_winners = []
        for conference in self.conferences:
            conference_winners.append(conference.matchup_tree[-1].winner)

        semifinal_1 = Matchup(conference_winners[0], conference_winners[2])
        semifinal_1.simulate_game()
        semifinal_2 = Matchup(conference_winners[1], conference_winners[3])
        semifinal_2.simulate_game()
        self.matchup_tree.append(semifinal_1)
        self.matchup_tree.append(semifinal_2)
        finals = Matchup(semifinal_1.winner, semifinal_2.winner)
        finals.simulate_game()
        self.matchup_tree.append(finals)

    def get_round_1_matchups(self):
        matchups = {}
        for conference in self.conferences:
            matchups[conference.name] = conference.matchup_tree[0:8]
        return matchups

    def get_round_2_matchups(self):
        matchups = {}
        for conference in self.conferences:
            matchups[conference.name] = conference.matchup_tree[8:12]
        return matchups

    def get_round_3_matchups(self):
        matchups = {}
        for conference in self.conferences:
            matchups[conference.name] = conference.matchup_tree[12:14]
        return matchups

    def get_round_4_matchups(self):
        matchups = []
        for conference in self.conferences:
            matchups.append(conference.matchup_tree[14])
        return matchups

    def get_round_5_matchups(self):
        return [self.matchup_tree[-3], self.matchup_tree[-2]]

    def get_round_6_matchups(self):
        return self.matchup_tree[-1]
