from time import time
import cProfile

class Game():
    deck = list()
    original_deck = list()
    nb_round = 0

    def __init__(self, size_of_deck):
        self.deck = list(range(1, size_of_deck + 1))
        self.original_deck = sorted(self.deck)

    def do_round(self):
        # Table will be the new deck at the end of the round
        table_deck = list()

        # Store deck size
        deck_size = len(self.deck)

        while len(self.deck):
            # Step a : Take the top card off the deck and set it on the table
            table_deck.append(self.deck.pop())

            if len(self.deck):
                self.deck.insert(0, self.deck.pop())

        self.deck = table_deck
        self.nb_round += 1

        # self.print_deck()

    def is_over(self):
        start = 1

        for card in self.deck:
            if card == start:
                start += 1
            else:
                return False
        return True

        # FIXME
        # return self.deck == sorted(self.deck)

    def print_deck(self):
        print(self.deck)

def run():

    # New Game
    game = Game(300)

    # Start First round
    start_time = time()
    i = 1
    game.do_round()

    # Try to go back to original deck
    while not game.is_over():
        game.do_round()
        i += 1
        # print(i)

    # Print Result
    end_time = time()
    print(i, '(computed in ', end_time - start_time, ')')

cProfile.run('run()')
# run()