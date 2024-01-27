#def double(x):
#    return x * 2

#print(double(5))

double = lambda x:x*2
print(double(5))

multiply = lambda x, y : x * y
print(multiply(5,5))

add = lambda x, y, z: x + y + z
print(add(5,5,5))

full_name = lambda firs_name, last_name: firs_name+" "+last_name
print(full_name("Andressa", "Carvalho"))

age_check = lambda age:True if age>=18 else False
print(age_check(18))