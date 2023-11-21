import random
from Forme import *

score1 = 0
score2 = 0
cnt = 0

while cnt < 3:
    if score1 == 2 or score2 == 2:
        break
    x = input("Rock, Paper, or Scissors?")
    if x == "1":
        print(rock)
    elif x == "2":
        print(paper)
    elif x == "3":
        print(scissors)
    else:
        print("must choose an option between 1, 2 and 3")
        break



    print("Computer choose:")
    z = {1: "Rock", 2: "Paper", 3: "Scissors"}
    z1 = random.randint(1, 3)
    if z1 == 1:
        print(rock)
    elif z1 == 2:
        print(paper)
    elif z1 == 3:
        print(scissors)

    if z1 == int(x):
        print("Tie")
    elif z[z1] == "Rock" and x == "2":
        print("You win this round")
        score1 += 1
        cnt += 1
    elif z[z1] == "Paper" and x == "1":
        print("You lose this round")
        score2 += 1
        cnt += 1
    elif z[z1] == "Rock" and x == "3":
        print("You lose this round")
        score2 += 1
        cnt += 1
    elif z[z1] == "Scissors" and x == "1":
        print("You win this round")
        score1 += 1
        cnt += 1
    elif z[z1] == "Scissors" and x == "2":
        print("You lose this round")
        score2 += 1
        cnt += 1
    elif z[z1] == "Paper" and x == "3":
        print("You win this round")
        score1 += 1
        cnt += 1

if score1 > score2:
    print("\nYou win the game, Congratulations ! :)")
else:
    print("\nYou lose the game :(")