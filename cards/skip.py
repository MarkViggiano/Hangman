from cards.card import Card
class Skip(Card):
    def __init__(self, color):
        super().__init__(color, "Skip")

    def onPlay(self, game):
        game.movePosition() #only move one because we also move one after calling this method
        print("Skipped the next person!")
