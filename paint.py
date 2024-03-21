"""Paint, for drawing shapes.

Autores: Juan Antonio Figueroa Rodriguez A01369043
         Ángel Armando Márquez Curiel A01754739

"""

from turtle import *
from freegames import vector


# Función para dibujar una línea desde un punto de inicio hasta un punto final
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función para dibujar un cuadrado desde un punto de inicio hasta un punto final
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()
    up()

# Función para dibujar un rectángulo desde un punto de inicio hasta un punto final
def circulo(start):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    circle(50)
    end_fill()
    up()

# Función para dibujar un triángulo desde un punto de inicio hasta un punto final
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.y - start.y) / 2)
        left(90)
        forward(end.x - start.x)
        left(90)
        forward((end.y - start.y) / 2)
        left(90)
    end_fill()
    up()

# Función para dibujar un triángulo desde un punto de inicio hasta un punto final
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
    up()

# Función para almacenar el punto de inicio o dibujar la forma
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Función para almacenar un valor en el estado en una clave
def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
color('red')
square(vector(-100, -100), vector(100, 100))
color('black')
circulo(vector(-50, -50))
color('blue')
rectangle(vector(-50, -50), vector(50, 50))
color('green')
triangle(vector(-50, -50), vector(50, 50))
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('Yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
