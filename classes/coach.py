import random
from definitions import ROOT_DIR


class Coach:
    def __init__(self, team_id):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.team_id = team_id

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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"