import sys
import constants
import copy

teams_list = copy.deepcopy(constants.TEAMS)
players_list = copy.deepcopy(constants.PLAYERS)
not_experienced = []
is_experienced = []
all_teams = int(len(teams_list))


def player_height():
    for player in players_list:
        height = player["height"].split()
        player["height"] = int(height[0])


def player_guardian():
    for player in players_list:
        player["guardians"] = player["guardians"]


def balance_teams():
    panthers = []
    bandits = []
    warriors = []
    teams = [panthers, bandits, warriors]
    num_teams = len(teams)
    # Jennifer Nordell gave helped me with figuring this out
    for num in range(len(players_list)):
        teams[num % num_teams].append(players_list[num])
        for player in players_list:
            if player["experience"] == "NO":
                player["experience"] = False
                not_experienced.append(player)
            elif player["experience"] == "YES":
                player["experience"] = True
                is_experienced.append(player)
                num_of_exp = len(is_experienced)
                num_of_no_exp = len(not_experienced)
                exp_per_team = int(num_of_exp / num_teams)
                no_exp_per_team = int(num_of_no_exp / num_teams)
                for players in is_experienced:
                    player_with_exp = players["name"]
                    if len(panthers) < exp_per_team:
                        panthers.append(player_with_exp)
                    elif len(bandits) < exp_per_team:
                        bandits.append(player_with_exp)
                    elif len(warriors) < exp_per_team:
                        warriors.append(player_with_exp)
                for players in not_experienced:
                    player_with_no_exp = players["name"]
                    if len(panthers) < no_exp_per_team:
                        panthers.append(player_with_no_exp)
                    elif len(bandits) < no_exp_per_team:
                        bandits.append(player_with_no_exp)
                    elif len(warriors) < no_exp_per_team:
                        warriors.append(player_with_no_exp)
    return panthers, bandits, warriors, teams


def team_stat_menu():
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
            # Jennifer Nordell was responsible for me being able to raise and except these ValueErrors correctly
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option.Please try again.")
            return team_stat_menu()
    team_option = input("\nEnter an OPTION: ")
    while True:
        try:
            if team_option.upper() == "A":
                panthers = balance_teams()[0]
                num_players = len(panthers)
                height = [player["height"] for player in panthers]
                # got ths solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(panthers), 1)
                print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                print(f"Experienced Players: {int(len(is_experienced) / all_teams)}")
                print(f"\nInexperienced Players: {int(len(not_experienced) / all_teams)}\n")
                print("Average Height on Team:", average_height, "\n")
                team_a = []
                for player in panthers:
                    name = player["name"]
                    team_a.append(str(name))
                print("Players on Roster:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_a))
                print("\n")
                team_a_guardians = []
                for player in panthers:
                    guardians = player["guardians"]
                    team_a_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_a_guardians))
                more_stats = input("\nWould you like to see other teams? ENTER: Y or N ")
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
                height = [player["height"] for player in bandits]
                # got ths solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(bandits), 1)
                print("\nTeam: Bandits\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                print(f"Experienced Players: {int(len(is_experienced) / all_teams)}")
                print(f"\nInexperienced Players: {int(len(not_experienced) / all_teams)}\n")
                print("Average Height on Team:", average_height, "\n")
                team_b = []
                for player in bandits:
                    name = player["name"]
                    team_b.append(str(name))
                print("Players on Roster:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_b))
                print("\n")
                team_b_guardians = []
                for player in bandits:
                    guardians = player["guardians"]
                    team_b_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_b_guardians))
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
                height = [player["height"] for player in warriors]
                # got ths solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(warriors), 1)
                print("\nTeam: Warriors\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                print(f"Experienced Players: {int(len(is_experienced) / all_teams)}")
                print(f"\nInexperienced Players: {int(len(not_experienced) / all_teams)}\n")
                print("Average Height on Team:", average_height, "\n")
                team_c = []
                for player in warriors:
                    name = player["name"]
                    team_c.append(str(name))
                print("Players on Roster:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_c))
                print("\n")
                team_c_guardians = []
                for player in warriors:
                    guardians = player["guardians"]
                    team_c_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R from TeamTreeHouse Slack gave me this solution
                print(", ".join(team_c_guardians))
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
            # Jennifer Nordell was responsible for me being able to raise and except these ValueErrors correctly
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
            return team_stat_menu()


if __name__ == "__main__":
    player_height()
    player_guardian()
    balance_teams()
    team_stat_menu()
