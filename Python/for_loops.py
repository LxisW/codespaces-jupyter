import colorsys
import turtle
from time import sleep

# console output


def draw_console():
    max_range = 10
    print()
    # top
    for a in range(1, max_range):
        for j in range(a):
            print("x", end="")
        for b in range(a, 2 * max_range - a):
            print(".", end="")
        for c in range(a):
            print("o", end="")
        print()

    # bottom
    for a in range(max_range, 1, -1):
        for j in range(a):
            print("x", end="")
        for b in range(a, 2 * max_range - a):
            print(".", end="")
        for c in range(a):
            print("o", end="")
        print()


def draw_spiral(t: turtle.Turtle, screen: turtle.Screen):
    t.speed(0)
    screen.bgcolor("black")
    t.width(5)

    for i in range(250):
        color = colorsys.hsv_to_rgb(i / 250, 1.0, 1.0)
        t.pencolor(color)
        t.forward(i * 2)
        t.left(59)


def draw_turtle():
    screen = turtle.Screen()
    t = turtle.Turtle()
    draw_spiral(t, screen)
    screen.mainloop()


def exercise():
    wn = turtle.Screen()
    wn.bgcolor("light green")
    skk = turtle.Turtle()
    skk.color("blue")

    def sqrfunc(size):
        for i in range(4):
            skk.fd(size)
            skk.left(90)
            size = size + 5

    base = 6
    for i in range(7):
        sqrfunc(base)
        base += 20
        print(base)


draw_turtle()
# exercise()
