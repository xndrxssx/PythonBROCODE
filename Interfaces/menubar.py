from tkinter import *
from tkinter import filedialog

#--------------------------------------------  
 
def openFile():
    filepath = filedialog.askopenfilename(initialdir="F:\\Meu Drive\\COMPUTACION\\PYTHON\\Python - Bro Code",
                                          title="Open a file",
                                          filetypes=(("text files", "*.txt"),
                                          ("all files", "*.*")))
    print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()
    print("File has been opened!")
   
    
def saveFile():
    text = Text(window)
    text.pack()
    file = filedialog.asksaveasfile(initialdir="F:\\Meu Drive\\COMPUTACION\\PYTHON\\Python - Bro Code",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML",".html"),
                                        ("All files",".*")
                                    ])
    
    if file is None:
        return
    
    filetext = str(text.get(1.0,END))
    #filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()
    print("File has been saved!")
    
#--------------------------------------------   

def cut():
    print("You cut some text!")
    
def copy():
    print("You copied some text!")

def paste():
    print("You pasted some text!")

#--------------------------------------------   
window = Tk()

openImage = PhotoImage(file='folder.png')
saveImage = PhotoImage(file='diskette.png')
exitImage = PhotoImage(file='stop.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()

