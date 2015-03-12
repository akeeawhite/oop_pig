__author__ = 'Akeea'

"""
File: pig.py
Source: https://python8460.wordpress.com/2011/11/03/game-of-pig-python/
Original Date: 11/3/2011
Revised By: Akeea White
Revision Date: 3/12/2015
The Classes are:
1) Die
2) Player
3) Main Class
    Note: For this Program, the main function controls the entire game
Comments:
Also, the original program is now an oop program
"""

import random
#Die class that generates a random number from 1 to 6
class Die:

    def roll_die(self, sides):
        self.r = random.randrange(1, 7)
        return self.r

#Player class allows one player to take a single turn
class Player:

    def __init__(self, player):
        self.player = player

    def take_turn(self, player):
        self.point = 0
        keep_rolling = 1
        print("Its your turn player ", player)
        input('Press enter to begin')
        while keep_rolling == 1:
            r = Die.roll_die(self, sides=self)
            print("you got a", r)
            if r == 1:
                self.point = 0
                keep_rolling = 0
            else:
                self.point += r
                print("Your total is", self.point)
                y = input("Do you want to continue (y=yes n=no)?  ")
                if y == "y":
                    keep_rolling = 1
                else:
                    keep_rolling = 0
                    print("Your turn is over player", player)
        return self.point

#Main Class calls all other classes
class Main:
    self = Die()
    self = Player(player=self)
    p1 = 0
    p2 = 0
    print("Welcome to the game of Pig. To win, be the")
    print("player with the most points at the end of the")
    print("game. The game ends at the end of a round where")
    print("at least one player has 100 or more points")
    print("")
    print("On each turn, you may roll the die as many times")
    print("as you like to obtain more points. However, if")
    print("you a 1, your turn is over, and you do not")
    print("obtain any points that turn.")
    while p1 < 100 and p2 < 100:
        print("Player points are:" + str(p1))
        print("Player points are:" + str(p2))
        r = self.take_turn(1)
        p1 += r
        print("Player points are:" + str(p1))
        print("Player points are:" + str(p2))
        r = self.take_turn(2)
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