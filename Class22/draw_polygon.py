import turtle


def main():
    t = turtle.Turtle()

    draw_polygon(t, [(50, 20), (-20, 20), (-40, -50), (70, -30)])

    turtle.mainloop()


def draw_polygon(t, vertices):
    """Draws a polygon from a list of vertices.
    The list has the form [(x1, y1), ..., (xn, yn)]."""

    t.up()
    t.goto(vertices[-1])
    t.down()

    for (x, y) in vertices:
        t.goto(x, y)


main()
