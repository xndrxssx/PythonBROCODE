#parameter that will pack all arguments into a tuple
def add(*args): #pode ser qualquer nome contanto que tenha o *
    args = list(args) #para que seja possivela alterar os argumentos
    args[0]=0
    sum=0
    for i in args:
        sum+=i
        
    return sum

print(add(1,2,3))