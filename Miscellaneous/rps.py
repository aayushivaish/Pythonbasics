'''
There will be two players
Both players will select one choice R-Rock,P-Paper,S-scissor
Accordingly we will select which player is winner.
Rock beats Scissor
Scissor beats Paper
Paper Beats Rock
'''
import random
def rps():
    p1 = 0
    p2 = 0
    choice = "Y"
    while(choice == "Y" or choice == "y"):

        Choices = ["R", "P" ,"S"]
        player_1 = input("Enter player 1 Choice R-Rock,P-Paper,S-scissor ")
        player_2 = random.choice(Choices)
        winner , score = game(player_1,player_2)
        print(winner)
        if score == "P1":
            p1 = p1+1
        elif score == "P2":
            p2 = p2+1
        print("Score: \nPlayer_1 {} \nPlayer_2 {}".format(p1,p2))
        choice = input("Do you want to continue? ")
        


def game(P1,P2):
    if P1 == P2:
        return "Its a tie", 0
    elif P1 == "R" and P2 == "S":
        return "Player_1 is the winner (Rock Beats Scissor)", "P1"
    elif P1 == "S" and P2 =="P":
        return "Player_1 is the winner (Scissor Beats Paper)", "P1"
    elif P1 == "P" and P2 =="R":
        return "Player_1 is the winner (Paper Beats Rock)", "P1"
    else:
        return ("Player_2 is the winner ( {} beats {})".format(P2,P1)), "P2"
rps()


