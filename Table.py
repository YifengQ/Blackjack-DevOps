from Dealer import Dealer
from Player import Player
from Deck import Deck


class Table(object):

    def __init__(self):

        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()

    def hit_card(self, player):

        card = self.deck.deal_card()
        player.hand.append(card)

    def deal_cards(self):

        self.deck.shuffle()

        self.hit_card(self.player)
        self.hit_card(self.dealer)
        self.hit_card(self.player)
        # self.hand_total(self.player)
        # self.hand_total(self.dealer)

    def dealer_hit(self):

        score = self.dealer.score
        while True:
            if score < 17:
                self.hit_card(self.dealer)
                self.hand_total(self.dealer)
                print(self)
            elif score >= 17:
                self.find_winner()

    def hand_total(self, player):

        has_ace = False
        score = 0
        for card in player.hand:
            if card[1] == 1 and not has_ace:
                card = ('A', 11)
                has_ace = True
            score += card[1]

        player.score = score

        if player.score > 21 and has_ace:
            player.score -= 10
            score = player.score
        self.check_win(score, player)
        return

    def check_win(self, score, player):
        if score > 21:
            print()
            print(self)
            print("Bust!!! -- " + str(player.name) + " Loses")
            self.end_game()
        elif score == 21:
            print(self)
            print("Blackjack!!! -- " + str(player.name) + " Wins")
            self.end_game()
        else:
            return

    def find_winner(self):

        if self.dealer.score > self.player.score:
            print("Dealer wins!")
            self.end_game()
        else:
            print("You Win")
            self.end_game()

    def end_game(self):
        again = input("Play Again? (Y/N)? ")
        if again.lower() == 'y':
            self.__init__()
        elif again.lower() == 'n':
            exit()

    def play_game(self):

        while True:
            print()
            print(self)
            choice = input("Do you want to Hit (Y/N)? ")
            player_move = self.player.hit_or_stand(choice)
            if player_move is True:
                self.hit_card(self.player)
                self.hand_total(self.player)
            elif player_move is False:
                self.dealer_hit()
                self.hand_total(self.dealer)

    def __str__(self):

        dealer_hand = [card for card, value in self.dealer.hand]
        player_hand = [card for card, value in self.player.hand]

        print("Dealer's Hand : " + str(dealer_hand))
        print("Dealer's Score : " + str(self.dealer.score) + "\n")
        print("Player's Hand" + str(player_hand) + "\n")
        print("Player's Score :" + str(self.player.score) + "\n")
        print("=" * 40)
        return ''
