from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 1.7
yVelocity = 1.2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg = PhotoImage(file='space.png')
background = canvas.create_image(0, 0, image=bg, anchor=NW)

ufo = PhotoImage(file='alien.png')
alien = canvas.create_image(0, 0, image=ufo, anchor=NW)

image_width = ufo.width()
image_height = ufo.height()

while True:
    coordinates = canvas.coords(alien)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(alien,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
