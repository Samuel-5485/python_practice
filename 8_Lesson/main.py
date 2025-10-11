# What Is a Module?

# A module is simply a Python file (.py) that contains code — variables,
# functions, or classes — that you can import and reuse in another file.
import file

file.say_hello("Sami")
file.say_goodbye("Sami")

# Example 2: Importing Specific Functions
# You can also import just what you need:
from file import say_goodbye
say_goodbye("Samuel!")

import my_module

print(my_module.greet("Simon"))
print(my_module.farewell("Simon"))

from my_module import farewell
print(farewell("Elias!"))

# Use Aliases
# You can also give a module or function a nickname for easier use:
import my_module as mm
print(mm.greet("John"))
print(mm.farewell("Tohm"))

# function
from my_module import greet as say_hello
print(say_hello("Chala"))

# 💡 Why This Is Useful

    # Makes code cleaner
    # Avoids typing long module names repeatedly
    # Lets you reuse code efficiently


from My_Package import greetings, farewells
print(greetings.say_hello("Abdi"))
print(farewells.say_goodbye("Sena"))