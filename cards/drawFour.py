from cards.card import Card
class DrawFour(Card):
    def __init__(self):
        super().__init__("Wild", "Four")

    def onPlay(self, game):

        game.movePosition()
        player = game.players[game.position]
        card1 = game.cards[1]
        card2 = game.cards[2]
        card3 = game.cards[3]
        card4 = game.cards[4]
        player.addCard(card1)
        player.addCard(card2)
        player.addCard(card3)
        player.addCard(card4)
        game.cards.remove(card1)
        game.cards.remove(card2)
        game.cards.remove(card3)
        game.cards.remove(card4)
        print("{} picked up 4 cards!\n".format(player.getName()))

        colors = "red, green, blue, yellow"
        print("Please provide a valid color ({}) for the next card to be: ".format(colors))
        selected = False
        while not selected:
            color = input().lower()
            if colors.find(color) != -1:
                card = Card(color, 100)
                game.topCard = card
                selected = True
            else:
                print("Invalid color!")
