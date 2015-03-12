__author__ = 'Akeea'

"""
File: pig.py
Source: https://python8460.wordpress.com/2011/11/03/game-of-pig-python/
Original Date: 11/3/2011
Revised By: Akeea White
Revision Date: 1/28/2015
Program:
In this program, two players will attempt to reach 100 points simply
rolling a die. At the beginning of the game, both players have 0 total points.
In each round, player 1 takes a turn, and player 2 takes a turn.
The player rolls a six sided die.
If the die roll produces a 1, then the player’s turn points are removed, and their turn is over.
If any other number is rolled (2-6), the roll is added to the player’s turn points.
The player now chooses whether to quit the turn, or continue the turn.
If the player quits the turn, their turn points are added to their total points.
If the player continues, then the player rolls the die again.
The game ends if at the end of a round, at least one of the players has 100 or more points.
The winner is the player with the most total points.

The functions are:
1) Roll a Six-Sided die
2) Taking a Turn
3) Giving Instructions
4) Main Control
    Note: For this Program, the main function controls the entire game
Comments:
The original game of pig program what meant to run on Python 2.7,
namely the parethesis around the print statement are not included.
In addition, made some clarification in line number 44, and omitted .

"""

import random


#1st function generates a random number from 1 to 6
def roll_die(sides):
    r = random.randrange(1, 7)
    return r

#2nd function allows one player to take a single turn
def take_turn(player):
    point = 0
    keep_rolling = 1
    print("Its your turn player ", player)
    input('Press enter to begin')
    while keep_rolling == 1:
        r = roll_die(6)
        print("you got a", r)
        if r == 1:
            point = 0
            keep_rolling = 0
        else:
            point += r
            print("Your total is", point)
            y = input("Do you want to continue (y=yes n=no)?  ")
            if y == "y":
                keep_rolling = 1
            else:
                keep_rolling = 0
                print("Your turn is over player", player)
    return point


#3rd Builds and returns the instructions on how to play the pig game
def show_instructions():
    print("Welcome to the game of Pig. To win, be the")
    print("player with the most points at the end of the")
    print("game. The game ends at the end of a round where")
    print("at least one player has 100 or more points")
    print("")
    print("On each turn, you may roll the die as many times")
    print("as you like to obtain more points. However, if")
    print("you a 1, your turn is over, and you do not")
    print("obtain any points that turn.")

# 4th function is the Main Function which calls the show_instructions functions
def main():
    show_instructions()
    p1 = 0
    p2 = 0
    while p1 < 100 and p2 < 100:
        print("Player points are:" + str(p1))
        print("Player points are:" + str(p2))
        r = take_turn(1)
        p1 += r
        print("Player points are:" + str(p1))

        print("Player points are:" + str(p2))
        r = take_turn(2)
        p2 += r
        print("Your turn is over")
        print("Player points are:" + str(p1))
        print("Player points are:" + str(p2))
    if p1 > p2:
        print("Player one is the winner")
    elif p2 > p1:
        print("player two is the winner")
    else:
        print("Tie game")

main()