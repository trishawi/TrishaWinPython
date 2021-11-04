import os

def menu():
    print("""\n1. Hello World\n2. Goodbye World\n3. Goodbye Person\n4. Good Teacher\n5. forLoop\n6. whileLoop\n7. string Loop\n8. Convert to ascii\n9. Encode a string\nx. To Exit""")


def hello_world():
    print("""Hello World""")

def goodbye_world():
    print("Hello World")
    input("------> Program paused - press enter to continue")
    print("Goodbye World")

def goodbye_person():
    name1 = input("Hello World\nWhat is your name ? ")
    print("Goodbye " + name1)

def good_teacher():
    teacher = input("Teacher's name (try Mr Horan) ")
    if teacher == "Mr Horan":
        print("You are lucky, he is a great teacher.")
    else:
        print(teacher + " is an ok teacher")

def for_loop():
    x = 0
    while (x<499):
        x = (x + 1)
        print(x)

def while_loop():
    while True:
        answer = input("What is the name of this subject ")
        if answer != "IST":
            print("Not correct - try again")
        else:
            break

    print("\n\nCongratulations!!\n\n")

def unknown():
    print("invalid option")

def x():
    print()

def start():
    print("\n----Start of Output ---------------------------\n")

def end():
    print("\n----End of Output -----------------------------\n\n\n")

def enter():
    input("Press Enter to continue")

print(""" ------------------------------------------------
|                                                |
|    07Menu                                      |
|    Name : Trisha Win                           |
|    Version : 01                                |
|                                                |
------------------------------------------------""")

os.system('cls')
menu()

answer = input("Enter an option ")

if answer == "1":
    start()
    hello_world()
    end()
    enter()
elif answer == "2":
    start()
    goodbye_world()
    end()
    enter()
elif answer == "3":
    start()
    goodbye_person()
    end()
    enter()
elif answer == "4":
    start()
    good_teacher()
    end()
    enter()
elif answer == "5":
    start()
    for_loop()
    end()
    enter()
elif answer == "6":
    start()
    while_loop()
    end()
    enter()
else:
    start()
    unknown()
    end()
    enter()