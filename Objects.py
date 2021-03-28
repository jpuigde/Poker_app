from itertools import product
from random import shuffle


class Card:
    def __str__(self):
        sting_number = {1: "A", 11: "J", 12: "Q", 13: "K"}
        sting_suits = {'C': "♣", 'D': "♦", 'H': "♥", 'S': "♠"}

        printable_number = sting_number.get(self.number, self.number)
        printable_suit = sting_suits.get(self.suit, self.suit)

        return str(printable_number) + printable_suit

    def __eq__(self, other):
        return (self.number == other.number) & (self.suit == other.suit)

    def __ge__(self, other):
        return (self.number == 1) | self.number >= other.number

    def __gt__(self, other):
        return (self.number == 1 & other.number != 1) | self.number > other.number

    def __le__(self, other):
        return (other.number == 1) | self.number <= other.number

    def __lt__(self, other):
        return (other.number == 1 & self.number != 1) | self.number < other.number

    def __repr__(self):
        return self.__str__()

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit


class Deck:

    def __init__(self) -> None:
        self.number_of_cards = 0
        numbers = range(1, 14)
        colours = ['C', 'D', 'H', 'S']
        self.cards = [Card(e1, e2) for e1, e2 in product(numbers, colours)]
        self.count_card()

    def count_card(self):
        self.number_of_cards = len(self.cards)
        return self.number_of_cards

    def shuffle_deck(self) -> None:
        numbers = range(1, 14)
        colours = ['H', 'R', 'T', 'S']
        self.cards = [Card(e1, e2) for e1, e2 in product(numbers, colours)]
        self.number_of_cards = len(self.cards)
        shuffle(self.cards)

    def __str__(self):
        return f'Deck with {self.count_card()} cards'

    def __repr__(self):
        return self.__str__()

    def draw_cards(self, n):
        cards_to_give = self.cards[:n]
        self.cards = self.cards[n:]
        self.count_card()
        return cards_to_give

    def __rshift__(self, handler):
        card = self.draw_cards(1)
        handler.add_cards(card)
        return f'One card for {handler.name}'
