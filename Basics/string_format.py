# animal="cow"
# item="moon"
# print("The "+animal+" jumped over the "+item)
# print("The {1} jumped over the {0}".format(animal, item))
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# text = "The {} jumped over the {}"
# print(text.format(animal,animal))

#name = "Andressa"
#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. HAHA".format(name))  # padding
#print("Hello, my name is {:>10}. HAHA".format(name))
#print("Hello, my name is {:<10}. HAHA".format(name))
#print("Hello, my name is {:^10}. HAHA".format(name))

num = 1000

print("The number pi is {:.2f}".format(num))
print("The number pi is {:,}".format(num))
print("The number pi is {:b}".format(num))
print("The number pi is {:o}".format(num))
print("The number pi is {:x}".format(num))
print("The number pi is {:e}".format(num))