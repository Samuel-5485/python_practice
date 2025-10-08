
#What is a variable?

#A variable is like a box that stores data in memory — a name that holds a value.
name = "sami"
age = 20
My_programming_Lang = "Python"
 #print("My name is", name, "And i am", age, "years old.", "My favorite programming language is", My_programming_Lang)
print(f"My name is {name} And I am {age} years old. My favorite programming language is {My_programming_Lang}")


#Data types
name_1 = "Chala"
height = 1.75
is_student = True 
nickname = None

print(type(name_1))
print(type(height))
print(type(is_student))
print(type(nickname))
#therefore the type() function shows what kind of data a variable holds

# Try writing this small task:

#1.Create five variables:

# your full name

# your age

# your weight

# whether you are a student (True/False)

# and set one variable to None

#2. Print each variable and its type using type().

name_2 = "Jon"
age_1 = 25
weight = 60
is_student = False
default = None
print(name_2)
print(age_1)
print(weight)
print(is_student)
print(default)

print(type(name_2))
print(type(age_1))
print(type(weight))
print(type(is_student))
print(type(default))

name = input("Enter your name:")
print("Hello,", name)
age = int(input("How old are you?:"))
print("I am,", age,"years old!")

# Try writing this small program 

#1. Ask the user to enter their:

# name

# age

# weight

#2. Then print a sentence like:
# "Hello Sami, you are 20 years old and your weight is 60 kg."

# Use input() and type conversion correctly.

# name = input("Enter the name:")

name_2 = input("Enter your name:")
print(name_2)

age = int(input("Enter your age:"))
print(age)

weight = int(input("Enter your weight:"))
print(weight)

print(f"Hello, {name_2} you are {age} years old and your weight is {weight} kg.")
