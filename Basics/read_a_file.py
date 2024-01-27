import os
from turtle import rt

try:
    with open('texto.tx') as file:
        print(file.read())
        print(file.closed)
except FileNotFoundError:
    print("That file was not found")
        

