"""
dice.py
This module has the Die class, which represents a 6-sided die.
"""

import random

class Die():
    """This clas represents a 6-sided die."""

    def __init__(self, sides):
        """constructor.
        The role of the constructor is to initialize the data of an object.
        "self" is the object itself (the one being initialized)."""

        self._value = None
        self._sides = sides
        self.roll()

    def roll(self):
        """Resets the die's value."""
        possible_values = range(1, self._sides + 1)
        self._value = random.choice(possible_values)

        # Another way of doing this.
        # self._value = random.randint(1, self._sides)

    def get_value(self):
        """Returns the die's value."""
        return self._value


def main():

    d1 = Die(6)
    d2 = Die(1000)
    rolls = 0
    while d1.get_value() != d2.get_value():
        print("Dice's roll:", d1.get_value(), d2.get_value())
        d1.roll()
        d2.roll()
        rolls += 1

    print("It took", rolls, "rolls to get doubles.")
    print("Dice's roll:", d1.get_value(), d2.get_value())


main()
