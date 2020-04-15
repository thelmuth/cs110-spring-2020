
from cs110graphics import *

WIN_WIDTH = 600
WIN_HEIGHT = 600


class Car(EventHandler):
    """ A car that can move forward, backward, or turn. """

    def __init__(self, win, color, cen):
        EventHandler.__init__(self)

        self._win = win
        self._width = 20
        self._length = 60

        self._distance = 30

        self._color = color

        # Represent which direction the car is moving.
        # x = 1, moving right, and x = -1 moving left
        # y = 1 moving down, and y = -1 moving up
        self._heading_x = 0
        self._heading_y = -1

        self._body = Rectangle(self._win, self._width, self._length, cen)
        self._body.set_fill_color(self._color)
        self._body.set_depth(10)

        self._body.add_handler(self)

        self._left_light_center = (cen[0] - 4, cen[1] - 26)
        self._right_light_center = (cen[0] + 4, cen[1] - 26)

        self._left_light = Circle(self._win, 3, self._left_light_center)
        self._left_light.set_fill_color("lightgray")
        self._left_light.set_depth(5)

        self._right_light = Circle(self._win, 3, self._right_light_center)
        self._right_light.set_fill_color("lightgray")
        self._right_light.set_depth(5)

        self._components = [self._body, self._left_light, self._right_light]

        for component in self._components:
            self._win.add(component)

        BUTTON_RADIUS = 15
        BUTTON_COLOR = "gray"

        self._forward_button = Button(self._win, self, BUTTON_RADIUS, (50, 25),
                                      BUTTON_COLOR, "forward")
        self._backward_button = Button(self._win, self, BUTTON_RADIUS, (50, 75),
                                       BUTTON_COLOR, "backward")
        self._left_button = Button(self._win, self, BUTTON_RADIUS, (25, 50),
                                      BUTTON_COLOR, "left")
        self._right_button = Button(self._win, self, BUTTON_RADIUS, (75, 50),
                                       BUTTON_COLOR, "right")

    def move(self, direction):
        """ Move in the specified direction."""

        if direction == "forward":
            change_x = self._heading_x * self._distance
            change_y = self._heading_y * self._distance

            for component in self._components:
                component.move(change_x, change_y)


class Button(EventHandler):
    """Buttons to tell which direction the car should go."""

    def __init__(self, win, car, radius, center, color, direction):
        self._win = win

        self._car = car
        self._direction = direction
        self._color = color

        self._circle = Circle(self._win, radius, center)
        self._circle.set_fill_color(self._color)

        self._circle.add_handler(self)
        self._win.add(self._circle)

    def handle_mouse_press(self, event):
        """Tell the car object to move in the correct direction"""
        self._car.move(self._direction)


def main(win):
    """The main function."""

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    bus = Car(win, "yellow", (300, 300))

if __name__ == '__main__':
    """When using cs110graphics, replace the usual line with this one:"""
    StartGraphicsSystem(main)
