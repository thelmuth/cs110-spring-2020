"""
hey_thats_my_fish.py
Graphical implementation of the board game Hey, That's My Fish!
Written in class
April 2019
"""

from cs110graphics import *
import random, math

WIN_WIDTH = 800
WIN_HEIGHT = 900

HEX_WIDTH = WIN_WIDTH // 8
HALF_HEX_WIDTH = HEX_WIDTH // 2

HEX_HEIGHT = int(2 * HALF_HEX_WIDTH / math.sqrt(3)) * 2
HEX_SIDE_LENGTH = HEX_HEIGHT // 2

BOARD_ROWS = 8
BOARD_COLS = 15

class HeyThatsMyFish:
    """Implements Hey That's My Fish!"""

    def __init__(self, win):

        win.set_background("darkblue")

        self._win = win

        # This tells us if we're still playing the initial penguins
        self._still_in_setup = True

        # This keeps track of which tile is selected to move a penguin from
        self._current_tile = None

        # Create board as a hexagonal grid of tiles
        self._board = []
        for r in range(BOARD_ROWS):
            row = []

            # Even rows have 7 tiles, odd rows have 8 tiles
            for c in range(BOARD_COLS):
                # Skip even columns in even rows, and odd columns in odd rows
                if (r + c) % 2 == 0:
                    tile = None
                else:
                    tile = Tile(win, self, r, c)
                row.append(tile)

            self._board.append(row)

        # Player colors
        self._players = [Player("red"), Player("green")]
                         #Player("yellow"), Player("purple")]
        self._player = 0

        # Number of penguins each player has played so far.
        self._penguin_number = 1

        # Add text at bottom describing who's turn it is, etc.
        color = (self._players[self._player]).get_color()
        self._text = Text(self._win, "{} player's turn to add penguin {}.".format(color, self._penguin_number),
                          32, (WIN_WIDTH // 2, 750))
        self._text.set_color(color)
        self._win.add(self._text)

        # Make score per player
        self._scores = []
        x_coord = 300
        for player in self._players:
            score_text = Text(self._win, "0", 32, (x_coord, 800))
            x_coord += 100
            score_text.set_color(player.get_color())
            self._scores.append(score_text)
            self._win.add(score_text)



    def handle_tile_click(self, tile):
        """Handles when a tile gets clicked on, which calls this method."""

        if self._still_in_setup:
            self.play_initial_penguin(tile)
        else:
            self.handle_penguin_move(tile)

    def play_initial_penguin(self, tile):
        """Handles the first placements of penguins during game setup."""

        # Check if this tile already has a penguin, and if so, skip
        if tile.get_penguin() != None:
            return

        # Check that tile has one fish
        if tile.get_fish() != 1:
            return

        # Add correctly-colored penguin to the tile
        color = (self._players[self._player]).get_color()
        tile.add_penguin(color)

        # Update the player
        self._player = (self._player + 1) % len(self._players)

        # Update the penguin number
        if self._player == 0:
            self._penguin_number += 1
        next_color = (self._players[self._player]).get_color()

        # Update text:
        self._text.set_text("{} player's turn to add penguin {}.".format(next_color, self._penguin_number))
        self._text.set_color(next_color)


        if self._penguin_number >= 3:
            # Not in setup anymore
            self._still_in_setup = False
            self._text.set_text("{} player's move.".format(next_color, self._penguin_number))


    def handle_penguin_move(self, tile):
        """Take care of moving penguins during the game itself."""

        # Check if a tile is selected yet
        if self._current_tile == None:
            # Check if tile has a penguin. If not, ignore this click
            # Also check that the penguin color is the same as the current player
            if tile.get_penguin() != (self._players[self._player]).get_color():
                return

            self._current_tile = tile
            tile.toggle_selected()

        else:
            # Check if the tile is selected already. If so, unselect it
            if tile.is_selected():
                tile.toggle_selected()
                self._current_tile = None
            else:
                # We need to move the penguin to this tile, as long as it isn't
                # already occupied
                if tile.get_penguin() != None:
                    return

                # Check that move is legal, in that it is on a hexagonal line
                # and there are no gaps or penguins between start and destination
                if not self.legal_move(self._current_tile, tile):
                    return

                self.make_move(tile)

                # update the player
                self._player = (self._player + 1) % len(self._players)
                next_color = (self._players[self._player]).get_color()
                self._text.set_color(next_color)
                self._text.set_text("{} players move.".format(next_color))

                # Display current score


    def legal_move(self, start_tile, destination_tile):
        """Checks if moving from start_tile to destination tile is a legal move.
        Returns True if move is legal, and False otherwise."""

        start_row = start_tile.get_row()
        start_col = start_tile.get_col()
        dest_row = destination_tile.get_row()
        dest_col = destination_tile.get_col()

        # Check if start and destination are in the same row
        if start_row == dest_row:
            current_col = start_col

            # Find the change in direction we need to check
            if start_col < dest_col:
                delta_col = 2
            else:
                delta_col = -2

            # Keep changing the current_col by delta until either we hit the
            # destination or a tile that is missing or has a penguin.
            while current_col != dest_col:
                current_col += delta_col
                if current_col == dest_col:
                    return True

                # Check if the current_col tile is removed or a penguin
                current_tile = self._board[start_row][current_col]
                if current_tile.get_penguin() != None or current_tile.is_removed():
                    return False


        else:
            # Check the diagonals
            diagonal_deltas = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

            for (delta_row, delta_col) in diagonal_deltas:
                current_row = start_row + delta_row
                current_col = start_col + delta_col

                # Keep changing column and row by deltas until we either hit
                # the destination or a tile that is sunk or a tile with
                # a penguin or fall off the map
                while current_row >= 0 and current_row < BOARD_ROWS and \
                      current_col >= 0 and current_col < BOARD_COLS:

                    # Check if at destination
                    if current_row == dest_row and current_col == dest_col:
                        return True

                    # Check if currently considered tile is removed or a penguin
                    current_tile = self._board[current_row][current_col]
                    if current_tile.get_penguin() != None or current_tile.is_removed():
                        break

                    # update the row and column
                    current_row += delta_row
                    current_col += delta_col

            # We've checked all 4 directions, and none are legal moves.
            return False


    def make_move(self, tile):
        """This moves the penguin on self._current_tile to tile."""

        # Update the current player's score
        player = self._players[self._player]
        fish = self._current_tile.get_fish()
        player.add_to_score(fish)

        score_to_update = self._scores[self._player]
        score_to_update.set_text(str(player.get_score()))

        # Get the color of the first selected tile
        color = self._current_tile.get_penguin()

        # Put penguin of this color on the new tile
        tile.add_penguin(color)

        # Remove the old tile from the window, and make it not current
        self._current_tile.remove()
        self._current_tile = None


class Player:
    """Represents a player in HTMF"""

    def __init__(self, color):
        self._color = color
        self._score = 0

    def get_color(self):
        return self._color

    def get_score(self):
        return self._score

    def add_to_score(self, fish):
        self._score += fish


class Tile(EventHandler):
    """A tile in HTMF"""

    def __init__(self, win, game, row, col):
        EventHandler.__init__(self)

        self._win = win
        self._game = game
        self._row = row
        self._col = col

        # This stores the color of the penguin on this tile, if there is one.
        # If not, set to None
        self._penguin = None

        # Tracks whether this tile is selected or not
        self._selected = False

        # Tells whether this tile has been removed
        self._removed = False

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

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col

    def get_penguin(self):
        return self._penguin

    def get_fish(self):
        return self._fish

    def is_selected(self):
        return self._selected

    def is_removed(self):
        return self._removed

    def center_from_row_col(self):
        """Find the center of this tile based on its row and column."""

        center_x = HALF_HEX_WIDTH * self._col + HALF_HEX_WIDTH

        center_y = (3 * HEX_SIDE_LENGTH * self._row // 2) + HEX_SIDE_LENGTH

        self._center = (center_x, center_y)

    def add_penguin(self, color):
        """Adds a penguin to this tile."""

        self._penguin = color

        self._penguin_shape = Circle(self._win, 12, (self._center[0], self._center[1] + 28))
        self._penguin_shape.set_fill_color(color)
        self._penguin_shape.set_depth(10)
        self._penguin_shape.add_handler(self)
        self._win.add(self._penguin_shape)

    def handle_mouse_press(self, event):
        """Tells the game class that this tile was clicked on."""
        self._game.handle_tile_click(self)

    def toggle_selected(self):
        """Toggles whether or not this tile is selected."""

        self._selected = not self._selected

        if self._selected:
            self._hex.set_border_color(self._penguin)
        else:
            self._hex.set_border_color("lightblue")

    def remove(self):
        """Remove the visual components of the tile from the window."""

        self._win.remove(self._hex)
        self._win.remove(self._text)
        self._win.remove(self._penguin_shape)
        self._removed = True

def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    HeyThatsMyFish(win)


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
