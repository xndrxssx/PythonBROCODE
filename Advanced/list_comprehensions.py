#a way to create a new list with less syntax
#can mimic cartain lambda functions, easier to read

#normal:
squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

#list comprehension
squares = [i*i for i in range(1,11)]
print(squares)

#normal
students = [100, 90,80,70,60,50,40,30,0]
#passed_students = list(filter(lambda x: x>=60, students))
#print(passed_students)

#list comprehension
passed_students = [i if i>=60 else "FAILED" for i in students]
print(passed_students)