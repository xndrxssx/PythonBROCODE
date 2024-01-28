from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Jegona's window")

icon = PhotoImage(file='Images/logo.png')
window.iconphoto(True, icon)
window.config(background="#BAB1FF")

window.mainloop()  # place window on screen
