'''
There will be three levels
Easy= 1 to 10 (Attempts = 3), points= +1, Deduction= -0.3
Medium= 1 to 50 (Attempts = 5), points= +3, Deduction= -1
Hard= 1 to 100 (Attempts = 10), points= +10, Deduction= -3

'''
import random
def game():
    userpoints = 0
    c = "Y"
    while c == "Y" or "y":
        print (c)
        lev = input("Select Level \nE-easy\nM-medium\nH-hard\n ")
        p= level(lev)
        userpoints = userpoints + p
        print("Points {}".format(userpoints))
        c = input("Do you want to continue? (Y) ")
        if c != "Y":
            exit()

def level(level):
    if level == "E":
        r = 10
        points = 1
        attempts = 3
        deduction = -0.3
    elif level == "M":
        r = 50
        points = 3
        attempts = 5
        deduction = -1
    elif level == "H":
        r = 100
        points = 10
        attempts = 10
        deduction = -3
    choices = []
    num = random.randint(1,r)
    for i in range(0,attempts):
        userchoice = int(input("Enter your Guess "))
        if userchoice == num:
            print("Congratulations, correct guess ")
            retpoints = points
            flag = 1
            break
        else:
            choices.append(userchoice)
            flag = 0
    if flag != 1:
        retpoints = deduction
        print("Oops, wrong choices {} correct choice {}".format(choices,num))
        return retpoints

    else:
        return retpoints
game()

