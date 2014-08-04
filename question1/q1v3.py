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
        self.round = 0

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
        # If compute had been already been called, reinitialize round count
        if self.round == 0:

            # Two decks to use alternatively
            decks = [list(self.deck), list(self.deck)]

            # Shuffle card until going back to original deck
            while True:

                new_deck = decks[self.round % 2]
                
                # Use the shuffle table to make the new deck
                for x in self.deck:
                    new_deck[self.shuffle_table[x]] = self.deck[x]

                # Set the new deck
                self.deck = new_deck
                self.round += 1

                if self.is_over():
                    break

        # Return the number of round to come back to the original order
        return self.round

    def is_over(self):
        """
        :return: Return true if the game deck is at initial status, False otherwise
        """
        # First card value (We assumed that first card value is 0)
        expected_value = 0

        # Iterate on card value
        for card in self.deck:
            if card == expected_value:
                # Increment expected value and continue
                expected_value += 1
            else:
                # Deck is not as the initial status
                return False
        # Deck is at the initial status
        return True

    def print_deck(self):
        print(self.deck)


def run(size_of_deck):
    # Record start time
    start_time = time()

    # New Game
    game = Game(size_of_deck)

    # Compute the number of rounds
    rounds = game.compute()

    # Print Result
    end_time = time()
    print(rounds, '(computed in ', end_time - start_time, ')')
    # print(end_time - start_time)

run(290)