
import tkinter as tk
import random as r

card = str

def write_to_player():
    with open("player.txt", "w") as pf:
        pf.write()

def write_to_computer():
    with open("computer.txt", "w") as cf:
        cf.write()

def game():
    while True:
        print()
        print("How many cards to use? ")
        print()
        number_of_cards = int(input(": "))
        if number_of_cards % 2 == 0 and number_of_cards in range(4,31):
            break
        else:
            print()
            print("INVALID")

    count = 0
    count2 = 0
    print()
    with open("dogs.txt", "r") as df, open("player.txt", "w") as pf, open("computer.txt", "w") as cf:
        for line in df:
            exercise = r.randint(1,5)
            intelligence = r.randint(1,100)
            friendliness = r.randint(1,10)
            drool = r.randint(1,10)
            card = f"NAME: {line}"
            name = str(line)
            print(card)
            print(f"| EXERCISE: {exercise} \n| INTELLIGENCE: {intelligence} \n| FRIENDLINESS: {friendliness} \n| DROOL: {drool}")
            print()
            count2 = count2 + 1
            if count2 % 2 == 0:
                pf.write(f"{name[:len(name) - 1]},{exercise},{intelligence},{friendliness},{drool}\n")
            else:
                cf.write(f"{name[:len(name) - 1]},{exercise},{intelligence},{friendliness},{drool}\n")
            count = count + 1
            if count == number_of_cards:
                break

def cardnum():
    while True:
        print()
        print("How many cards to use? ")
        print()
        number_of_cards = int(input(": "))
        if number_of_cards % 2 == 0 and number_of_cards in range(4,31):
            game()
            break
        else:
            print()
            print("INVALID")

while True:
    number_of_cards = 0
    count = 0
    print()
    print("TOP DOGS / CELEBRITY DOGS")
    print("1. PLAY GAME  2. QUIT ")
    print()
    dec = int(input(": "))
    if dec == 1:
        game()

    elif dec == 2:
        break