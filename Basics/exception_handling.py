try:
    num=int(input("Enter a number to divide: "))
    den=int(input("Enter a number to divide by: "))
    result=num/den
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("This will always execute")