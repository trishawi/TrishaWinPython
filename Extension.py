import time
import random
import os

def number_guesser():
    print("Welcome to Number Guesser!\nHow to play:\nEnter a number higher than 0 and I will pick an integer from 0 to the number you have chosen. Guess the number I have chosen and you win.")
    time.sleep(2)
    input("Press enter to start")
    high = int(input("Enter your number. "))
    x = random.choice(range(0, high))
    answer = -1
    guesses = 0
    while answer != x:
        guesses = guesses + 1
        answer = input("Guess your number. ")
        if int(answer) < x:
            print("Your answer is too small.")
        elif int(answer) > x:
            print("Your answer is too large.")
        elif int(answer) == x:
            break
    print("Hooray! You guessed the number in " + str(guesses) + " guesses!")
    input("Press enter to return to the menu.")
    
        

def scissors_paper_rock():
    print("Welcome to Scissors Paper Rock!\nHow to play:\nPick scissors, paper or rock and I will do the same. Good luck!")
    time.sleep(2)
    input("Press enter to start")
    input("Press enter to return to the menu.")

def invalid():
    print("Invalid option.")

def enter():
    input("Press Enter to return to the menu.")
    os.system('cls')

print(""" ------------------------------------------------
|                                                |
|    Extension                                   |
|    Name : Trisha Win                           |
|    Version : 01                                |
|                                                |
------------------------------------------------""")
name = input("What's your name? ")

while game != "x":
    print("Welcome to the python minigames, " + name + "! Choose a game below:\n1. Number Guesser\n2. Scissors Paper Rock")
    time.sleep(0.5) 
    game = input("Enter your choice: ")
    if game == "1":
        number_guesser()
    elif game == "2":
        scissors_paper_rock()
    else:
        invalid()

print("Thanks for playing!")
wait(0.5)