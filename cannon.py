"""
Autores: Juan Antonio Figueroa Rodriguez A01369043
         Ángel Armando Márquez Curiel A01754739
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Responde al toque en la pantalla."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Ajustamos la velocidad del la bola para que sea más rápida

        speed.x = (x + 411) / 25    
        speed.y = (y + 411) / 25

def inside(xy):
    "Devuelve True si xy está dentro de la pantalla."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Dibuja la bola y los objetivos."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Mueve la bola y los objetivos."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Ajustamos la velocidad de los objetivos para que sea más rápida
        
        target.x -= 2

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        # Si el objetivo no está dentro de la ventana, lo reposicionamos en el otro extremo
        
        if not inside(target):
            target.x = 200

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()