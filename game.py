from player import Player
from cards.card import Card
from cards.drawTwo import DrawTwo
from cards.reverse import Reverse
from cards.skip import Skip
from cards.wild import Wild
from cards.drawFour import DrawFour
import random
import time

class Game():

    def __init__(self):
        self.players = []
        self.cards = []
        self.topCard = None
        self.position = 0
        self.clockWise = True
        self.activePlayer = None
        self.playerCardCount = 7
        self.winner = None
        self.second = None
        self.third = None

    def registerPlayers(self):
        ready = False
        print("Enter player names to play, when your finished type: 'play':")
        while not ready:
            name = input()
            if len(name) == 0:
                print("Type a name of a player to add or type 'play' to play!")
                continue
            if (name.lower() == "play"):
                for player in self.players:
                    print("Registered Player: {}".format(player.getName()))
                ready = True
            else:
                player = Player(name)
                self.players.append(player)

        self.playGame()

    def printPodium(self):
        print("1st: {}".format(self.winner))
        print("2nd: {}".format(self.second))
        print("3rd: {}".format(self.third))

    def countdown(self):
        print(5)
        time.sleep(1)
        print(4)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)

    def clearConsole(self):
        print("\n" * 100) #IDLE has no good way of clearing console

    def start(self):
        print("Starting Uno!")
        self.registerPlayers()

    def printTopCard(self):
        topCardData = "{0} {1}".format(self.topCard.color, self.topCard.id)
        dashes = "-" * len(topCardData)
        print("TOP CARD: ")
        print("| {} |".format(dashes))
        print("| {} |".format(topCardData))
        print("| {} |".format(dashes))

    def movePosition(self, amount = 1): #no value for 1 move
        playerAmount = len(self.players) - 1
        if self.clockWise:
            if self.position + amount > playerAmount:
                self.position = 0
                return
            self.position += amount
            return

        if self.position - amount < 0:
            self.position = playerAmount
            return

        self.position -= amount

    def createDecks(self):
        colors = ["red", "green", "blue", "yellow"]

        wildCount = 0
        wildAmount = 4
        while wildCount < wildAmount:
            self.cards.append(Wild())
            self.cards.append(DrawFour())
            wildCount += 1

        for color in colors:
            count = 0
            while count <= 9:
                self.cards.append(Card(color, count))

                if count == 9:
                    self.cards.append(DrawTwo(color))
                    self.cards.append(Reverse(color))
                    self.cards.append(Skip(color))

                count += 1

        random.shuffle(self.cards)
        cardCount = 0
        while cardCount < self.playerCardCount:
            for player in self.players:
                card = self.cards[cardCount]
                player.addCard(card)
                self.cards.remove(card)

            cardCount += 1

    def getNextSelectedCard(self):
        if self.cards[0] == self.topCard:
            return self.cards[1]

        return self.cards[0]

    def playGame(self):
        self.clearConsole()
        print("Creating decks...")
        self.createDecks()
        self.topCard = self.cards[0]
        self.activePlayer = self.players[self.position]
        if (self.topCard.color.lower() == "wild"):
            if (self.topCard.id.lower() == "four"):
                self.movePosition(-1)
            self.topCard.onPlay(self)

        while len(self.players) > 1:
            if self.winner is not None and self.second is not None and self.third is not None:
                break
            self.activePlayer = self.players[self.position]
            print("It is {}'s turn in: ".format(self.activePlayer.getName()))
            self.countdown()

            print("Players with uno:")
            for player in self.players:
                if len(player.getDeck()) == 1:
                    print(" - " + player.getName())
            print("\n")

            command = "draw"
            if len(self.cards) == 0:
                command = "skip"

            self.printTopCard()
            print("\n" * 2)
            print("Your Deck:")
            self.activePlayer.printDeck()

            cardSelected = False
            print("Enter the number of the card you want to play! Or '{0}' if you want to {0}!".format(command))
            while not cardSelected:
                cardNumber = input()
                if cardNumber.lower() == "draw":
                    if len(self.cards) < 1:
                        print("You cannot draw right now!") #prevent cheaters :)
                    else:
                        card = self.getNextSelectedCard()
                        self.activePlayer.addCard(card)
                        self.cards.remove(card)
                        self.clearConsole()
                        self.printTopCard()
                        print("\n" * 2)
                        self.activePlayer.printDeck()
                        print("Enter the number of the card you want to play! Or '{0}' if you want to {0}!".format(command))

                elif cardNumber.lower() == "skip":
                    if len(self.cards) > 1:
                        print("You cannot skip right now!") #prevent cheaters :)
                    else:
                        self.movePosition() #just move to the next person
                        cardSelected = True

                else:
                    if int(cardNumber) > len(self.activePlayer.getDeck()) - 1:
                        print("Invalid card! Try again!")
                        continue
                    card = self.activePlayer.getDeck()[int(cardNumber)]
                    if card.color.lower() == "wild" or card.color.lower() == self.topCard.color.lower() or card.id == self.topCard.id:
                        print("{0} has played: {1} {2}".format(self.activePlayer.getName(), card.color.title(), card.id))
                        self.topCard = card
                        self.activePlayer.removeCard(card)
                        card.onPlay(self)
                        self.movePosition()
                        time.sleep(5)
                        self.clearConsole()
                        if len(self.activePlayer.getDeck()) == 0:
                            if self.winner == None:
                                print("WE HAVE A WINNER:")
                                print(self.activePlayer.getName())
                                self.winner = self.activePlayer.getName()
                                self.players.remove(self.activePlayer)
                                if len(self.players) == 1:
                                    self.second = self.players[0]
                                    self.third = "N/A"
                                    self.players.pop(0)
                                    break
                                print("\n\nKeep playing for second and third place!")
                                time.sleep(5)
                            if self.second == None:
                                print("SECOND PLACE:")
                                print(self.activePlayer.getName())
                                self.second = self.activePlayer.getName()
                                self.players.remove(self.activePlayer)
                                if len(self.players) == 1:
                                    self.third = self.players[0]
                                    self.players.pop(0)
                                    break
                                print("\n\nKeep playing for third place!")
                                time.sleep(5)
                            if self.third == None:
                                print("THIRD PLACE:")
                                print(self.activePlayer.getName())
                                self.third = self.activePlayer.getName()
                                self.players.remove(self.activePlayer)
                                time.sleep(5)
                        cardSelected = True
                    else:
                        print("Invalid card! Try again!")

        self.clearConsole()
        self.printPodium()
