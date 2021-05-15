from cards.card import Card
class Wild(Card):
    def __init__(self):
        super().__init__("wild", "card")

    def onPlay(self, game):
        colors = "red, green, blue, yellow"
        print("Please provide a valid color ({}) for the next card to be: ".format(colors))
        selected = False
        while not selected:
            color = input().lower()
            if colors.find(color) != -1:
                card = Card(color, 100)
                game.topCard = card
                print("Next card color will be: {}".format(color))
                selected = True
            else:
                print("Invalid color!")
