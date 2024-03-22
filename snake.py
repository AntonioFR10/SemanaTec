"""
Autores: Juan Antonio Figueroa Rodriguez A01369043
         Ángel Armando Márquez Curiel A01754739
"""

from turtle import *
from random import randrange, choice
from freegames import square, vector

colors = ['blue', 'green', 'yellow', 'purple', 'orange']
snake_color = choice(colors)
colors.remove(snake_color)  # Impedimos que la serpiente y la comida tengan el mismo color
food_color = choice(colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """
    Cambia la dirección de la serpiente.
    Los parámetros x e y definen la nueva dirección.
    """
    aim.x = x
    aim.y = y

def inside(head):
    """
    Verifica si la cabeza de la serpiente está dentro de los límites del juego.
    Devuelve True si la cabeza está dentro de los límites, False en caso contrario.
    """
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """
    Mueve la comida un paso en una dirección aleatoria.
    Si la comida se sale de los límites, la mueve de vuelta dentro de los límites.
    """
    food.x += randrange(-10, 11, 10)
    food.y += randrange(-10, 11, 10)

    # Check if food is inside boundaries
    if not inside(food):
        # If food is out of boundaries, move it back
        food.x = max(min(food.x, 190), -200)
        food.y = max(min(food.y, 190), -200)
#
def move():
    """
    Mueve la serpiente un segmento hacia adelante.
    Si la serpiente choca con los límites o con ella misma, termina el juego.
    Si la serpiente come la comida, la comida se mueve a una nueva ubicación.
    Si la serpiente no come la comida, se elimina el último segmento de la serpiente.
    """
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)
    ontimer(move_food, 3000)  # Move food every 7000ms

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()