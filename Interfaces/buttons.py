from tkinter import *
# label = an area widget that holds text and/or an image within a window
def click():
    label = Label(window,
              text="Hello",
              font=('Arial', 40, 'bold'),
              fg='#B5ED00',
              bg='#BAB1FF',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
    label.pack()
    button.pack_forget()

window = Tk()  # instantiate an instance of a window
# window.geometry("420x420")
window.title("Jegona's window")

icon = PhotoImage(file='Images/logo.png')
window.iconphoto(True, icon)
window.config(background="#BAB1FF")

photo = PhotoImage(file='Images/babies.png')
arrow = PhotoImage(file='Images/arrow.png')

button = Button(window,
                text='Clique agui',
                command=click,
                font=("Comic Sans", 30),
                fg="#7D00ED",
                bg="#c9c3fa",
                activeforeground="#7D00ED",
                activebackground="#c9c3fa",
                state=ACTIVE,
                image=arrow,
                compound='bottom')
button.pack()

# label.place(x=0, y=0)

window.mainloop()
