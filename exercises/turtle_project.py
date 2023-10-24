"""Starry Night, but made with a turtle."""

__author__: str = "730655689"


from turtle import Turtle, done
leo: Turtle = Turtle()


def star(x: Turtle, y: float, z: float, color: str, size: float) -> None:
    """Creates a star of a chosen size and color at a chosen location."""
    x.pencolor(color)
    x.fillcolor(color)
    x.penup()
    x.goto(y, z)
    x.pendown()
    x.begin_fill()
    x.left(18)
    x.forward(size)
    i: int = 0
    while (i < 4):
        x.left(144)
        x.forward(size)
        i += 1
    x.end_fill()


def circle(x: Turtle, y: float, z: float, r: float, color: str) -> None:
    """Creates a circle with a given radius, and color, centered at the given coordinates."""
    x.pencolor(color)
    x.fillcolor(color)
    x.penup()
    x.goto(y, z)
    x.pendown()
    x.begin_fill()
    x.speed(200)
    x.forward(r)
    x.left(90)
    i: int = 0
    while i < 360:
        x.forward(0.017453 * r)
        x.left(1)
        i += 1
    x.end_fill()


def spiral(x: Turtle, y: float, z: float, r: float, color: str) -> None:
    """Creates a spiral of the given color and radius at the given coordinates."""
    x.pencolor(color)
    x.penup()
    x.goto(y, z)
    x.pendown()
    i: int = 0
    d: int = 15
    while i < 23:
        if i % 5 == 0:
            d += 5
        if i == 20:
            d += 15
        x.forward(r)
        x.left(d)
        i += 1


def fill_canvas(x: Turtle, color: str) -> None:
    """Fills the whole canvas with the given color."""
    x.pencolor(color)
    x.fillcolor(color)
    x.begin_fill()
    x.goto(-385, -315)
    i: int = 0
    while i < 4:
        x.forward(770)
        x.left(90)
        i += 1
    x.end_fill()


def rect(x: Turtle, y: float, z: float, length: float, width: float, color: str) -> None:
    """Creates a rectangle of the given color and with the given width and length at the given coordinates."""
    x.pencolor(color)
    x.fillcolor(color)
    x.penup()
    x.goto(y, z)
    x.pendown()
    x.begin_fill()
    x.left(90)
    x.forward(length)
    x.left(90)
    i: int = 0
    while i < 4:
        x.left(90)
        if i % 2 != 0:
            x.forward(width)
        else:
            x.forward(length)
        i += 1
    x.end_fill()
    
    
def main() -> None:
    """Part of my code where I draw :)."""
    fill_canvas(leo, "dark blue")
    """Sky."""
    rect(leo, -385, -315, 100, 770, "brown")
    """Ground."""
    rect(leo, -300, 0, 260, 100, "grey")
    """Building."""
    star(leo, 100, 100, "yellow", 100)
    star(leo, -100, 100, "yellow", 50)
    star(leo, 100, 200, "yellow", 25)
    star(leo, -200, 150, "yellow", 75)
    star(leo, -300, 150, "yellow", 45)
    """Stars."""
    spiral(leo, 0, 200, 15, "light blue")
    spiral(leo, -200, 150, 25, "light blue")
    spiral(leo, 175, 30, 10, "light blue")
    spiral(leo, 320, 260, 10, "light blue")
    """Spirals."""
    done()


if __name__ == "__main__":
    main()