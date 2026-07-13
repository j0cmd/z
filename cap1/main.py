# Exemplo 1: um baralho como uma sequencia de cartas
#

import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "espada copas ouro paus".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()  # instancia de FrenchDeck
beer_card = Card("7", "paus")
print(beer_card)
print(f"O baralho tem {len(deck)} cartas")
print(deck[:3])  # usando fatiamento
print(choice(deck))  # usnado uma função aleatoria

# for carta in sorted(deck):  # iterar cartas e ordenar com sorted
#   print(carta)
# comitando no celular
