
from cs110graphics import *

WIN_WIDTH = 600
WIN_HEIGHT = 600


# We need a class to make graphics interactive
class Light(EventHandler):
    """ A light is a circle graphic that can change color."""

    def __init__(self, win, rad, cen):
        """ The constructor for Light."""

        # This calls the superclass's constructor (EventHandler), so that it
        # sets up the attributes necessary for EventHandler to work.
        EventHandler.__init__(self)

        self._win = win         # the graphics window
        self._radius = rad      # radius of the circle
        self._center = cen      # center of the circle

        self._colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self._color_index = 0
        self._color = self._colors[self._color_index]

        self._circle = Circle(self._win, self._radius, self._center)
        self._circle.set_fill_color(self._color)

        # Each object has a depth, which determines which object is on top of
        # the other. These are in the range [0, 100], with lower numbers being
        # on top of higher numbers
        self._circle.set_depth(10)

        # Here we ask the Circle object to be its own event handler.
        self._circle.add_handler(self)

        self._win.add(self._circle)


    def handle_mouse_press(self, event):
        """This method is called when the circle is clicked on.
        event contains details about the click, such as the x-y location, etc."""

        self._color_index = (self._color_index + 1) % len(self._colors)
        self._color = self._colors[self._color_index]
        self._circle.set_fill_color(self._color)


class LightDiff(Light):
    """New Light class to allow different colors."""

    def __init__(self, win, rad, cen):

        # Want to call Light's constructor.
        Light.__init__(self, win, rad, cen)

        self._colors = ["black", "grey", "white", "beige", "tan"]
        self._color = self._colors[self._color_index]
        self._circle.set_fill_color(self._color)
        self._circle.set_depth(5)



def main(win):
    """The main function."""

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    # Create a circle:
    first_circle = Circle(win, 30, (300, 300))
    first_circle.set_fill_color("cyan")
    win.add(first_circle)

    second_circle = Circle(win, 60, (580, 20))
    win.add(second_circle)

    # Test Light
    light1 = Light(win, 50, (100, 300))
    light3 = Light(win, 200, (500, 500))

    # Test LightDiff
    light2 = LightDiff(win, 30, (120, 300))
    light4 = LightDiff(win, 15, (400, 200))




if __name__ == '__main__':
    """When using cs110graphics, replace the usual line with this one:"""
    StartGraphicsSystem(main)
