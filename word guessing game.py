# Word Guessing Game

answer = int(input("player1: please insert a number(1 -100): "))
is_cprrect = False
try_count = 0 
while try_count < 11 and is_cprrect == False:
    guess = int(input("player2: please insert guess a number: "))
    if guess == answer:
        print("player2 you win!")
        is_cprrect = True
    elif guess < answer:
        print("player2 your guess smaller than the answer!")
        try_count += 1
    else:
        print("player2 you guess greater than the answer!")
        try_count += 1

if is_cprrect == False:
    print("player2 you lost!")