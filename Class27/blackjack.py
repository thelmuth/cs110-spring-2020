"""
File: blackjack.py
Author: Darren Strash
Implement classes for a blackjack game.
"""
import random

RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
SUITS = ["D", "C", "S", "H"]

FACE_CARD_VALUE = 10
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
HIGHEST_HAND_VALUE = 21

class PlayingCard:
    """ A playing card for the game black jack. """

    def __init__(self, rank, suit):
        """ Constructs a playing card with given rank and suit. """
        self._rank = rank
        self._suit = suit

    def __str__(self):
        """ Returns the string representation of the playing card. """
        return str(self._rank) + self._suit

    def __repr__(self):
        """ Returns the string representation of the playing card. """
        return self.__str__()

    def get_rank(self):
        """ Return the rank of the playing card. """
        return self._rank

    def get_suit(self):
        """ Return the suit of the playing card. """
        return self._suit

    def is_face(self):
        """ Return True if and only if the playing card is a face card. """
        return self._rank == "J" or \
               self._rank == "Q" or \
               self._rank == "K"


class Deck:
    """ A deck of playing cards for the game blackjack. """

    def __init__(self):
        """ Construct a shuffled standard 52-card deck of playing cards. """
        self._deck_list = []
        for rank in RANKS:
            for suit in SUITS:
                playing_card = PlayingCard(rank, suit)
                self._deck_list.append(playing_card)
        self.shuffle()

    def __repr__(self):
        """ Return a string representation of the deck of playing cards. """
        return str(self._deck_list)

    def shuffle(self):
        """ Shuffle the deck of playing cards. """
        random.shuffle(self._deck_list)

    def draw_one_card(self):
        """ Remove and return one playing card from the deck. """
        return self._deck_list.pop()

class Hand:
    """ A class for storing a hand of playing cards in blackjack. """

    def __init__(self):
        """ Construct an empty hand with an empty list. """
        self._hand_list = []

    def __repr__(self):
        """ Returning a string representation of the hand. """
        return str(self._hand_list)

    def take_into_hand(self, playing_card):
        """ Including a new playing card into our hand. """
        self._hand_list.append(playing_card)

    def value(self):
        """ Compute the value of the hand as would do in blackjack
            i.e., if having an ace's value be 11 would push total
            value over 21, treat it as a 1. """
        sum_hand = 0
        num_aces = 0
        for card in self._hand_list:
            if card.is_face():
                sum_hand += FACE_CARD_VALUE
            elif card.get_rank() == "A":
                sum_hand += ACE_LOW_VALUE
                num_aces += 1
            else:
                sum_hand += card.get_rank()

        for ace in range(num_aces):
            if sum_hand + ACE_HIGH_VALUE - ACE_LOW_VALUE <= 21:
                sum_hand += ACE_HIGH_VALUE - ACE_LOW_VALUE
        return sum_hand


class Player:
    """Controls a human player of Blackjack."""

    def __init__(self, name, deck):
        """Creates a new player. Note that a Deck object must be passed to the
        player, so that they can draw from it."""
        self._name = name
        self._deck = deck
        self._hand = Hand()

    def get_name(self):
        return self._name

    def get_hand(self):
        return self._hand

    def draw_card(self):
        """Draw a card out of deck into hand."""
        card = self._deck.draw_one_card()
        self._hand.take_into_hand(card)

    def player_value(self):
        """Return the value of a player's hand."""
        return self._hand.value()

    def hit_or_stay(self):
        """Ask the player whether to hit or stay, given their hand value."""
        print()
        print("{}, your current hand is {} with value {}.".format(self._name,
                                                                  self._hand,
                                                                  self.player_value()))

        # Force player to stay if they have value > 21
        if self.player_value() > HIGHEST_HAND_VALUE:
            return "stay"

        # Choice to hit or stay:
        choice = input("Do you want to hit (h) or stay (s): ")
        if choice == "h":
            #Hit
            self.draw_card()
            return "hit"

        else:
            # Stay
            return "stay"


def main():
    """ Make a deck of playing cards and draw two cards."""
    deck = Deck()

    veronica = Player("Veronica", deck)
    arnold = Player("Arnold", deck)
    penelope = Player("Penelope", deck)

    players = [veronica, arnold, penelope]

    # Deal 2 cards to each player:
    for player in players:
        player.draw_card()
        player.draw_card()

    # Have each player play a turn:
    for player in players:
        choice = "start"
        while choice != "stay":
            choice = player.hit_or_stay()

    # Show the results:
    print()
    print("The game is over!")

    best_player = "None"
    best_value = 0

    for player in players:
        value = player.player_value()
        if value > HIGHEST_HAND_VALUE:
            print("{} busted, with a hand of {}.".format(player.get_name(),
                                                         player.get_hand()))
        else:
            print("{} had a hand of {} with value {}.".format(player.get_name(),
                                                              player.get_hand(),
                                                              value))
            if value > best_value:
                best_player = player.get_name()
                best_value = value

    print("The winner is {}!".format(best_player))


if __name__ == "__main__":
    main()
