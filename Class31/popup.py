
from cs110graphics import *
import random

WIN_WIDTH = 600
WIN_HEIGHT = 600

class Counter(EventHandler):
    """Makes a button that displays the number of times it has been clicked.
    Every 5 times you click it, a popup window will appear with the given
    message."""

    def __init__(self, win, center, message):
        EventHandler.__init__(self)

        self._win = win
        self._center = center
        self._message = message

        self._count = 0
        self._clickable = True

        self._circ = Circle(self._win, 50, center)
        self._circ.set_fill_color("gold")
        self._circ.set_depth(50)
        self._circ.add_handler(self)
        self._win.add(self._circ)

        self._text = Text(self._win, str(self._count), 40, center)
        self._text.set_depth(20)
        self._text.add_handler(self)
        self._win.add(self._text)


    def handle_mouse_press(self, event):

        if self._clickable:
            self._count += 1
            self._text.set_text(str(self._count))

            if self._count % 5 == 0:
                self.toggle_clickable()
                Popup(self._win, self, (WIN_WIDTH // 2, WIN_HEIGHT // 2), self._message)

    def toggle_clickable(self):
        self._clickable = not self._clickable

class Popup(EventHandler):
    """Makes a popup window that lets you click an "ok" button."""

    # This is a class variable: a variable accessible to every instance of
    # the class. You can access it within the class using Popup.top_depth
    top_depth = 10

    def __init__(self, win, counter, center, message):
        self._win = win
        self._counter = counter

        (x, y) = center

        self._popup_window = Rectangle(self._win, 140, 100, center)
        self._popup_window.set_fill_color("tomato")

        self._text = Text(self._win, message, 14, (x, y - 25))

        self._ok_button = Rectangle(self._win, 40, 30, (x, y + 25))
        self._ok_button.set_fill_color("lightblue")

        self._ok_text = Text(self._win, "ok", 16, (x, y + 25))

        self._ok_button.add_handler(self)
        self._ok_text.add_handler(self)

        self._components = [self._popup_window, self._text, self._ok_button,
                            self._ok_text]

        for component in self._components:
            component.set_depth(Popup.top_depth)
            Popup.top_depth -= 1 #change top_depth for the next component or Popup object

            print(Popup.top_depth)
            self._win.add(component)


    def handle_mouse_press(self, event):
        self._counter.toggle_clickable()
        for component in self._components:
            self._win.remove(component)


def main(win):
    """ The main function. """

    win.set_width(WIN_WIDTH)
    win.set_height(WIN_HEIGHT)

    Counter(win, (250, 250), "This is the\nfirst counter!")
    Counter(win, (350, 350), "This is the\nsecond counter!")


if __name__ == '__main__':
    """ When using cs110graphics, replace the usual line with this one: """
    StartGraphicsSystem(main)
