from tkinter import *

food = ["hamburger", "pizza", "taco"]

def order():
    if(x.get()==0):
        print("You ordered burger")
    elif(x.get()==1):
        print("You ordered pizza")
    elif(x.get()==2):
        print("You ordered taco")
    else:
        print("?")

window = Tk()

pizzaImage = PhotoImage(file='Images/pizza.png')
burgerImage = PhotoImage(file='Images/burger.png')
tacoImage = PhotoImage(file='Images/taco.png')
foodImages = [burgerImage, pizzaImage, tacoImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              pady=10,
                              font=("Lato", 25),
                              image = foodImages[index],
                              compound='left',
                              indicatoron=0,
                              width=375,
                              command=order)
    radiobutton.pack(anchor=W)
    
window.mainloop()