import unittest
from Player import Player
from Deck import Deck
from Table import Table


class testHitOrStand(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    """
    Test tests the hit or stand function to see if the correct input returns True
    :return: Returns true because Y is correct value
    """
    def test_hitorstand__correctUpper_True(self):
        self.assertTrue(self.player.hit_or_stand("Y"))

    """
    Test tests the hit or stand function edge case where user enters lower case correct value
    :return: Returns true because n is correct value in lower case
    """
    def test_hitorstand__correctLower_True(self):
        self.assertFalse(self.player.hit_or_stand("n"))

    """
    Test tests the hit or stand function to see if the incorrect input returns False
    :return: Returns false because a is not a desrired value
    """
    def test_hitorstand__correctValue_False(self):
        self.assertFalse(self.player.hit_or_stand("a"))

    """
    Test tests the hit or stand edge case where string contains correct value
    :return: Returns false because it is a string
    """
    def test_hitorstand__string__True(self):
        self.assertFalse(self.player.hit_or_stand("YA"))


class testDealCard(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck2 = Deck()

    """
    Test that the deck pops out one card from the stack when called
    return: Returns a deck that contains one less card from the original deck
    """
    def test_deal_card_size_oneless(self):
        self.deck.deal_card()
        self.assertEqual(len(self.deck.stack) + 1, len(self.deck2.stack))

    """
    Test that the deck pops out one card from the stack when called
    return: Returns a deck that contains one less card from the original deck
    """
    def test_deal_card_return_valueNonNull(self):
        test = self.deck.deal_card()
        self.assertNotEqual(test, None)

    """
    Test that the deck pops out two cards from the stack when called
    return: Returns a deck that contains two less card from the original deck
    """
    def test_deal_card_twice_size_twoless(self):
        self.deck.deal_card()
        self.deck.deal_card()
        self.assertEqual(len(self.deck.stack) + 2, len(self.deck2.stack))

    """
    Test that the deck pops out two cards from the stack when called even when it is shuffled
    return: Returns a deck that contains two less card from the original deck
    """
    def test_deal_card_twice_suffle_size_twoless(self):
        self.deck.deal_card()
        self.deck.shuffle()
        self.deck.deal_card()
        self.assertEqual(len(self.deck.stack) + 2, len(self.deck2.stack))


class testShuffle(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.deck2 = Deck()

    """
    Tests that the shuffle mixes up the deck so it is not same as original
    return: Return a deck that is shuffled and not equal to original deck
    """
    def test_shuffle_different_original(self):
        self.deck.shuffle()
        self.assertNotEqual(self.deck, self.deck2)

    """
    Tests that the shuffle twice works
    return: Return a deck that is shuffled and not equal to original deck
    """
    def test_shuffle_shuffle_different_original(self):
        self.deck.shuffle()
        self.deck.shuffle()
        self.assertNotEqual(self.deck, self.deck2)

    """
    Tests that the shuffle doesn't create the same shuffle everytime
    return: Return a two shuffled decks that are different from each other
    """
    def test_shuffle_two_decks_not_same(self):
        self.deck.shuffle()
        self.deck2.shuffle()
        self.assertNotEqual(self.deck, self.deck2)


class test_hit_card(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    """
    Test that the deck pops out one card from the stack when called
    return: Returns a deck that contains one less card from the original deck
    """

    def test_hit_card_size_oneless(self):
        orignallen = len(self.table.deck.stack)
        self.table.deck.deal_card()
        self.assertEqual(len(self.table.deck.stack) + 1, orignallen)

    """
    Test that the deck pops out two cards from the stack when called
    return: Returns a deck that contains two less card from the original deck
    """

    def test_hit_card_twice_size_twoless(self):
        orignallen = len(self.table.deck.stack)
        self.table.deck.deal_card()
        self.table.deck.deal_card()
        self.assertEqual(len(self.table.deck.stack) + 2, orignallen)

    """
    Test that the deck pops out two cards from the stack when called even when it is shuffled
    return: Returns a deck that contains two less card from the original deck
    """

    def test_hit_card_twice_suffle_size_twoless(self):
        orignallen = len(self.table.deck.stack)
        self.table.deck.deal_card()
        self.table.deck.shuffle()
        self.table.deck.deal_card()
        self.assertEqual(len(self.table.deck.stack) + 2, orignallen)


class test_DealCards(unittest.TestCase):

    def setUp(self):
        self.table = Table()

    """
    Tests that the player gets two cards
    return: should return a player with hand of size two
    """
    def test_deal_cards_player_size_2(self):
        self.table.deal_cards()
        self.assertEqual(len(self.table.player.hand), 2)

    """
    Tests that the dealer only gets 1 cards
    return: should return a player with hand of size 1
    """
    def test_deal_cards_dealer_size_1(self):
        self.table.deal_cards()
        self.assertEqual(len(self.table.dealer.hand), 1)

    """
    Tests that the player gets cards and the score is calculated
    return: should return a score that is greater then 1
    """
    def test_deal_cards_player_score_not_1(self):
        self.table.deal_cards()
        self.table.hand_total(self.table.player)
        self.assertGreater(self.table.player.score, 1)

    """
    Tests that the dealer gets a card and the score is calculated
    return: should return a score that is greater then 0
    """
    def test_deal_cards_dealer_score_not_10(self):
        self.table.deal_cards()
        self.table.hand_total(self.table.dealer)
        self.assertGreater(self.table.dealer.score, 0)


if __name__ == '__main__':
    unittest.main()
