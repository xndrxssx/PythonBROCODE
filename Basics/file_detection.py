import os

path = "C:\\Users\\Luyza\\Desktop\\texto.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file")
    else:
        print("That isnt a file")
else:
    print("That location doesnt exist!")

