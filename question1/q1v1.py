#!/usr/bin/python

__author__ = 'boltz_j'

import sys
from time import time


class Game():
    def __init__(self, size_of_deck):
        """
        At the creation of the game, we init a lookup table (shuffle_table)
        to precalculate the distribution of card for a round
        :param size_of_deck: Number of cards in the deck (MUST BE POSITIVE)
        :return:
        """
        self.deck = list(range(1, size_of_deck + 1))
        self.round = 0

    def compute(self):
        """
        Execute rounds until going back to initial deck
        :return: Return the number of round to come back to the initial deck
        """
        # Start first round
        self.do_round()

        # Try to go back to original deck
        while not self.is_over():
            self.do_round()

        return self.round

    def do_round(self):
        """
        do_round() do one shuffle round on the deck
        :return:
        """
        # Table will be the new deck at the end of the round
        table_deck = list()

        while self.deck:
            # Step a : Take the top card off the deck and set it on the table
            table_deck.append(self.deck.pop())

            if self.deck:
                self.deck.insert(0, self.deck.pop())

        self.deck = table_deck
        self.round += 1

    def is_over(self):
        """
        :return: Return true if the game deck is at initial status, False otherwise
        """
        start = 1

        for card in self.deck:
            if card == start:
                start += 1
            else:
                return False
        return True

    def print_deck(self):
        print(self.deck)


def main(argv):
    if not argv[0]:
        sys.exit(1)

    try:
        size_of_deck = int(argv[0])
    except ValueError:
        print('Error:', argv[0], 'is not a valid input')
        sys.exit(1)

    # New Game
    game = Game(size_of_deck)

    # Get start time
    start_time = time()

    # Find the solution
    rounds = game.compute()

    # Print Result
    end_time = time()
    print(rounds, 'rounds (computed in ', end_time - start_time, ')')

    sys.exit(0)

if __name__ == "__main__":
   main(sys.argv[1:])