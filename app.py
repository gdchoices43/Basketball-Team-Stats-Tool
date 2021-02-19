import constants
import sys
import copy

player_list = copy.deepcopy(constants.PLAYERS)
teams_list = copy.deepcopy(constants.TEAMS)

team_bandits = []
team_warriors = []
team_panthers = []
is_exp = []
no_exp = []

def clean_data():
    for player in player_list:
        player_hgt = player["height"].split()
        player_hgt = int(player_hgt[0])
        if player["experience"] == "NO":
            player["experience"] = False
            no_exp.append(player)
        elif player["experience"] == "YES":
            palyer["experience"] = True
            is_exp.append(player)



def clean_guardian():
    for player in player_list:
        player["guardians"] = player["gaurdian"].split(" and ")


def balance_teams():
    pass


def team_stat_menu():
    while True:
        print("\n")
        print("BASKETBALL TEAM STATS TOOL")
        print("\n")
        print("*********  MENU  *********")
        print("\n")
        print("YOUR OPTIONS ARE:  ")
        print("""
    Enter-> A) For Team Stats

    Enter-> B) To Quit
        """)
        option = input("Enter an option: ")

        while True:
            try:
                if option == "B":
                    print("Quitting the Basketball Team Stats Tool.")
                    break
                elif option == "A":
                    print("""
                    \nEnter-> A) Bandits\nEnter-> B) Warriors\nEnter-> C) panthers
                    """)
                    team_option = input("Enter an option: ")
                    if team_option == "A":
                        pass
                    elif team_option == "B":
                        pass
                    elif team_option == "C":
                        pass
            except ValueError:
                print("That was not a valid OPTION. Please try again")
                return team_stat_menu()


if __name__ == "__main__":
    clean_data()
    clean_guardian()
