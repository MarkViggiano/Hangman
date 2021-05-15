from cards.card import Card
from cards.wild import Wild

class DrawFour(Card):
    def __init__(self):
        super().__init__("Wild", "Four")

    def onPlay(self, game):

        game.movePosition()
        player = game.players[game.position]
        cardLength = len(game.cards)

        if cardLength == 0:
            print("There are no cards to draw! Skipping {} instead...".format(player.getName()))
            return

        limit = 4
        count = 0
        for card in game.cards:
            if card == game.topCard:
                continue

            if count >= limit:
                break

            player.addCard(card)
            game.cards.remove(card)
            count += 1

        print("{} picked up {} cards!\n".format(player.getName(), count))
        Wild().onPlay(game)
