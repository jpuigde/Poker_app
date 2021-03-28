from Classes import Player, TableCards, Discarded
from Objects import Deck, Card
import unittest


class TestCards(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()
        self.card = Card('A', 'C')

    def test_setUp(self):
        self.assertEqual(self.deck.number_of_cards, 52)

    def test_setUp(self):
        cards = self.deck.draw_cards(3)
        self.assertEqual(self.deck.number_of_cards, 49)
        self.assertEqual(len(cards), 3)


class TestHandler(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("player1", 111)
        self.player2 = Player("player2", 222)
        self.card = Card('A', 'C')

    def test_setUp(self):
        self.player1.set_chips(111)
        self.assertEqual(self.player1.name, "player1")
        self.assertEqual(self.player1.chips, 111)
        self.assertEqual(self.player1.cards, [])
        self.assertTrue(self.player1.active)
        self.assertEqual(self.player1.number_of_cards, 0)

    def test_add_chips(self):
        self.player1.set_chips(100)
        self.assertEqual(self.player1.chips, 100)
        self.player1.add_chips(111)
        self.assertEqual(self.player1.chips, 211)

    def test_subtract_chips(self):
        self.player1.set_chips(100)
        self.assertEqual(self.player1.subtract_chips(10), 10)
        self.assertEqual(self.player1.chips, 90)
        self.assertEqual(self.player1.subtract_chips(100), 90)
        self.assertEqual(self.player1.chips, 0)

    def test_transfer_chips(self):
        self.player1.set_chips(111)
        self.player2.set_chips(222)
        self.player1 >> (10, self.player1)
        self.assertEqual(self.player1.chips, 111)
        self.player1 >> (10, self.player2)
        self.assertEqual(self.player1.chips, 101)
        self.assertEqual(self.player2.chips, 232)
        self.player2 >> (300, self.player1)
        self.assertEqual(self.player1.chips, 333)
        self.assertEqual(self.player2.chips, 0)
        self.assertFalse(self.player2.active)

    def test_add_card(self):
        self.assertEqual(self.player1.number_of_cards, 0)
        self.assertEqual(self.player1.add_cards([self.card]), 1)
        self.assertEqual(self.player1.number_of_cards, 1)

class TestShareCards(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("player1", 111)
        self.Discarded = Discarded()
        self.TableCards = TableCards()
        self.deck = Deck()

    def test_give_card(self):
        self.assertEqual(self.player1.number_of_cards, 0)
        self.deck >> self.player1
        self.deck >> self.TableCards
        self.deck >> self.Discarded
        self.deck >> self.Discarded
        self.assertEqual(self.deck.number_of_cards, 48)
        self.assertEqual(self.player1.number_of_cards, 1)
        self.assertEqual(self.TableCards.number_of_cards, 1)
        self.assertEqual(self.Discarded.number_of_cards, 2)
        self.deck >> self.player1
        self.assertEqual(self.Discarded.show_card(), 2)
        self.assertEqual(self.TableCards.show_card(), [Card(1, 'D')])
        self.assertEqual(self.player1.show_card(), [Card(1, 'C'), Card(2, 'C')])



if __name__ == '__main__':
    unittest.main(verbosity=1)

