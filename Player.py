from Dealer import Dealer


class Player(Dealer):

    def __init__(self):
        super().__init__()
        self.name = "Player"

    @staticmethod
    def hit_or_stand(choice):

        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Incorrect Input -- Default No Hit")
            return False
