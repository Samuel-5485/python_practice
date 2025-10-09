# factorial

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i #1*1, 1*2, 2*3, 6*4: 24 
#     return result
# print(factorial(4))


# # Fibonacci Sequence
# # The Fibonacci sequence is a series of numbers where:
#     # The first two numbers are 0 and 1.
#     # Every next number is the sum of the previous two.

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b=b, a+b
# print(fibonacci(10))


# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result*=i
#     return result

# num = int(input("Enter number:"))
# print(f"The factorial of {num} is {factorial(num)}")

# # Mini Exercise for You
#     # Write a function factorial(n) using a for loop.
#     # Ask the user for input and print the result.
#     # (Optional) Try to handle negative numbers gracefully — factorial is only defined for non-negative integers.

# def factorial(n):
#     My_Result = 1
#     for i in range(1, n+1):
#         My_Result*=i
#     return My_Result
# num = int(input("Enter number:"))
# print(f"Factorial of {num} is {factorial(num)}")


# def is_even(num):
#     return num % 2 ==0
    
# number = int(input("Enter a number:"))
# if is_even(number):
#     print(f"{number} Even")
# else:
#     print("Odd")


# Mini Exercise for You

    # Ask the user for multiple numbers separated by space, and print if each is even or odd.
    # Try to store the results in a list and print that list at the end.


numbers = input("Enter numbers separated by space:") #ask the user to enter the numbers separeted by space
num_list = numbers.split() #split the input string into a list of string  : separates the string by spaces → ['10', '20', '30', '40'].
num_list = [int(num) for num in num_list] #convert each string in the list to an integer: converts each item into an integer → [10, 20, 30, 40].
print("You entered:", num_list) #print the number one by one

#We can also use this method and check for odd and even

numbers = input("Enter the numbers separated by space:")
num_list = numbers.split()  # ["1", "2", "3"]
num_list = [int(num) for num in num_list] #and this convert that into integer form 
# nums = input("Enter numbers: ").split()
# print(nums)




#For long list comprehension
# new_list = []
# for num in num_list:
#    new_List.append(int(num))
#2nd criteria
# for num in num_list:
#    if num % 2 == 0:
#       print(f"{num} is Even")
#    else:
#       print(f"{num} is Odd")
