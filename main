
import tkinter as tk
import random as r

number_of_cards = 0

def game():
    print()
    with open("dogs.txt", "r") as df:
        for line in df:
            exercise = r.randint(1,5)
            intelligence = r.randint(1,100)
            friendliness = r.randint(1,10)
            drool = r.randint(1,10)
            card = f"NAME: {line}"
            print(card)
            print(f"| EXERCISE: {exercise} \n| INTELLIGENCE: {intelligence} \n| FRIENDLINESS: {friendliness} \n| DROOL: {drool}")
            print()

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
    print()
    print("TOP DOGS / CELEBRITY DOGS")
    print("1. PLAY GAME  2. QUIT ")
    print()
    dec = int(input(": "))
    if dec == 1:
        cardnum()

    elif dec == 2:
        break