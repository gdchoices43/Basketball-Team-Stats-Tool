import sys
import constants
import copy

players_list = copy.deepcopy(constants.PLAYERS)
has_experience = []
no_experience = []


def clean_data():
    experience()
    balance_teams()


def experience():
    for player in players_list:
        if player["experience"] == "NO":
            player["experience"] = False
            no_experience.append(player)
        elif player["experience"] == "YES":
            player["experience"] = True
            has_experience.append(player)


def balance_teams():
    players_per_team = len(constants.PLAYERS) / len(constants.TEAMS)
    team_bandits = []
    team_warriors = []
    team_panthers = []
    teams = [team_bandits, team_warriors, team_panthers]
    num_players = len(teams)
    for num in range(len(players_list)):
        teams[num % num_players].append(players_list[num])
        return team_bandits, team_panthers, team_warriors


def team_stat_menu():
    while True:
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
            except ValueError:
                print("That's not a valid option. Please try again.")
                continue
        team_option = input("\nEnter an OPTION: ")
        while True:
            try:
                if team_option.upper() == "A":
                    team_bandits = balance_teams()[0]
                    num_players = len(team_bandits)
                    print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+"
                    "\nPlayers: {}\n".format(num_players))
                    team_list1 = []
                    for player in team_bandits:
                        players_name = player["name"]
                        team_list1.append(str(players_name))
                        print(", ".join(team_list1))
                elif team_option.upper() == "B":
                    team_warriors = balance_teams()[0]
                    num_players = len(team_warriors)
                    print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+"
                    "\nPlayers: {}\n".format(num_players))
                    team_list2 = []
                    for player in team_warriors:
                        players_name = player["name"]
                        team_list2.append(str(players_name))
                        print(", ".join(team_list2))
                elif team_option.upper() == "C":
                    team_panther = balance_teams()[0]
                    num_players = len(team_panther)
                    print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+"
                    "\nPlayers: {}\n".format(num_players))
                    team_list3 = []
                    for player in team_panther:
                        players_name = player["name"]
                        team_list3.append(str(players_name))
                        print(", ".join(team_list3))
                        break
            except ValueError:
                print("That's not a valid option. Please try again.")
                continue


if __name__ == "__main__":
    team_stat_menu()
