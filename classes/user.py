import json
from classes.team import Team
from classes.matchup import Matchup
from utilities.text_output import output
from definitions import ROOT_DIR


class User:
    def enter_bracket(self, bracket):
        with open(
            f"{ROOT_DIR}/save_data/player_bracket.json", "w"
        ) as bracket_file:
            predictions = {}
            predictions["round_1"] = {}
            predictions["round_1"]["WEST"] = []
            predictions["round_1"]["PRAIRIE"] = []
            predictions["round_1"]["SOUTH"] = []
            predictions["round_1"]["NORTHEAST"] = []
            predictions["round_2"] = {}
            predictions["round_2"]["WEST"] = []
            predictions["round_2"]["PRAIRIE"] = []
            predictions["round_2"]["SOUTH"] = []
            predictions["round_2"]["NORTHEAST"] = []
            predictions["round_3"] = {}
            predictions["round_3"]["WEST"] = []
            predictions["round_3"]["PRAIRIE"] = []
            predictions["round_3"]["SOUTH"] = []
            predictions["round_3"]["NORTHEAST"] = []
            predictions["round_4"] = []
            predictions["round_5"] = []
            predictions["round_6"] = []
            output("ROUND OF 64")
            round_1_matchups = bracket.get_round_1_matchups()
            for conference, matchups in round_1_matchups.items():
                output(conference)
                for matchup in matchups:
                    input_accepted = False
                    while not input_accepted:
                        output(f"{matchup.pre_game_str()}")
                        answer = input()
                        if answer in matchup.team1.get_conference_team_aliases():
                            predictions["round_1"][conference].append(matchup.team1.team_id)
                            input_accepted = True
                        elif answer in matchup.team2.get_conference_team_aliases():
                            predictions["round_1"][conference].append(matchup.team2.team_id)
                            input_accepted = True
                        else:
                            output("Having trouble? Try just typing the school name.")
            output("ROUND OF 32")
            for conference_name, matchups in predictions["round_1"].items():
                conference = bracket.get_conference(conference_name)
                output(conference.name)
                for i in range(0, len(matchups), 2):
                    team1 = conference.get_team(matchups[i])
                    team2 = conference.get_team(matchups[i+1])
                    matchup = Matchup(team1, team2)
                    input_accepted = False
                    while not input_accepted:
                        output(f"{matchup.pre_game_str()}")
                        answer = input()
                        if answer in matchup.team1.get_conference_team_aliases():
                            predictions["round_2"][conference.name].append(matchup.team1.team_id)
                            input_accepted = True
                        elif answer in matchup.team2.get_conference_team_aliases():
                            predictions["round_2"][conference.name].append(matchup.team2.team_id)
                            input_accepted = True
                        else:
                            output("Having trouble? Try just typing the school name.")
            output("SWEET 16")
            for conference_name, matchups in predictions["round_2"].items():
                conference = bracket.get_conference(conference_name)
                output(conference.name)
                for i in range(0, len(matchups), 2):
                    team1 = conference.get_team(matchups[i])
                    team2 = conference.get_team(matchups[i+1])
                    matchup = Matchup(team1, team2)
                    input_accepted = False
                    while not input_accepted:
                        output(f"{matchup.pre_game_str()}")
                        answer = input()
                        if answer in matchup.team1.get_conference_team_aliases():
                            predictions["round_3"][conference.name].append(matchup.team1.team_id)
                            input_accepted = True
                        elif answer in matchup.team2.get_conference_team_aliases():
                            predictions["round_3"][conference.name].append(matchup.team2.team_id)
                            input_accepted = True
                        else:
                            output("Having trouble? Try just typing the school name.")

            output("ELITE 8")
            round_4_matchups = bracket.get_round_4_matchups()
            for matchup in round_4_matchups:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        predictions["round_4"].append(matchup.team1.team_id)
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        predictions["round_4"].append(matchup.team2.team_id)
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("FINAL 4")
            round_5_matchups = bracket.get_round_5_matchups()
            for matchup in round_5_matchups:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        predictions["round_5"].append(matchup.team1.team_id)
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        predictions["round_5"].append(matchup.team2.team_id)
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("FINALS")
            matchup = bracket.get_round_6_matchups()
            input_accepted = False
            while not input_accepted:
                output(f"{matchup.pre_game_str()}")
                answer = input()
                if answer in matchup.team1.get_conference_team_aliases():
                    predictions["round_6"].append(matchup.team1.team_id)
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    predictions["round_6"].append(matchup.team2.team_id)
                    input_accepted = True
                else:
                    output("Having trouble? Try just typing the school name.")
            json.dump(predictions, bracket_file)
