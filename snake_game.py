import random
from shutil import move
from tkinter import *

# Constants

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
SPACE_SIZE = 20
FOOD_COLOR = 'green'
COLOR_BODY = 'blue'
COLOR_HEAD = 'yellow'
BACKGROUND_COLOR = '#000000'
SNAKE_LENGTH = 3
SPEED = 100


class Snake:
    def __init__(self):
        self.snake_length = SNAKE_LENGTH
        self.coord = [[0, 0]] * 3
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR)
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE  # 800/48
        y = random.randint(0, (WINDOW_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE  # 500/32

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR)

    def move(snake, food, canvas, window):
        x, y = snake.coord[0]

        snake.coord.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR)
        snake.squares.insert(0, square)

        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

        window.after(SPEED, move, snake, food)

    window = Tk()
    window.title('Snake')
    window.resizable(False, False)

    score = 0

    label_score = Label(window, text='Your score: {}'.format(score), font=('Arial', 35))
    label_score.pack()

    canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg=BACKGROUND_COLOR)
    canvas.pack()

    window.geometry('800x500')


    snake = Snake()
    food = Food()

    move(snake, food)

    window.mainloop()