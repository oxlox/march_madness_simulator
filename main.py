from classes import team


def main():
    teams = team.initialize_teams()
    for new_team in teams:
        print(new_team)


if __name__ == "__main__":
    main()
