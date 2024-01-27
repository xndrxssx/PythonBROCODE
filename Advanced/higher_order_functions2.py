def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2) #fica esperando o dividend(y)
print(divide(10)) #dividend(y)