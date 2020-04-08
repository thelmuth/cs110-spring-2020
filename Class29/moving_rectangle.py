
from cs110graphics import *

WIN_WIDTH = 600
WIN_HEIGHT = 600


class MovingRectangle(EventHandler):
    """ A rectangle that moves when we click on it. """

    def __init__(self, win, width, length, cen):
        EventHandler.__init__(self)

        self._win = win
        self._width = width
        self._length = length
        self._center = cen

        self._color = "deeppink"

        self._rect = Rectangle(self._win, self._width, self._length,
                               self._center)
        self._rect.set_fill_color(self._color)
        self._rect.set_border_color("skyblue")

        self._rect.add_handler(self)

        self._win.add(self._rect)

    def handle_mouse_press(self, event):
        """ Move rectangle to the right 20 pixels."""

        (x, y) = self._center
        self._center = (x + 20, y)

        self._rect.move_to(self._center)



def main(win):
    """The main function."""

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    rect = MovingRectangle(win, 100, 40, (100, 500))
    rect2 = MovingRectangle(win, 200, 200, (50, 300))
    rect3 = MovingRectangle(win, 40, 60, (300, 300))

if __name__ == '__main__':
    """When using cs110graphics, replace the usual line with this one:"""
    StartGraphicsSystem(main)
