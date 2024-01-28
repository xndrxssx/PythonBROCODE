from tkinter import *

#entry widget = textbox that accepts a single line of user input
def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window,
              font=("Arial", 50),
              fg="#7D00ED",
              bg="white",
              show="*")

entry.insert(0,'Hable')
entry.pack(side=TOP)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=BOTTOM)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=BOTTOM)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=BOTTOM)

window.mainloop()