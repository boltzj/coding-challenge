from time import time
import array
import cProfile


class Game():
    deck = list()
    original_deck = list()
    nb_round = 0

    def __init__(self, size_of_deck):
        self.deck = list(range(1, size_of_deck + 1))
        self.table = list(range(1, size_of_deck + 1))

        table_deck = list()
        deck = list(range(1, len(self.deck) + 1))

        while len(deck):
            # Step a : Take the top card off the deck and set it on the table
            table_deck.append(deck.pop())

            if len(deck):
                deck.insert(0, deck.pop())

        for x in range(0, size_of_deck):
            self.table[x] = table_deck[x]

    def do_round(self):
        # Table will be the new deck at the end of the round
        new_deck = list(range(1, len(self.deck)))

        for x in range(0, len(self.deck)):
            i = self.table[x]
            new_deck[i] = 0#self.deck[x]

        self.deck = new_deck
        self.nb_round += 1


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
    game = Game(200)

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

# cProfile.run('run()')
run()