import turtle


def main():
    michelangelo = turtle.Turtle()
    turtle_drawing(michelangelo)


def turtle_drawing(t):
    """ Write a function that takes a turtle, and then asks the user what
    direction the turtle should move using the WASD keyboard keys.

    The turtle should move up 30 pixels if the user enters "w", west 30
    pixels if the user enters "a", etc.

    This process should repeat until the user enters "quit"."""

    direction = ""
    distance = 30

    while direction != "quit":

        direction = input("Enter a direction using wasd: ")

        if direction == "w":
            t.setheading(90)
            t.forward(distance)
        elif direction == "a":
            t.setheading(180)
            t.forward(distance)
        elif direction == "s":
            t.setheading(270)
            t.forward(distance)
        elif direction == "d":
            t.setheading(0)
            t.forward(distance)












main()
