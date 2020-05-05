from Table import Table


def main():

    table = Table()
    table.deal_cards()
    table.hand_total(table.player)
    table.hand_total(table.dealer)
    table.play_game()


if __name__ == '__main__':

    main()

# Test Commit 8
