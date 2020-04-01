"""
File: cards.py
Author: Darren Strash + Class!
Make playing card class for blackjack.
"""

import random

#Rank
RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
#Suit
SUITS = ["D", "C", "S", "H"]

class PlayingCard:
    """Represents a single playing card from a standard deck."""

    def __init__(self, rank, suit):
        """Constructor for PlayingCard class."""
        self._rank = rank
        self._suit = suit

    def __str__(self):
        """Returns a string representation of the playing card.
        NOTE: Never print anything in __str__"""
        return str(self._rank) + self._suit

    def __repr__(self):
        """Very similar to __str__ method, except it gives a
        "computer readable" version of this object."""
        return self.__str__()

    def get_rank(self):
        """Return rank of this card."""
        return self._rank

    def get_suit(self):
        """Return the suit of this card."""
        return self._suit

    def is_face(self):
        """Returns True if the rank of this card is a face card."""
        return self._rank == "J" or \
               self._rank == "Q" or \
               self._rank == "K"

class Deck:
    """Represent a deck of playing cards."""

    def __init__(self):
        """Initialize a standard deck of 52 cards."""
        self._deck_list = []
        for rank in RANKS:
            for suit in SUITS:
                new_card = PlayingCard(rank, suit)
                self._deck_list.append(new_card)

        self.shuffle()

    def shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self._deck_list)

    def __str__(self):
        return str(self._deck_list)

    def draw_one_card(self):
        """Remove the top card from the deck and return it."""
        return self._deck_list.pop()


def main():

    # card = ("A", "D")
    # #card[0] -> rank
    # #card[1] -> suit
    #
    # real_card = PlayingCard("J", "D")
    # print("Rank:", real_card.get_rank(), ", Suit:", real_card.get_suit())
    # print("Is Face?:", real_card.is_face())
    # print(real_card)

    deck = Deck()
    print(deck)

    a = deck.draw_one_card()
    b = deck.draw_one_card()

    print("first card is", a, "and second card is", b)

    print(deck)


if __name__ == "__main__":
    main()
