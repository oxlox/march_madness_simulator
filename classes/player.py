import random

positions = set("PG", "PG/SG", "SG", "SG/SF", "SG", "SG/PF", "PF", "PF/C", "C")


class Player:
    def __init__(self):
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
        self.position = self.generate_position()
        self.year = self.generate_year()

    def generate_first_name():
        return ""

    def generate_last_name():
        return ""

    def generate_position():
        return positions[random.randint(0, len(positions) - 1)]

    def generate_year():
        return random.randint(1, 5)
