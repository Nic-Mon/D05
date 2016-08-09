#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body


def infinite_stairway_room(username, count=0):
    print(username + " walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print(username + ' takes the stairs')
        if (count > 0):
            print("but he/she is not happy about it")
        infinite_stairway_room(username, count + 1)
    # option 2 == ?????
    if next == "turn around":
        back_room(username)
    else:
        print("I got no idea what that means.")
        
def back_room(username):
    print(username + " enters a room filled with awesome programmers.")
    print(username + " states his name when asked, and the programmers reply: Welcome " + username)
    print(username + " starts coding python and never leaves")
    exit(0)

def gold_room(username):
    print("This room is full of gold.  How much does " +username + " take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, " + username + " isn't greedy, he/she wins!")
        exit(0)
    else:
        dead(username + ", that greedy goose!")


def bear_room(username):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is " + username + " going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        #user can input just 'take' or 'honey'
        if "take" in next or "honey" in next:
            dead("The bear looks at " + username + " then slaps his/her face off.")

        #user can input just 'taunt'
        elif "taunt" in next and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews " + username + "\'s leg off.")
        elif "open" in next or "door" in next and bear_moved:
            gold_room(username)
        else:
            print("I got no idea what that means.")


def cthulhu_room(username):
    print("Here " + username + " sees the great evil Cthulhu.")
    print("He, it, whatever stares at " + username + " and " + username + " goes insane.")
    print("Does " + username + " flee for his/her life or eat his/her head?")

    next = input("> ")

    if "flee" in next:
        start(username)
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(username)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################

def start(username):

    print(username + " is in a dark room.")
    print("There is a door to " + username + "\'s right and left, and one behind")
    print("Which one does " + username + " take?")

    next = input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    elif next == "behind":
        infinite_stairway_room(username)
    else:
        dead(username + " stumbles around the room until " + username + " starves.")


def main():
    # START the TextAdventure game

    username = str(input("Enter Your Name: "))

    start(username)

if __name__ == '__main__':
    main()
