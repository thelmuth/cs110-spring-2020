# What does this program draw?
# Label the origin (i.e. (0, 0)) and the color of everything.
import turtle

def main():
    speedy = turtle.Turtle()

    speedy.dot(20)
    speedy.up()
    speedy.forward(100)

    speedy.down()
    speedy.width(5)
    speedy.pencolor("teal")
    speedy.fillcolor("pink")
    speedy.begin_fill()

    for _ in range(3):
        speedy.forward(100)
        speedy.left(120)
    speedy.end_fill()
    turtle.mainloop()

main()
