import sys
import constants
import copy

teams_list = copy.deepcopy(constants.TEAMS)
players_list = copy.deepcopy(constants.PLAYERS)
no_experience = []
has_experience = []


def clean_data():
    for player in players_list:
        if player["experience"] == "NO":
            player["experience"] = False
            no_experience.append(player)
        elif player["experience"] == "YES":
            player["experience"] = True
            has_experience.append(player)


def balance_teams():
    panthers = []
    bandits = []
    warriors = []
    all_teams = [panthers, bandits, warriors]
    num_teams = len(all_teams)
    for num in range(len(players_list)):
        all_teams[num % num_teams].append(players_list[num])
    return panthers, bandits, warriors


def team_stat_menu():
    print("\n")
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
                print("\nEnter-> A) Team Bandits Stats")
                print("\n")
                print("Enter-> B) Team Warriors Stats")
                print("\n")
                print("Enter-> C) Team Panthers Stats")
                break
            elif option.upper() == "B":
                print("\nExiting Basketball Team Stats Tool.")
                sys.exit()
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option.Please try again.")
            break
    team_option = input("\nEnter an OPTION: ")
    while True:
        try:
            if team_option.upper() == "A":
                panthers = balance_teams()[0]
                num_players = len(panthers)
                print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_a = []
                for player in panthers:
                    players_name = player["name"]
                    team_list_a.append(str(players_name))
                    print(player["name"], end="\n")
                more_stats = input("\n\nWould you like to see other teams? ENTER: Y or N ")
                more_stats = str(more_stats)
                if more_stats.upper() == "Y":
                    print("\nOK, rerouting to the main menu.")
                    return team_stat_menu()
                elif more_stats.upper() == "N":
                    print("\nExiting the Team Stats Tool.")
                    sys.exit()
                else:
                    print("\nThat's not an OPTION. Rerouting to main menu.")
                    return team_stat_menu()
            elif team_option.upper() == "B":
                bandits = balance_teams()[1]
                num_players = len(bandits)
                print("\nTeam: Bandits\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_b = []
                for player in bandits:
                    players_name = player["name"]
                    team_list_b.append(str(players_name))
                    print(player["name"], end="\n")
                more_stats = input("\n\nWould you like to see other teams? ENTER: Y or N ")
                more_stats = str(more_stats)
                if more_stats.upper() == "Y":
                    print("\nOk rerouting to the main menu.")
                    return team_stat_menu()
                elif more_stats.upper() == "N":
                    print("\nExiting the Team Stats Tool.")
                    sys.exit()
                else:
                    print("\nThat's not an OPTION. Rerouting to main menu.")
                    return team_stat_menu()
            elif team_option.upper() == "C":
                warriors = balance_teams()[2]
                num_players = len(warriors)
                print("\nTeam: Warriors\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_c = []
                for player in warriors:
                    player_name = player["name"]
                    team_list_c.append(str(player_name))
                    print(player["name"], end="\n")
                more_stats = input("\n\nWould you like to see other teams? ENTER: Y or N ")
                more_stats = str(more_stats)
                if more_stats.upper() == "Y":
                    print("\nOk rerouting to the main menu.")
                    return team_stat_menu()
                elif more_stats.upper() == "N":
                    print("\nExiting the Team Stats Tool.")
                    sys.exit()
                else:
                    print("\nThat's not an OPTION. Rerouting to main menu.")
                    return team_stat_menu()
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
            break


if __name__ == "__main__":
    clean_data()
    balance_teams()
    team_stat_menu()
