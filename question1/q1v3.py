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
        self.deck = list(range(size_of_deck))
        self.shuffle_table = list(range(size_of_deck))

        table_deck = list()
        deck = list(range(size_of_deck))

        # Compute the lookup table
        while deck:
            # Step 1 : Take the top card off the deck and set it on the table
            table_deck.append(deck.pop())

            if deck:
                # Step 2 : Take the next card off the top of desk and put it on the bottom of the deck in your hand.
                deck.insert(0, deck.pop())

        # Store the position of the card after one round as the lookup table
        for x in range(size_of_deck):
            self.shuffle_table[x] = table_deck[x]

    def compute(self):
        """
        :return: Return the number of round to come back to the initial deck
        """
        # Two decks to use alternatively
        decks = [list(self.deck), list(self.deck)]
        round = 0

        # Shuffle card until going back to original deck
        while True:
            # Select decks
            deck = decks[(round + 1) % 2]
            new_deck = decks[round % 2]

            # Use the shuffle table to make the new deck
            for x in deck:
                new_deck[self.shuffle_table[x]] = deck[x]

            round += 1

            if self.is_over(new_deck):
                break

        # Return the number of round to come back to the original order
        return round

    @staticmethod
    def is_over(deck):
        """
        :return: Return true if the game deck is at initial status, False otherwise
        """
        # First card value (We assumed that first card value is 0)
        expected_value = 0

        # Iterate on card value
        for card in deck:
            if card == expected_value:
                # Increment expected value and continue
                expected_value += 1
            else:
                # Deck is not as the initial status
                return False
        # Deck is at the initial status
        return True


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