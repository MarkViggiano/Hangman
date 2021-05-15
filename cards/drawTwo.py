from cards.card import Card
import time
class DrawTwo(Card):
    def __init__(self, color):
        super().__init__(color, "Draw Two")

    def onPlay(self, game):
        game.movePosition()
        player = game.players[game.position]
        #assuming the card that was on the table is 0
        card1 = game.cards[1]
        card2 = game.cards[2]
        player.addCard(card1)
        player.addCard(card2)
        game.cards.remove(card1)
        game.cards.remove(card2)
        print("{} just picked up 2 cards!".format(player.getName()))
        #No need to move again or clear console because it happens right after this method call
