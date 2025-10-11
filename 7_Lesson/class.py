
class Person:
     #constructor(called when object is created!)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def method_display(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old!")

# create an object
Person1 = Person("Sami",21)
Person2 = Person("Elias",23)

# call method
Person1.method_display()
Person2.method_display()    


# Exercise: Create a Book Class

# Create a class called Book.

# The class should have these attributes:

# title

# author

# year

# The class should have a method called display_info() that prints:
# "Title: {title}, Author: {author}, Year: {year}"

# Create 2 objects of the Book class with different values.

# Call the display_info() method for both objects.

class Book:
    # constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display_info(self):
        print(f"The title of this book is {self.title} and written by {self.author} at the {self.year}")

Book1 = Book("Life", "James", 1999)
Book2 = Book("How to overcome challenges", "Christina", 2005)

Book1.display_info()
Book2.display_info()


# Instance Variables vs Class Variables
    # Instance Variables → unique to each object (we’ve been using these: self.title, self.author)
    # Class Variables → shared by all objects of the class

class Books:
    library_name = "Abrot Library!"
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    print(Book1.title, library_name)
    print(Book2.author, library_name)
Book1 = Books("Life", "Jefar")
Book2 = Books("Overcome your challange", "Lincon")

Books.library_name = "National Library"
print(Book1.library_name)
print(Book2.library_name)
    # Key: All objects share the class variable, but instance variables are unique to each object.

# 2.Methods with Parameters
# You can also make methods that take extra arguments:
class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def update_title(self, new_title):
        self.title = new_title
book1 = Books("Old Life", "Anan")
print(book1.title)

book1.update_title("The new Life")
print(book1.title)
    # update_title changes the instance variable after object creation.


# 3️⃣ Quick Practice for You

# Create a Car class.

# Attributes: brand, model, year.

# Class variable: wheels = 4

# Method display_info() → prints all info including wheels.

# Create 2 cars and show their info.

class Car:
    wheels = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
    
    def display_info(self):
        print(f"Brand:{self.brand}, Model:{self.model}, Year:{self.year}, and Wheels:{self.wheels}")

Car1 = Car("Ford", "Higher", 2006)
Car2 = Car("Toyota", "medium", 2004)
Car3 = Car("Tesla", "Higher", 2024)

Car1.wheels = 6
Car1.display_info()
Car2.display_info()
Car3.display_info()

# Inheritance

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        print(f"Brand:{self.brand}, Year:{self.year}")
    
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def info(self):
        print(f"Brand:{self.brand},Model:{self.model},Year:{self.year}")

Vehicle1 = Vehicle("Generic", 2010)
Vehicle1.info()
Car1 = Car("Toyota", 2003, "Corolla")
Car1.info()


# Exercise: Animal → Dog

# You’re going to create two classes:

# Animal → the parent class

# Dog → the child class that inherits from Animal

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

        # method
    def make_sound(self):
        print(f"{self.name} {self.species}")
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    #method2
    def make_sound(self):
        print(f"{self.name} {self.species} {self.breed}")

#create an object
Animal_1 = Animal("Lion", "Wild animal")
Dog_1 = Dog("Jos", "dog", "from two mate")

# call
Animal_1.make_sound()
Dog_1.make_sound()

# 🐾 Instructions:

# Create a parent class Animal with:

# A constructor (__init__) that takes name and species

# A method make_sound() that prints:
# "Some generic animal sound"

# Create a child class Dog that:

# Inherits from Animal

# Has an extra attribute breed

# Overrides the make_sound() method to print:
# "Woof! Woof!"

# Finally, create an object from Dog and display:

# Its name, species, and breed
# Then call make_sound()


class Animals:
    # constructor
    def __init__(self, name):
        self.name = name

    # Method_1
    def makes_sound(self):
        print(f"{self.name} makes a sound!")
    
class Dog(Animals):
    def makes_sound(self):
        print(f"{self.name} make a sound of woof!🐶")
class Cat(Animals):
    def makes_sound(self):
        print(f"{self.name} makes a sound of meow!🐱")
class Bird(Animals):
    def makes_sound(self):
        print(f"{self.name} says chirp!🐦")

# create an object
Dog_1 = Dog("Booby")
Cat_1 = Cat("Jerry")
Bird_1 = Bird("Foy")

#call method
# Dog_1.makes_sound()
# Cat_1.makes_sound()
# Bird_1.makes_sound()

# you can also even loop through them!
for animals in [Dog_1, Cat_1, Bird_1]:
    animals.makes_sound()
    # That’s called polymorphism — the same method (makes_sound) behaves differently for each subclass.
    

# What Is Polymorphism?

# Polymorphism means "many forms".
# It allows you to use one method name that behaves differently depending on the object that calls it.

# In Python, polymorphism works naturally with inheritance — just like your last example with Dog, Cat, and Bird.

class Animals:
    def __init__(self):
        pass
    
class Dogs(Animals):
    def make_sound(self):
        return "woof!"
class Cats(Animals):
    def make_sound(self):
        return "meo!"
class Birds(Animals):
    def make_sound(self):
        return "shrip!"

# create an object
animals = [Dogs(), Cats(), Birds()]

# call

for animal in animals:
    print(animal.make_sound())

# ⚡ Bonus: Polymorphism with Functions

# def animal_sound(animal):
#     print(animal.make_Sound())
# animal_sound(Dog())
# animal_sound(Cat())