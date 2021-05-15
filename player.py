class Player:
    def __init__(self, name):
        self.name = name;
        self.deck = [];

    def getName(self):
        return self.name

    def addCard(self, card):
        self.deck.append(card)

    def removeCard(self, card):
        self.deck.remove(card)

    def getDeck(self):
        return self.deck

    def printDeck(self):
        deckDashes = ""
        deckData = ""
        cardNumberData = ""
        cardNumber = 0
        for card in self.getDeck():
            cardData = "{0} {1}".format(card.color, card.id)
            dashLength = len(cardData)
            spacedDashLength = dashLength - 1
            deckData += "| {} |".format(cardData)
            deckDashes += "| {} |".format("-" * dashLength)
            cardNumberData += "| {0}{1} |".format(cardNumber, " " * spacedDashLength)
            cardNumber += 1

        print(deckDashes)
        print(deckData)
        print(deckDashes)
        print(deckDashes)
        print(cardNumberData)
        print(deckDashes)
