# Exception Handling (Error Handling)

# What You’ll Learn:
    # What exceptions are in Python
    # How to handle errors using try, except, else, and finally
    # How to raise your own custom exceptions

try:
    number =int(input("Enter a number:"))
    result = 10/number
    print("Result is:", result)
except ZeroDivisionError:
    print("You can't divided by zero!")
except ValueError:
    print("Please enter a valid number.")

# Explanation:
    # try: — code that might cause an error
    # except: — code that runs if an error happens
    # You can have multiple except blocks for different types of errors

try:
    number = int(input("Enter a number:"))
    result = 12/number
except ZeroDivisionError:
    print("You can't divided number by Zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result is:", result)
finally:
    print("This blocks runs no matter what.")

# else → runs only if no error occurs
# finally → runs always, even if there was an error


# Task: Safe Division

    # Ask the user to enter two numbers.

    # Divide the first number by the second.

    # Handle these possible errors:

    # ValueError → if the user enters something that is not a number

    # ZeroDivisionError → if the user tries to divide by zero

    # Use else to print the result only if no error occurs.

    # Use finally to print a message like "Thank you for using safe division!"

try:
    my_first_num = int(input("Enter my first number:"))
    my_first_num_2 = int(input("Enter my second number:"))
    results = my_first_num/my_first_num_2 
except ZeroDivisionError:
    print("You can't able to divide by zero!")
except ValueError:
    print("You must enter a valid number!")
else:
    print("Thanks you nailed that:", results)
finally:
    print("Thank you for using safe division!")