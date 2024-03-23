"""
Autores: Juan Antonio Figueroa Rodriguez A01369043
         Ángel Armando Márquez Curiel A01754739
"""
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
writer = Turtle(visible=False)
state = {'mark': None, 'taps': 0}  # Agregamos un contador de taps al estado
hide = [True] * 64

def square(x, y):
    "Dibuja un cuadrado blanco con contorno negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convierte las coordenadas (x, y) en índice de los cuadros."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convierte el conteo de cuadros en coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Actualiza la marca y los cuadros ocultos basado en el tap."
    
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Incrementamos el contador de taps
    state['taps'] += 1  

def draw():
    "Dibuja la imagen y los cuadros."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
    
    # Aumentamos el contador de taps en el marcador
    writer.undo()
    writer.write(state['taps'], font=('Arial', 11, 'normal'))

    # Verificamos si todos los cuadros se han destapado
    if all(not h for h in hide):
        writer.goto(0, 0)
        writer.color('black')
        writer.write('¡Todos los cuadros se han destapado!', font=('Arial', 20, 'normal'))

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