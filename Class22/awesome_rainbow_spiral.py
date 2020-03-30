import turtle, colorsys

def main():

    michelangelo = turtle.Turtle()

    michelangelo.screen.bgcolor("black")
    michelangelo.pencolor("white")

    # Makes the turtle move faster!
    michelangelo.speed(0)
    michelangelo.width(2)

    # Turns off drawing of turtle until next turtle.update()
    #turtle.tracer(False)

    draw_spiral(michelangelo)

    #turtle.update()

    turtle.mainloop()



def draw_spiral(t):
    """Draws a spiral"""

    for x in range(400):
        hue = x / 400

        rgb = colorsys.hsv_to_rgb(hue, 1, 1)

        rgb_int = int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)

        t.pencolor(rgb_int)
        t.forward(x)
        t.left(59) # Show first with left(60)


if __name__ == "__main__":
    main()
