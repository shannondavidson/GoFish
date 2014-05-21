from time import sleep
from os import system
from random import randint
from random import shuffle
import re

class Game(object):

    def __init__(self):
        super(Game, self).__init__()

        self.pHand = []
        self.cHand = []
        self.pPoints = 0
        self.cPoints = 0
        self.turn = True

        self.deck = ["AS", "AC", "AH", "AD",
                     "2S", "2C", "2H", "2D",
                     "3S", "3C", "3H", "3D",
                     "4S", "4C", "4H", "4D",
                     "5S", "5C", "5H", "5D",
                     "6S", "6C", "6H", "6D",
                     "7S", "7C", "7H", "7D",
                     "8S", "8C", "8H", "8D",
                     "9S", "9C", "9H", "9D",
                     "10S","10C","10H","10D",
                     "JS", "JC", "JH", "JD",
                     "QS", "QC", "QH", "QD",
                     "KS", "KC", "KH", "KD" ]

    def __isGameOver(self):

        if len(self.deck) > 0:

            return True

        else:

            return False

    def drawCard(self, hand, name, card):

        hand.append(self.deck[0])
        self.deck.pop(0)

        if name == 'Player':

            print "[%s] :Drew A Card: [%s]" % (name, hand[len(hand) - 1])

        else:

            "[%s] :Drew A Card:" % name

        if hand[len(hand) - 1] == card:

            return hand, True

        return hand, False
        
    def shuffle(self):
        
        shuffle(self.deck)

    def createHand(self, hand):
        
        for i in range(0, 7):

            y = randint(0, len(self.deck) - 1)
            hand.append(self.deck[y])
            self.deck.remove(self.deck[y])

    def drawHand(self, hand):

        for card in hand:

            print "[" + card + "]",

        print

    def faceName(self, card):

        if card[0].upper() == 'K':

            return "King"

        elif card[0].upper() == 'Q':

            return "Queen"

        elif card[0].upper() == 'J':

            return "Jack"

        elif card[0].upper() == 'A':

            return "Ace"

        else:

            return card

    def checkHand(self, rank, player):

        def pla():

            print "[Player] Do You Have Any " + self.faceName(rank) + "s"

            sleep(1.5)

            for cards in self.cHand:

                if cards[0] == rank[0].upper():

                    print "[CPU] Yes"
                    sleep(1.5)
                    return True

            print "[CPU] No\n"
            sleep(1.5)
            return False

        def com():

            print "[CPU] Do You Have Any " + self.faceName(rank[0]) + "s"

            sleep(1.5)

            for cards in self.pHand:

                if cards[0] == rank[0]:

                    print "[Player] Yes"
                    sleep(1.5)
                    return True

            print "[Player] No\n"
            sleep(1.5)
            return False


        switch = {'P' : pla,
                   'C' : com }

        if player[0] in switch:

            return switch[player[0]]()

        else:

            pass
            #default

    def giveCard(self, card, f, t, name):

        x = []

        for i in range(0, len(f) - 1):

            if f[i][0] == card[0]:

                x.append(f[i])

        t.extend(x)

        print "[%s] :Got %d:" % (name, len(x))

        return t, f

    #:Sorting Function:#

    def atoi(self, text):
        
        return int(text) if text.isdigit() else text

    def sort_key(self, text):

        return [ self.atoi(c) for c in re.split('(\d+)', text) ]

    def sort(self, hand):

        hand.sort(key=self.sort_key)

    #:Find Books:#

    def findBooks(self, hand, name=None):

        x = 0

        for i in range(0, len(hand) - 1):

            if i < len(hand) - 3:

                if hand[i][0] == hand[i + 1][0] and \
                    hand[i + 1][0] == hand[i + 2][0] and \
                    hand[i + 2][0] == hand[i + 3][0]:

                    x += 1

                    hand.remove(hand[i])
                    hand.remove(hand[i + 1])
                    hand.remove(hand[i + 2])
                    hand.remove(hand[i + 3])

                    if name != None:

                        print "[%s] :Got A Book:" % name

        return x, hand

    def newTurn(self):

        while True:

            x = ''

            while x == '':
                
                self.sort(self.pHand)
                self.drawHand(self.cHand)
                self.drawHand(self.pHand)
                x = raw_input("player-- ")

                system('cls')
                

            if self.checkHand(x, 'Player'):

                self.pHand, self.cHand = self.giveCard(x.upper()[0], self.cHand, self.pHand, 'Player')

                system('cls')

            else:

                self.pPoints = self.findBooks(self.pHand, 'Player')
                x,self.pHand = self.findBooks(self.pHand)

                self.pHand, z = self.drawCard(self.pHand, 'Player', x)

                if not z:

                    break

        while True:

            y = randint(0, len(self.cHand) - 1)

            x = self.cHand[y]

            system('cls')

            if self.checkHand(x, 'CPU'):
                
                self.cHand, self.pHand = self.giveCard(x.upper()[0], self.pHand, self.cHand, 'CPU')

                system('cls')

            else:

                self.cPoints = self.findBooks(self.cHand, 'CPU')
                x,self.cHand = self.findBooks(self.cHand)

                self.cHand, z = self.drawCard(self.cHand, 'CPU', x)

                system('cls')

                if not z:

                    break
                     
    def play(self):

        self.shuffle()

        self.createHand(self.pHand)
        self.createHand(self.cHand)

        while self.__isGameOver():

            self.sort(self.pHand)
            self.sort(self.cHand)
            
            self.newTurn()
            
def main():

    game = Game()
    game.play()

if __name__ == '__main__':

    main()
