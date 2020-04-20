
from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

COLORS = ["blue", "yellow", "white", "black", "red"]


class KittenMondrian(EventHandler):
    """Makes paintings like Piet Mondrian."""

    # This is the direction to split the screen. "h" is for horizontal,
    # "v" is for vertical.
    # Want this to be a class variable, so that all Mondrian objects have the
    # same value.
    split_direction = "h"

    def __init__(self, win, x_left, x_right, y_top, y_bottom, depth, images):
        EventHandler.__init__(self)

        self._win = win
        self._x_left = x_left
        self._x_right = x_right
        self._y_top = y_top
        self._y_bottom = y_bottom
        self._depth = depth
        self._images = images

        center = ((x_left + x_right) // 2, (y_top + y_bottom) // 2)
        width = x_right - x_left
        height = y_bottom - y_top

        image = random.choice(self._images)
        self._rect = Image(self._win, image, width, height, center)
        self._rect.set_depth(depth)

        self._rect.add_handler(self)

        self._win.add(self._rect)


    def handle_key_press(self, event):
        """Stores whether h or v key was pressed most recently on keyboard."""
        key = event.get_key()

        # Ignore all keys besides "h" and "v"
        if key == "h":
            KittenMondrian.split_direction = "h"
        elif key == "v":
            KittenMondrian.split_direction = "v"


    def handle_mouse_press(self, event):

        # This gets the location where the mouse clicked.
        (split_x, split_y) = event.get_mouse_location()

        # If left button clicked, split vertically. If right button, horizontally
        if KittenMondrian.split_direction == "v":
            # Split vertically

            KittenMondrian(self._win, self._x_left, split_x, self._y_top, self._y_bottom,
                     self._depth - 1, self._images)
            KittenMondrian(self._win, split_x, self._x_right, self._y_top, self._y_bottom,
                     self._depth - 1, self._images)


        elif KittenMondrian.split_direction == "h":
            # Split horizontally

            KittenMondrian(self._win, self._x_left, self._x_right, self._y_top, split_y,
                     self._depth - 1, self._images)
            KittenMondrian(self._win, self._x_left, self._x_right, split_y, self._y_bottom,
                     self._depth - 1, self._images)

def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    kittens = []
    for i in range(16):
        filename = "images/kitten{}.jpg".format(i)
        kittens.append(filename)


    KittenMondrian(win, 10, WIN_WIDTH - 10, 10, WIN_HEIGHT - 10, 100, kittens)



if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
