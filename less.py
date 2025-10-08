
#What is a variable?

#A variable is like a box that stores data in memory — a name that holds a value.
# name = "sami"
# age = 20
# My_programming_Lang = "Python"
#  #print("My name is", name, "And i am", age, "years old.", "My favorite programming language is", My_programming_Lang)
# print(f"My name is {name} And I am {age} years old. My favorite programming language is {My_programming_Lang}")


# #Data types
# # name_1 = "Chala"
# # height = 1.75
# # is_student = True 
# # nickname = None

# # print(type(name_1))
# # print(type(height))
# # print(type(is_student))
# # print(type(nickname))
# # #therefore the type() function shows what kind of data a variable holds

# # # Try writing this small task:

# # #1.Create five variables:

# # # your full name

# # # your age

# # # your weight

# # # whether you are a student (True/False)

# # # and set one variable to None

# # #2. Print each variable and its type using type().

# # name_2 = "Jon"
# # age_1 = 25
# # weight = 60
# # is_student = False
# # default = None
# # print(name_2)
# # print(age_1)
# # print(weight)
# # print(is_student)
# # print(default)

# # print(type(name_2))
# # print(type(age_1))
# # print(type(weight))
# # print(type(is_student))
# # print(type(default))

# #Lesson_4:
# # name = input("Enter your name:")
# # print("Hello,", name)
# # age = int(input("How old are you?:"))
# # print("I am,", age,"years old!")

# # Try writing this small program 

# #1. Ask the user to enter their:

# # name

# # age

# # weight

# #2. Then print a sentence like:
# # "Hello Sami, you are 20 years old and your weight is 60 kg."

# # Use input() and type conversion correctly.

# # name = input("Enter the name:")

# # name_2 = input("Enter your name:")
# # print(name_2)

# # age = int(input("Enter your age:"))
# # print(age)

# # weight = int(input("Enter your weight:"))
# # print(weight)

# # print(f"Hello, {name_2} you are {age} years old and your weight is {weight} kg.")

# #Lesson 5:Arithmetic and operators

# a = 10
# b = 4
# print("Addition:", a + b)
# print("Subtract:", a - b)
# print("Multiplication:", a*b)
# print("Division:", a/b)
# print("Floor division", a//b)
# print("Modulo:", a%b)
# print("power:", a**b)

# # Write a small program that:

# # Asks the user to enter two numbers.

# # Prints the result of:

# # addition

# # subtraction

# # multiplication

# # division

# # remainder

# # Use clear labels when printing, for example:
# # The sum of 5 and 3 is 8

# a = int(input("The first number:"))
# b = int(input("The second number:"))

# print(f"The sum of {a} and {b} is", a + b)
# print(f"The difference of {a} and {b} is", a - b)
# print(f"The multiplication of {a} and {b} is", a*b)
# print(f"The division of {a} and {b} is", a/b) #if you need 2 decimal place you can code {a/b:.2f}
# print(f"The remainder of {a} and {b} is", a%b)

# x = 6
# y = 3

# print(f"is that {x==y}")
# print(f"is that {x>y}")
# print(f"is that {x<y}")
# print(f"what you say {x!=y}")
# print(f"what you say {x<=y}")
# print(f"what about now {x>=y}")

# # Write a program that:

# # Asks the user to enter two numbers.

# # Checks and prints:

# # If the numbers are equal

# # If the first number is greater

# # If the first number is less

# # Then use a logical operator to check if both numbers are positive.

# x = int(input("Enter the first number:"))
# y = int(input("Enter the second number:"))

# print(f"true or false {x} and {y} is {x==y}")
# print(f"is that {x} is greater than {y}: {y<x}")
# print(f"what about now is that {x} is less than {y}: {x<y}")
# print(f"is that they are positive: {x>0 and y>0}")


# Lesson 7: Conditional Statements (if, elif, else)

# Conditional statements allow your program to make decisions and run different code depending on whether something is true or false.

# 1.if statement
x = 5
if x > 0:
    print("it is positive.")
# Note: Python uses indentation (spaces) instead of curly braces {}.

# 2.else statement
x = 8
if x > 7:
    print("it is greater than 7")
else:
    print("it is less or it self")

# 3.elif
x = 2
if x == 3:
    print("exactly they are equal")
elif x>3:
    print("x is greater than 3")
else:
    print("x is less than 3")


# Write a program that:

# Takes a number from the user.

# Prints:

# "Positive" if the number is greater than 0

# "Negative" if the number is less than 0

# "Zero" if the number is 0

# This will combine input, comparison, and conditional statements.

x = int(input("Enter number:"))
if x > 0:
    print("it is positive")
elif x < 0:
    print("it is negative")
else:
    print("it equal to zero")