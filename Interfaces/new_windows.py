from tkinter import *

def create_window():
    #new_window = Toplevel()
    new_window = Tk()
    #old_window.destroy()

old_window = Tk()  # instantiate an instance of a window

Button(old_window, text="create a new window", command=create_window).pack()

old_window.mainloop()