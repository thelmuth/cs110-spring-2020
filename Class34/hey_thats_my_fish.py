"""
hey_thats_my_fish.py
Graphical implementation of the board game Hey, That's My Fish!
Written in class
April 2019
"""

from cs110graphics import *
import random, math

WIN_WIDTH = 800
WIN_HEIGHT = 800

HEX_WIDTH = WIN_WIDTH // 8
HALF_HEX_WIDTH = HEX_WIDTH // 2

HEX_HEIGHT = int(2 * HALF_HEX_WIDTH / math.sqrt(3)) * 2
HEX_SIDE_LENGTH = HEX_HEIGHT // 2

class HeyThatsMyFish:
    """Implements Hey That's My Fish!"""

    def __init__(self, win):

        win.set_background("darkblue")

        self._win = win

        # Create board as a hexagonal grid of tiles
        self._board = []
        for r in range(8):
            row = []

            # Even rows have 7 tiles, odd rows have 8 tiles
            cols = 7
            if r % 2 == 1:
                cols = 8

            for c in range(cols):
                tile = Tile(win, self, r, c)
                row.append(tile)

            self._board.append(row)


class Tile(EventHandler):
    """A tile in HTMF"""

    def __init__(self, win, game, row, col):
        EventHandler.__init__(self)

        self._win = win
        self._game = game
        self._row = row
        self._col = col

        # The number of fish on the tile
        self._fish = random.randint(1, 3)

        self.center_from_row_col()

        self._hex = Circle(win, 47, self._center)
        self._hex.set_border_color("lightblue")
        self._hex.set_border_width(5)
        self._hex.set_depth(50)
        self._hex.add_handler(self)

        self._text = Text(win, str(self._fish), 20, self._center)
        self._text.set_depth(30)
        self._text.add_handler(self)

        self._win.add(self._hex)
        self._win.add(self._text)


    def center_from_row_col(self):
        """Find the center of this tile based on its row and column."""

        center_x = HEX_WIDTH * self._col + HALF_HEX_WIDTH
        if self._row % 2 == 0:
            center_x += HALF_HEX_WIDTH

        center_y = (3 * HEX_SIDE_LENGTH * self._row // 2) + HEX_SIDE_LENGTH

        self._center = (center_x, center_y)

    def add_penguin(self, color):
        """Adds a penguin to this tile."""

        self._penguin = Circle(self._win, 12, (self._center[0], self._center[1] + 28))
        self._penguin.set_fill_color(color)
        self._penguin.set_depth(10)
        self._penguin.add_handler(self)
        self._win.add(self._penguin)

    def handle_mouse_press(self, event):
        self.add_penguin("green")


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
