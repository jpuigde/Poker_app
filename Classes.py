from random import choice, random
from names import get_first_name
from Objects import Deck

class HandlerChips:
    chips = 0
    active = False

    def add_chips(self, n) -> None:
        self.chips += n

    def set_chips(self, n: int) -> None:
        self.chips = n

    def subtract_chips(self, n: int) -> int:
        if self.chips >= n:
            self.chips -= n
        else:
            n = self.chips
            self.chips = 0
            self.active = False
        return n

    def __rshift__(self, tuple_n_other):
        n, other = tuple_n_other
        n = self.subtract_chips(n)
        other.add_chips(n)


class HandlerCards:
    cards = []
    number_of_cards = 0
    name = ""

    def show_card(self) -> list:
        return self.cards

    def count_card(self) -> int:
        self.number_of_cards = len(self.cards)
        return self.number_of_cards

    def add_cards(self, cards: list) -> int:
        self.cards = self.cards + cards
        return self.count_card()

    def __str__(self) -> str:
        return f'{self.name} : {self.show_card()}'

    def __repr__(self) -> str:
        return self.__str__()


class Discarded(HandlerCards):
    def __init__(self):
        self.name = "Discarded"

    def show_card(self):
        return self.count_card()


class TableCards(HandlerCards):
    def __init__(self):
        self.name = "Table Cards"


class Player(HandlerCards, HandlerChips):
    name = ""
    active = False
    identifier = -1

    def __init__(self, name, chips=0):
        self.name = name
        self.chips = chips
        self.active = True
        if name == "":
            self.name = get_first_name()
        if chips == 0:
            self.chips = random() * 100 // 1

    def set_id(self, identifier):
        self.identifier = identifier

    def __str__(self) -> str:
        return f'{self.name} : {self.chips} : {self.number_of_cards}'

    def __repr__(self) -> str:
        return self.__str__()


class TablePot(HandlerChips):
    chips = 0

    def __init__(self, players):
        self.players = players

    def subtract_player(self, player_id):
        self.players = [p for p in self.players if p.identifier != player_id]


class HandMatch:
    TablePots = []

    def __init__(self, positions=6):
        self.positions = positions
        self.players = {i: None for i in range(positions)}
        self.deck = Deck()
        self.discarded = Discarded()
        self.TableCards = TableCards()

    def get_active_players(self):
        return [p for p in self.players if p.active]

    def add_pot(self):
        self.TablePots = self.TablePots + [TablePot(self.get_active_players)]

    def __str__(self):
        return f'{self.players} \n' \
               f'{self.TableCards} \n' \
               f'{self.deck} \n' \
               f'{self.discarded}'

    def __repr__(self):
        return self.__str__()

    def __lshift__(self, player):
        resp = self.add_player(player)
        return resp

    def get_empty_sits(self):
        empty_sits = [empty_sit for empty_sit in self.players if not self.players[empty_sit]]
        return empty_sits

    def sits_left(self):
        sits_left = len(self.get_empty_sits())
        return sits_left

    def add_player(self, player):
        empty_sits = self.get_empty_sits()
        if len(empty_sits) == 0:
            print("No empty spaces")
            sit_number = -1
        else:
            sit_number = choice(empty_sits)
            self.players[sit_number] = player
            player.set_id(sit_number)
        return sit_number

class Match:
    table