from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="F:\\Meu Drive\\COMPUTACION\\PYTHON\\Python - Bro Code",
                                          title="Open a file",
                                          filetypes=(("text files", "*.txt"),
                                          ("all files", "*.*")))
    print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()
    
window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()