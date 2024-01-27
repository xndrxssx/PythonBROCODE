import os

source = "test.txt"
destination = "G:\\Meu Drive\\COMPUTACION\\PYTHON\\test.txt"

try:
    if os.path.exists(destination):
        print("Theres already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")