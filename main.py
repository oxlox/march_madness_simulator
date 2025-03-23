from classes.bracket import Bracket


def main():
    bracket = Bracket()
    for conference in bracket.conferences:
        for team in conference.teams:
            print(team.coach)


if __name__ == "__main__":
    main()
