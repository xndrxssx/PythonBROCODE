from tkinter import *
import time
from ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 2, 2, "yellow")
tenis_ball = Ball(canvas, 0, 0, 50, 4, 3, "green")
basket_ball = Ball(canvas, 0, 0, 130, 1, 1.01, "orange")

while True:
    volley_ball.move()
    tenis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()