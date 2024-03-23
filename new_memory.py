"""
Autores: Juan Antonio Figueroa Rodriguez A01369043
         Ángel Armando Márquez Curiel A01754739
"""
from turtle import *
from freegames import path
from random import shuffle

car = path('car.gif')
colors = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'pink', 'orange', 'brown', 'cyan', 
          'lightblue', 'lightgreen', 'darkgreen', 'lavender', 'maroon', 'navy', 'olive', 'teal', 
          'lime', 'aqua', 'fuchsia', 'gray', 'silver', 'crimson', 'indigo', 'violet', 'salmon', 
          'gold', 'darkred', 'darkblue', 'darkyellow', 'darkcyan'] * 2
tiles = colors * 2
writer = Turtle(visible=False)
state = {'mark': None, 'taps': 0}  # Agregamos un contador de taps al estado
hide = [True] * 64

def square(x, y, color_name):
    "Dibuja un cuadrado usando path en (x, y)."
    up()
    goto(x, y)
    down()
    color(color_name)

    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) en índice de tiles."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte el conteo de tiles en coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y los tiles ocultos basándose en el tap."
    spot = index(x, y)
    mark = state['mark']

    if spot >= len(tiles): # Regresar por si se pasa del rango
        return

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    state['taps'] += 1  

def draw():
    "Dibuja la imagen y los tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y, 'white')

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        square(x, y, tiles[mark])

    update()
    ontimer(draw, 100)

    writer.undo()
    writer.write(state['taps'], font=('Arial', 11, 'normal'))

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)

# Agregamos el contador de taps al marcador
writer.goto(180, 180)
writer.color('black')
writer.write(state['taps'], font=('Arial', 11, 'normal'))
onscreenclick(tap)
draw()
done()