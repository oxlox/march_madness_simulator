from classes.bracket import Bracket


def main():
    simulate_tournament()


if __name__ == "__main__":
    main()


def simulate_tournament():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_bracket()
