from tkinter import *

def display():
    if(x.get()==1):
        print("Agreed")
    else:
        print("Disagreed")

window = Tk()

x = IntVar()

check = PhotoImage(file='check.png')

check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 30),
                           fg="#7D00ED",
                           bg="#E1FFC6",
                           activeforeground="#7D00ED",
                           activebackground="#E1FFC6",
                           padx=25,
                           pady=10,
                           image=check,
                           compound='left')

check_button.pack()

window.mainloop()