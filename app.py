import sys
import constants
import copy

teams_list = copy.deepcopy(constants.TEAMS)
players_list = copy.deepcopy(constants.PLAYERS)
not_experienced = []
is_experienced = []


def clean_data():
    for player in players_list:
        if player["experience"] == "YES":
            player["experience"] = True
            is_experienced.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            not_experienced.append(player)
        height = player["height"].split()
        player["height"] = int(height[0])
        # Mel R {they/them} TeamTreeHouse Slack gave me a couple suggestions
        # on how how to take the "and" out of the guardians list
        player["guardians"] = player["guardians"].replace(" and ", ", ")


def balance_teams():
    # I had previoulsy made this function so much more difficult than what I was trying to accomplish
    # Mel R {they/them} suggested I look at my function and make sure it is doing everythig I'm intending it
    # to do. That's when I realized the soution was much simpler. All I needed to do was use indexing to call
    # a team and then use indexing again to put the first 3 exp players and the first 3 non_exp players on
    # that team.
    teams_list[0] = is_experienced[:3] + not_experienced[:3]
    teams_list[1] = is_experienced[3:6] + not_experienced[3:6]
    teams_list[2] = is_experienced[6:9] + not_experienced[6:9]


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
            # Jennifer Nordell TeamTreeHouse Slack was responsible for me being able to raise and except these
            # ValueErrors correctly
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option.Please try again.")
            return team_stat_menu()
    team_option = input("\nEnter an OPTION: ")
    while True:
        try:
            if team_option.upper() == "A":
                panthers = teams_list[0]
                num_players = len(panthers)
                # I rewatched the "Python Comprehensions Workshop" and realized This was the way to get the
                # proper output for showing exp/non_exp players per team
                exp_player = [player["experience"] for player in panthers if player["experience"] == True]
                non_exp_player = [player["experience"] for player in panthers if player["experience"] == False]
                height = [player["height"] for player in panthers]
                # Got this solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(panthers), 1)
                print(
                    f"\nTeam: Panthers Stats\n=+=+=+=+=+=+=+=+=+=+=+=\nPlayers: {int(num_players)} "
                    f"Experienced Players: {int(len(exp_player))} "
                    f"Inexperienced Players: {int(len(non_exp_player))} "
                    f"Average Height on Team: {float(average_height)}\n")
                team_a = []
                for player in panthers:
                    name = player["name"]
                    team_a.append(str(name))
                print("Players on Roster:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
                print(", ".join(team_a))
                print("\n")
                team_a_guardians = []
                for player in panthers:
                    guardians = player["guardians"]
                    team_a_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
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
                bandits = teams_list[1]
                num_players = len(bandits)
                # I rewatched the "Python Comprehensions Workshop" and realized This was the way to get the
                # proper output for showing exp/non_exp players per team
                exp_player = [player["experience"] for player in bandits if player["experience"] == True]
                non_exp_player = [player["experience"] for player in bandits if player["experience"] == False]
                height = [player["height"] for player in bandits]
                # got this solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(bandits), 1)
                print(
                    f"\nTeam: Bandits Stats\n=+=+=+=+=+=+=+=+=+=+=+=\nPlayers: {int(num_players)} "
                    f"Experienced Players: {int(len(exp_player))} "
                    f"Inexperienced Players: {int(len(non_exp_player))} "
                    f"Average Height on Team: {float(average_height)}\n")
                team_b = []
                for player in bandits:
                    name = player["name"]
                    team_b.append(str(name))
                print("Players on Roster:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
                print(", ".join(team_b))
                print("\n")
                team_b_guardians = []
                for player in bandits:
                    guardians = player["guardians"]
                    team_b_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
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
                warriors = teams_list[2]
                num_players = len(warriors)
                # I rewatched the "Python Comprehensions Workshop" and realized This was the way to get the
                # proper output for showing exp/non_exp players per team
                exp_player = [player["experience"] for player in warriors if player["experience"] == True]
                non_exp_player = [player["experience"] for player in warriors if player["experience"] == False]
                height = [player["height"] for player in warriors]
                # got this solution from GeekForGeeks https://geeksforgeeks/find-average-list-python
                average_height = round(sum(height) / len(warriors), 1)
                print(
                    f"\nTeam: Warriors Stats\n=+=+=+=+=+=+=+=+=+=+=+=\nPlayers: {int(num_players)} "
                    f"Experienced Players: {int(len(exp_player))} "
                    f"Inexperienced Players: {int(len(non_exp_player))} "
                    f"Average Height on Team: {float(average_height)}\n")
                team_c = []
                for player in warriors:
                    name = player["name"]
                    team_c.append(str(name))
                print("Players on Roster:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
                print(", ".join(team_c))
                print("\n")
                team_c_guardians = []
                for player in warriors:
                    guardians = player["guardians"]
                    team_c_guardians.append(str(guardians))
                print("Players Guardians:")
                # Mel R {they/them} TeamTreeHouse Slack helped me with this solution
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
            # Jennifer Nordell TeamTreeHouse was responsible for me being able to raise and except these
            # ValueErrors correctly
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
            return team_stat_menu()


if __name__ == "__main__":
    clean_data()
    balance_teams()
    team_stat_menu()
