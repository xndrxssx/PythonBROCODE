from tkinter import *
# label = an area widget that holds text and/or an image within a window

window = Tk()  # instantiate an instance of a window
# window.geometry("420x420")
window.title("Jegona's window")

icon = PhotoImage(file='Images/logo.png')
window.iconphoto(True, icon)
window.config(background="#BAB1FF")

photo = PhotoImage(file='Images/babies.png')

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
# label.place(x=0, y=0)

window.mainloop()
