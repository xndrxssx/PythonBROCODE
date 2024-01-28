from tkinter import *
from tkinter import ttk

window = Tk()  # instantiate an instance of a window

notebook = ttk.Notebook(window) #widget that manages windows/display

tab1 = Frame(notebook) #new frame for tab1
tab2 = Frame(notebook) #new frame for tab2



notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab#1", width=50, height=25).pack()
Label(tab2, text="Hello, this is tab#2", width=50, height=25).pack()

window.mainloop()