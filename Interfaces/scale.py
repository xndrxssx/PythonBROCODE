from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+" degrees C")

window = Tk()

hotImage = PhotoImage(file='Images/flame.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, 
              from_=100, 
              to=0,
              length=400,
              orient=VERTICAL,
              font=('Consoles', 20),
              tickinterval=10,
              #showvalue=0,
              #resolution=5
              troughcolor='#C6FFFD',
              fg='#FF1C00',
              bg='#111111'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

coldImage = PhotoImage(file='Images/snow.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()