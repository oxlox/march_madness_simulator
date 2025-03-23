import random
from definitions import ROOT_DIR

positions = ["PG", "SG", "SF", "PF", "C"]


class Player:
    def __init__(self, team_id):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.position = self.generate_position()
        self.year = self.generate_year()
        self.team_id = team_id
        self.starter = False

    def generate_first_name(self):
        with open(f"{ROOT_DIR}/data/male_first_names.txt", "r") as name_file:
            random_int = random.randint(0, 502)
            for i, line in enumerate(name_file):
                if i == random_int:
                    return str.strip(line)

    def generate_last_name(self):
        with open(f"{ROOT_DIR}/data/surnames.txt", "r") as name_file:
            random_int = random.randint(0, 1001)
            for i, line in enumerate(name_file):
                if i == random_int:
                    return str.strip(line)

    def generate_position(self):
        return positions[random.randint(0, len(positions) - 1)]

    def generate_year(self):
        return random.randint(1, 5)

    def set_starter(self):
        self.starter = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
