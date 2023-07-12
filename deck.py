from terminal_playing_cards import Card, View
from itertools import product


class Desk:
    def __init__(self):
        self.desk = self.generate_deck()


    suits = ("hearts", "spades", "diamonds", "clubs")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def generate_deck(self):
        cards = []
        points = 0
        for suit, rank in product(self.suits, self.ranks):
            if rank.isdigit():
                points = int(rank)
            elif rank in "JQK":
                points = 10
            elif rank == "A":
                points = 11
            card = Card(rank, suit, value=points, hidden=False, picture=True)
            cards.append(card)
        return View(cards)

    def get_card(self):
        card = [self.desk.pop()]
        return View(card)



ob = Desk()
print(View(ob.desk[:1]))
print(ob.get_card())
