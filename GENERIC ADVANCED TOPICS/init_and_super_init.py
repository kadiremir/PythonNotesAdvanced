"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain the usage of__init__ and its combined usage with super() method.

__init__ method:
    It is:
        A special method (called constructor) that is called when an object is created from a class.
        Used to initialize the object's attributes.
        Always called automatically when an object is created.

__init__ method with super():
    The super() function is used to call the parent class's __init__ method.
    It is used to call the parent class's __init__ method when creating an object of the subclass.
"""

####################################################################################################
# Basic example:
####################################################################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person with Name: {self.name}, Age: {self.age}")


class Child(Person):
    def __init__(self, name, age, parent_name):
        # Call the Parent's __init__ method via super() method
        super().__init__(name, age)  # This calls the parent class's __init__ method
        self.parent_name = parent_name
        print(f"Child with name: {self.name}, age: {self.age} and parent: {self.parent_name}")

person = Person("John", 25)
person.display()
child = Child("Jessica", 25, parent_name="Doe")
child.display()

# Output:
# Person with Name: John, Age: 25
# Child with name: Jessica, age: 25 and parent: Doe


####################################################################################################
# An advanced example:
####################################################################################################

class A:
    def __init__(self):
        print("Initializing A")


class B(A):
    def __init__(self):
        super().__init__()  # Call A's __init__
        print("Initializing B")


class C(A):
    def __init__(self):
        super().__init__()  # Call A's __init__
        print("Initializing C")


class D(B, C):
    def __init__(self):
        super().__init__()  # Dynamically resolves MRO
        print("Initializing D")


# Create an instance of D
d = D()

# Output:
# Initializing A
# Initializing C
# Initializing B
# Initializing D
