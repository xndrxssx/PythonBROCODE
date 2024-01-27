#function that accepts other function as an arguments
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)