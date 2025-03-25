from classes.bracket import Bracket
from classes.user import User


def simulate_tournament():
    bracket = Bracket()
    bracket.build_matchups()
    bracket.simulate_bracket()
    return bracket


def main():
    bracket = simulate_tournament()
    user = User()
    user.enter_bracket(bracket)


if __name__ == "__main__":
    main()
