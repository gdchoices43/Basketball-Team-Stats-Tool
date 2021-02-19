import sys
import constants
import copy

players_list = copy.deepcopy(constants.PLAYERS)
has_experience = []
no_experience = []


def clean_data():
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
    team_bandits = []
    team_warriors = []
    team_panthers = []
    teams = [team_bandits, team_warriors, team_panthers]
    num_players = len(teams)
    for num in range(len(players_list)):
        teams[num % num_players].append(players_list[num])
    return teams


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
                team_bandits = balance_teams()[0]
                num_players = len(team_bandits)
                print("\nTeam: Bandits\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_a = []
                for player in team_bandits:
                    players_name = player["name"]
                    team_list_a.append(str(players_name))
                    # Got this solution from "Daniel OSullavin". I was using .join and it was not the result
                    # I wanted and for the life of me couldn't figure it out
                    print(player["name"], end=", ")
                break
            elif team_option.upper() == "B":
                team_warriors = balance_teams()[0]
                num_players = len(team_warriors)
                print("\nTeam: Warriors\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_b = []
                for player in team_warriors:
                    players_name = player["name"]
                    team_list_b.append(str(players_name))
                    print(player["name"], end=", ")
                break
            elif team_option.upper() == "C":
                team_panthers = balance_teams()[0]
                num_players = len(team_panthers)
                print("\nTeam: Panthers\n=+=+=+=+=+=+=+=+=+=+=+=+=+\nPlayers: {}\n".format(num_players))
                team_list_c = []
                for player in team_panthers:
                    players_name = player["name"]
                    team_list_c.append(str(players_name))
                    print(player["name"], end=", ")
                break
            raise ValueError()
        except ValueError as e:
            print("\nThat's not a valid option. Please try again.")
            break


if __name__ == "__main__":
    clean_data()
    team_stat_menu()
