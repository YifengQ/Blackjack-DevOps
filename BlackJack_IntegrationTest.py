import unittest
from Player import Player
from Deck import Deck
from Table import Table
from Dealer import Dealer


class testPlayerGetsCards(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        self.player = Player()

    """
    Tests that the table will call the deck class to get a card to update the player class
    return: Return a player with a card updated from deck
    """

    def test_deal_cards_player_size_2(self):
        self.table.deal_cards()

        self.table.hit_card(self.table.player)
        self.assertEqual(len(self.table.player.hand), 3)


class testDealerGetsCards(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        self.dealer = Dealer()

    """
    Tests that the table will call the deck class to get a card to update the dealer class
    return: Return a dealer with a card updated from deck
    """

    def test_deal_cards_dealer_size_2(self):
        self.table.deal_cards()
        self.assertEqual(len(self.table.dealer.hand), 1)

    """
    Tests that the the table class will get a card from the deck class and give it to the player class
    This is called when the dealer has a hand less than 16
    return: Return a player with a card updated from deck
    """
    def test_table_calls_getCard_updateDealer(self):
        self.table.hit_card(self.dealer)
        self.assertEqual(len(self.dealer.hand), 1)


class testPlayerDealerScoreUpdate(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        self.dealer = Dealer()
        self.player = Player()

    """
    Tests that when the player is updated with a card from deck the player score is updated
    return: should return a score that is greater then 1
    """
    def test_deal_cards_player_score_not_1(self):
        self.table.deal_cards()
        self.table.hand_total(self.table.player)
        self.assertGreater(self.table.player.score, 1)

    """
    Tests that when the player is updated with a card from deck the player score is updated
    return: should return a score that is greater then 0
    """

    def test_deal_cards_dealer_score_not_0(self):
        self.table.deal_cards()
        self.table.hand_total(self.table.dealer)
        self.assertGreater(self.table.dealer.score, 0)


class testDeckSizeShange(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    """
    Test that the deck pops out the 3 cards dealt from the stack when called
    Makes sure that the table manipulates the deck class by popping out a card from deck class
    return: Returns a deck that contains one less card from the original deck
    """
    def test_TableDeckPopSizeLess(self):
        origlen = len(self.table.deck.stack)
        self.table.deal_cards()
        self.assertEqual(len(self.table.deck.stack) + 3, origlen)

    """
    Test that the deck pops out three cards from the stack when called
    Makes sure that the table manipulates the deck class by popping out a card from deck class
    return: Returns a deck that contains one less card from the original deck
    """

    def test_TableDeckPopSize2Less(self):
        origlen = len(self.table.deck.stack)
        self.table.deal_cards()
        self.assertEqual(len(self.table.deck.stack) + 3, origlen)

    """
    Test that the deck pops out one card from the stack when called
    Makes sure that the table manipulates the deck class by popping out a card from deck class
    return: Returns a deck that contains one less card from the original deck
    """

    def test_TableDeckHitPopSizeLess(self):
        origlen = len(self.table.deck.stack)
        self.table.hit_card(self.table.player)
        self.assertEqual(len(self.table.deck.stack) + 1, origlen)


class testShuffle(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck2 = Deck()

    """
    Makes sure the table class manipulates the deck class to shuffle the deck
    return: Return a deck that is shuffled and not equal to original deck
    """
    def test_shuffle__deck_diff(self):
        self.deck.shuffle()
        self.assertNotEqual(self.deck, self.deck2)

    """
    Makes sure the table class manipulates the deck class to shuffle the deck
    return: Return a deck that is shuffled and not equal to original deck
    """
    def test_shuffle_shuffle_different_original(self):
        self.deck.shuffle()
        self.deck.shuffle()
        self.assertNotEqual(self.deck, self.deck2)

    """
    Tests that the shuffle doesn't create the same shuffle everytime
    Makes sure the table class manipulates the deck class to shuffle the deck
    return: Return a two shuffled decks that are different from each other
    """
    def test_shuffle_two_decks_not_same(self):
        self.deck.shuffle()
        self.deck2.shuffle()
        self.assertNotEqual(self.deck, self.deck2)


if __name__ == '__main__':
    unittest.main()
#Test