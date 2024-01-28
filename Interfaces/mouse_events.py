from tkinter import *

def doSomething(event):
    print("You did a thing at: " + str(event.x)+", "+str(event.y))

window = Tk()

window.bind("<Button-1>", doSomething) #left mouse button
#window.bind("<ButtonRelease>", doSomething)
#window.bind("<Enter>", doSomething)
#window.bind("<Leave>", doSomething)
window.bind("<Motion>", doSomething)

window.mainloop()