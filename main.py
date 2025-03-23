from classes.bracket import Bracket


def main():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_conferences()
    bracket.print_bracket()


if __name__ == "__main__":
    main()
