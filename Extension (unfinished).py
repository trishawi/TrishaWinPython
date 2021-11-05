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
        answer = input("Guess my number. ")
        if int(answer) < x:
            print("Your answer is too small.")
        elif int(answer) > x:
            print("Your answer is too large.")
        elif int(answer) == x:
            break
    print("Hooray! You guessed the number in " + str(guesses) + " guesses!") 

def scissors_paper_rock():
    win = 0
    print("Welcome to Scissors Paper Rock!\nHow to play:\nPick scissors, paper or rock and I will do the same. Good luck!")
    time.sleep(2)
    input("Press enter to start")
    choice = (input("Enter scissors, paper or rock. ")).lower()
    mylist = ["scissors", "paper", "rock"]
    x = (random.choice(mylist))
    if choice == "scissors":
        print("You chose scissors.")
        if x == "scissors":
            print("I chose scissors.")
            win = 2
        elif x == "paper":
            print("I chose paper.")
            win = 3
        elif x == "rock":
            print("I chose rock.")
            win = 1
    elif choice == "paper":
        print("You chose scissors.")
        if x == "scissors":
            print("I chose scissors.")
            win = 1
        elif x == "paper":
            print("I chose paper.")
            win = 2
        elif x == "rock":
            print("I chose rock.")
            win = 3
    elif choice == "rock":
        print("You chose rock.")
        if x == "scissors":
            print("I chose scissors.")
            win = 3
        elif x == "paper":
            print("I chose paper.")
            win = 1
        elif x == "rock":
            print("I chose rock.")
            win = 2
    if win == 1:
        print("You lose.")
    elif win == 2:
        print("Draw!")
    elif win == 3:
        print("You win!")

def invalid():
    input("Invalid option. Press Enter to return.")
    os.system('cls')

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

game = ""
while game != "x":
    print("Welcome to the python minigames, " + name + "! Choose a game below:\n1. Number Guesser\n2. Scissors Paper Rock\nx. Exit")
    time.sleep(0.5) 
    game = input("Enter your choice: ")
    if game == "1":
        number_guesser()
        enter()
    elif game == "2":
        scissors_paper_rock()
        enter()
    elif game != "1" and game != "2" and game != "x":
        invalid()

print("Thanks for playing!")
time.sleep(0.5)