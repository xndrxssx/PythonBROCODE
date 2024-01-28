from tkinter import *

window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

first_nameLabel = Label(window, text="First name: ", width=20).grid(row=1, column=0)
first_nameEntry = Entry(window).grid(row=1, column=1)

last_nameLabel = Label(window, text="Last name: ").grid(row=2, column=0)
last_nameEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text="Email: ", width=30).grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, columnspan=2, column=0)

window.mainloop()
