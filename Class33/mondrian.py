
from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

COLORS = ["white", "black", "blue", "yellow", "red"]

class Mondrian(EventHandler):
    """Makes paintings like Piet Mondrian."""

    # This is the direction to split the screen.
    split_direction = "h"

    def __init__(self, win, x_left, x_right, y_top, y_bottom, depth):
        EventHandler.__init__(self)

        self._win = win
        self._x_left = x_left
        self._x_right = x_right
        self._y_top = y_top
        self._y_bottom = y_bottom
        self._depth = depth

        center = ((x_left + x_right) // 2, (y_top + y_bottom) // 2)
        width = x_right - x_left
        height = y_bottom - y_top

        self._rect = Rectangle(self._win, width, height, center)
        self._rect.set_fill_color(random.choice(COLORS))
        self._rect.set_depth(depth)

        self._rect.add_handler(self)

        self._win.add(self._rect)


    def handle_key_press(self, event):
        """Runs when you press a key on the keyboard.
        Store whether h or v was pressed most recently on the keyboard."""
        key = event.get_key()

        # Ignore all keys besides "h" and "v":
        if key == "h":
            Mondrian.split_direction = "h"
        elif key == "v":
            Mondrian.split_direction = "v"


    def handle_mouse_press(self, event):
        """When we click on the rectangle, it should split in two at that point."""

        # This gets the location where the mouse clicked:
        (split_x, split_y) = event.get_mouse_location()

        if Mondrian.split_direction == "h":
            # Horizontal split
            # Top rectangle
            Mondrian(self._win, self._x_left, self._x_right, self._y_top, split_y, self._depth - 1)

            # Bottom rectangle
            Mondrian(self._win, self._x_left, self._x_right, split_y, self._y_bottom, self._depth - 1)

        elif Mondrian.split_direction == "v":
            # Vertical split
            # Left rectangle
            Mondrian(self._win, self._x_left, split_x, self._y_top, self._y_bottom, self._depth - 1)

            # Right rectangle
            Mondrian(self._win, split_x, self._x_right, self._y_top, self._y_bottom, self._depth - 1)

def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    Mondrian(win, 10, WIN_WIDTH - 10, 10, WIN_HEIGHT - 10, 100)



if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
