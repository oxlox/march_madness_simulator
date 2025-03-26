from classes.bracket import Bracket
from utilities.text_output import output
from definitions import ROOT_DIR


class User:
    def enter_bracket(self, bracket):
        with open(
            f"{ROOT_DIR}/save_data/player_bracket.csv", "w", encoding="utf-8"
        ) as bracket_file:
            lines = []
            output("ROUND OF 64")
            round_1_matchups = bracket.get_round_1_matchups()
            output("WEST CONFERENCE")
            for matchup in round_1_matchups["WEST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("PRAIRIE CONFERENCE")
            for matchup in round_1_matchups["PRAIRIE"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("SOUTH CONFERENCE")
            for matchup in round_1_matchups["SOUTH"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("NORTHEAST CONFERENCE")
            for matchup in round_1_matchups["NORTHEAST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("ROUND OF 32")
            round_2_matchups = bracket.get_round_2_matchups()
            output("WEST CONFERENCE")
            for matchup in round_2_matchups["WEST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("PRAIRIE CONFERENCE")
            for matchup in round_2_matchups["PRAIRIE"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("SOUTH CONFERENCE")
            for matchup in round_2_matchups["SOUTH"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("NORTHEAST CONFERENCE")
            for matchup in round_2_matchups["NORTHEAST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("SWEET 16")
            round_3_matchups = bracket.get_round_3_matchups()
            output("WEST CONFERENCE")
            for matchup in round_3_matchups["WEST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("PRAIRIE CONFERENCE")
            for matchup in round_3_matchups["PRAIRIE"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("SOUTH CONFERENCE")
            for matchup in round_3_matchups["SOUTH"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("NORTHEAST CONFERENCE")
            for matchup in round_3_matchups["NORTHEAST"]:
                input_accepted = False
                while not input_accepted:
                    output(f"{matchup.pre_game_str()}")
                    answer = input()
                    if answer in matchup.team1.get_conference_team_aliases():
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
                        input_accepted = True
                    else:
                        output("Having trouble? Try just typing the school name.")
            output("ELITE 8")
            round_4_matchups = bracket.get_round_4_matchups()
            output("WEST CONFERENCE")
            matchup = round_4_matchups["WEST"]
            input_accepted = False
            while not input_accepted:
                output(f"{matchup.pre_game_str()}")
                answer = input()
                if answer in matchup.team1.get_conference_team_aliases():
                    lines.append(f"{matchup.team1.team_id},")
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    lines.append(f"{matchup.team2.team_id},")
                    input_accepted = True
                else:
                    output("Having trouble? Try just typing the school name.")
            output("PRAIRIE CONFERENCE")
            matchup = round_4_matchups["PRAIRIE"]
            input_accepted = False
            while not input_accepted:
                output(f"{matchup.pre_game_str()}")
                answer = input()
                if answer in matchup.team1.get_conference_team_aliases():
                    lines.append(f"{matchup.team1.team_id},")
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    lines.append(f"{matchup.team2.team_id},")
                    input_accepted = True
                else:
                    output("Having trouble? Try just typing the school name.")
            output("SOUTH CONFERENCE")
            matchup = round_4_matchups["SOUTH"]
            input_accepted = False
            while not input_accepted:
                output(f"{matchup.pre_game_str()}")
                answer = input()
                if answer in matchup.team1.get_conference_team_aliases():
                    lines.append(f"{matchup.team1.team_id},")
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    lines.append(f"{matchup.team2.team_id},")
                    input_accepted = True
                else:
                    output("Having trouble? Try just typing the school name.")
            output("NORTHEAST CONFERENCE")
            matchup = round_4_matchups["NORTHEAST"]
            input_accepted = False
            while not input_accepted:
                output(f"{matchup.pre_game_str()}")
                answer = input()
                if answer in matchup.team1.get_conference_team_aliases():
                    lines.append(f"{matchup.team1.team_id},")
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    lines.append(f"{matchup.team2.team_id},")
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
                        lines.append(f"{matchup.team1.team_id},")
                        input_accepted = True
                    elif answer in matchup.team2.get_conference_team_aliases():
                        lines.append(f"{matchup.team2.team_id},")
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
                    lines.append(f"{matchup.team1.team_id},")
                    input_accepted = True
                elif answer in matchup.team2.get_conference_team_aliases():
                    lines.append(f"{matchup.team2.team_id},")
                    input_accepted = True
                else:
                    output("Having trouble? Try just typing the school name.")
            lines.append("\n")
            bracket_file.writelines(lines)
