#Rock,Peper,Scissor

import random

Game = ("Rock" , "Peper" , "Scissor")
Player = input("Please insert Rock,Paper,Scissor: ")
system = random.choice(Game)
if Player == "Rock":
    if system == "Rock":
        print("Mosavi")
    if system == "Peper":
        print("Bakht")
    if system == "Scissor":
        print("Win")
elif Player == "Peper":
    if system == "Rock":
        print("Win")
    if system == "Peper":
        print("Mosavi")
    if system == "Scissor":
        print("Bakht")
else:
    if system == "Rock":
        print("Win")
    if system == "Peper":
        print("Bakht")
    if system == "Scissor":
        print("Mosavi")


print("Player: " , Player)
print("system: " , system)