import turtle, random

def main():

    michelangelo = turtle.Turtle()

    michelangelo.screen.bgcolor("black")
    michelangelo.pencolor("white")
    michelangelo.width(2)

    michelangelo.speed(0)

    # Turns off drawing of turtle for now
    # turtle.tracer(False)

    draw_spiral(michelangelo)

    # This updates the screen
    # turtle.update()

    turtle.mainloop()



def draw_spiral(t):
    """Draws a hexagon with sides of length size"""

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for x in range(400):
        color = colors[x % 6]
        t.pencolor(color)
        t.forward(x)
        t.left(59)

def draw_curved_spiral(t):
    """Draws a hexagon with sides of length size"""

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for x in range(400):
        color = colors[x % 6]
        t.pencolor(color)
        t.circle(x, 60)









if __name__ == "__main__":
    main()
