from time import time
import cProfile


class Game():
    def __init__(self, size_of_deck):
        self.deck = list(range(0, size_of_deck))
        self.shuffle_table = list(range(0, size_of_deck))
        self.round = 0

        table_deck = list()
        deck = list(range(0, len(self.deck)))

        while len(deck):
            # Step 1 : Take the top card off the deck and set it on the table
            table_deck.append(deck.pop())

            if len(deck):
                # Step 2 : Take the next card off the top of desk and put it on the bottom of the deck in your hand.
                deck.insert(0, deck.pop())

        for x in range(0, size_of_deck):
            self.shuffle_table[x] = table_deck[x]

    def do_round(self):

        # This deck will be the new deck at the end of the round
        table_deck = list(range(0, len(self.deck)))

        # Use the shuffle table to make the new deck
        for x in range(0, len(self.deck)):
            table_deck[self.shuffle_table[x]] = self.deck[x]

        # Set the new deck
        self.deck = table_deck
        self.round += 1

    def is_over(self):
        start = 0

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
    game = Game(313)

    # Start First round
    start_time = time()
    game.do_round()

    # Try to go back to original deck
    while not game.is_over():
        game.do_round()

    # Print Result
    end_time = time()
    print(game.round, '(computed in ', end_time - start_time, ')')

# cProfile.run('run()')
run()