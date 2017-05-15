import random
import sys


class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score += score
    def place_bet(self):
        print self.name, " Please enter a number between 1 and 4 "
        self.bet = int(raw_input())

    """
    def stats(self):
        for i in range(0, playersCount):
            self.
        """

class Game():
    def __init__(self, playersCount, gamesCount):
        self.playersCount = int(playersCount)
        self.gamesCount   = int(gamesCount)
        self.Players = []
        for i in range(playersCount):
            print "Player ",i+1
            playerName = raw_input("Please enter the name ")
            player = Player(playerName)
            self.Players.append(player)

    def game_loop(self):
        for i in range(0, self.gamesCount):
            for j in range(0, self.playersCount):
                self.Players[j].place_bet()
            randomnumber = random.randrange(1,4)
            print "random number :", randomnumber
            
            for j in range(0, self.playersCount):
                if randomnumber == self.Players[j].bet:
                    self.Players[j].add_score(1)
                    print "the WINNER is ",self.Players[j].name.upper()
                else:
                   print self.Players[j].name,"lost :("


playersCount   = int(sys.argv[1])
gamesCount     = int(sys.argv[2])

game = Game(playersCount,gamesCount)
game.game_loop()
