import sys
import constants
import copy

teams_list = copy.deepcopy(constants.TEAMS)
players_list = copy.deepcopy(constants.PLAYERS)
not_experienced = []
is_experienced = []
panthers = []
bandits = []
warriors = []


def clean_data():
    for player in players_list:
        height = player["height"].split()
        player["height"] = int(height[0])
        player["guardians"] = player["guardians"].replace(" and ", ", ")
        if player["experience"] == "YES":
            player["experience"] = True
            is_experienced.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            not_experienced.append(player)
    return not_experienced, is_experienced


def balance_teams():
    exp_players_per_team = int(len(is_experienced) / len(teams_list))
    non_exp_players_per_team = int(len(not_experienced) / len(teams_list))
    total_num_players_per_team = exp_players_per_team + non_exp_players_per_team
    for player in is_experienced:
        if len(bandits) < exp_players_per_team:
            bandits.append(player)
        elif len(panthers) < exp_players_per_team:
            panthers.append(player)
        elif len(warriors) < exp_players_per_team:
            warriors.append(player)
    for player in not_experienced:
        if len(bandits) < total_num_players_per_team:
            bandits.append(player)
        elif len(panthers) < total_num_players_per_team:
            panthers.append(player)
        elif len(warriors) < total_num_players_per_team:
            warriors.append(player)
    return bandits, panthers, warriors


def team_select_menu():
    team_1 = "Panthers"
    team_2 = "Bandits"
    team_3 = "Warriors"
    print("BASKETBALL TEAM STATS TOOL")
    print("\n")
    print("*********  MENU  *********")
    print("\n")
    print("YOUR OPTIONS ARE:  ")
    print("""
Enter-> A) Team Stats

Enter-> B) To Exit
    """)
    option = input("Enter an OPTION: ")
    while True:
        try:
            if option.upper() == "A":
                print("\nEnter-> A) Team Panthers Stats")
                print("\n")
                print("Enter-> B) Team Bandits Stats")
                print("\n")
                print("Enter-> C) Team Warriors Stats")
                break
            elif option.upper() == "B":
                print("\nExiting Basketball Team Stats Tool.")
                sys.exit()
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
            return team_select_menu()
    while True:
        try:
            team_option = input("\nEnter an OPTION: ")
            if team_option.upper() == "A":
                print(f"\nTeam Name: {team_1}")
                print("=+=+=+=+=+=+=+=+=+=+=+=")
                players_exp_non_exp()
                names_guardians_height(panthers)
                see_other_teams()
            elif team_option.upper() == "B":
                print(f"\nTeam Name: {team_2}")
                print("=+=+=+=+=+=+=+=+=+=+=+=")
                players_exp_non_exp()
                names_guardians_height(bandits)
                see_other_teams()
            elif team_option.upper() == "C":
                print(f"\nTeam Name: {team_3}")
                print("=+=+=+=+=+=+=+=+=+=+=+=")
                players_exp_non_exp()
                names_guardians_height(warriors)
                see_other_teams()
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
        return team_select_menu()


def players_exp_non_exp():
    print(
        f"Players on Team: {int(len(constants.PLAYERS) / len(constants.TEAMS))} | "
        f"Experienced Players on Team: {int(len(is_experienced) / len(teams_list))} | "
        f"Inexperienced Players on Team: {int(len(not_experienced)/ len(teams_list))} "
        )


def names_guardians_height(team_name):
    names = [player["name"] for player in team_name]
    guardians = []
    height = [player["height"] for player in team_name]
    for player in team_name:
        player_guardian = player["guardians"]
        guardians.append(player_guardian)
    average_height = round(sum(height) / len(team_name), 1)
    print(f"\nAverage Height on Team: {float(average_height)}")
    print("\nNames of Players:")
    print(", ".join(names))
    print("\nGuardians of Players:")
    print(", ".join(guardians))


def see_other_teams():
    more_stats = input("\nWould you like to see other teams? ENTER: Y or N ")
    more_stats = str(more_stats)
    if more_stats.upper() == "Y":
        print("\nOK, rerouting to the main menu.")
        return team_select_menu()
    elif more_stats.upper() == "N":
        print("\nExiting the Team Stats Tool.")
        sys.exit()
    else:
        print("\nThat's not an OPTION. Rerouting to main menu.")
        return team_select_menu()


if __name__ == "__main__":
    clean_data()
    balance_teams()
    team_select_menu()
