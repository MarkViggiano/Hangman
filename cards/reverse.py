from cards.card import Card
class Reverse(Card):
    def __init__(self, color):
        super().__init__(color, "Reverse")

    def onPlay(self, game):
        game.clockWise = not game.clockWise
