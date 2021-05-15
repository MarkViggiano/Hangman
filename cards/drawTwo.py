from cards.card import Card
import time
class DrawTwo(Card):
    def __init__(self, color):
        super().__init__(color, "Draw Two")

    def onPlay(self, game):
        game.movePosition()
        player = game.players[game.position]
        cardLength = len(game.cards)

        if cardLength == 0:
            print("There are no cards to draw! Skipping {} instead...".format(player.getName()))
            return

        if cardLength == 1:
            card = game.getNextSelectedCard()
            player.addCard(card)
            game.cards.remove(card)
            print("{} just picked up 1 card!".format(player.getName()))
            return

        card1 = game.getNextSelectedCard()
        game.cards.remove(card1)

        card2 = game.getNextSelectedCard()
        game.cards.remove(card2)

        player.addCard(card1)
        player.addCard(card2)
        print("{} just picked up 2 cards!".format(player.getName()))
        #No need to move again or clear console because it happens right after this method call
