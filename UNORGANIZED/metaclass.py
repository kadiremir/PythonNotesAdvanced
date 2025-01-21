# Classes are objects too.
# When you create an object of a class, you are creating an invoking an instance of the class.
# That means you automatically invoke the __init__ and __new__ methods of the class.
# Default factory for creating classes is type.
# And the __init__ and __new__ methods are defined in the type class by default.
# The type class is a metaclass.
# So if you want a different factory for creating classes, you can create a metaclass.
# By doing so, you can customize the way classes are created.
# That means your custom __init__ and __new__ methods will be invoked when you create an object of the class.

# Example 1: Creating a Metaclass
# The following code creates a metaclass named Meta.
# The Meta metaclass has a custom __new__ method that prints a message when a new class is created.
# The Meta metaclass is used to create a class named MyClass.
# The MyClass class has a custom __init__ method that prints a message when an object of the class is created.

class Meta(type):
    def __new__(cls, class_name, bases, class_dict):
        print(f"Creating class {class_name}")
        return super().__new__(cls, class_name, bases, class_dict)


class MyClass(metaclass=Meta):
    def __init__(self):
        print("Instantiating MyClass")


a = MyClass()


class MyClassNew(Meta):
    pass


# Create an object of the class
b = MyClassNew()


# type can be considered as a factory of classes.

class Dessert:
    pass

Cake = Dessert()

print(type(Cake))  # <class '__main__.Dessert'>
print(type(Dessert))  # <class 'type'>


#############

# class TestClass:
#    pass

# The above code is equivalent to the following code:
# Because the type of the class is type, the class itself is an object!!!
TestClass = type('TestClass', (), {})

# Here
# the first argument is the name of the class,
# the second argument is a tuple of the parent classes (for inheritance), and
# the third argument is the class dictionary containing the attributes.

# Example with non-empty class dictionary:

class TestClass:
    class_variable = 10

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        pass


# The above code is equivalent to the following code:
TestClass = type('TestClass', (), {
    'class_variable': 10,
    '__init__': lambda self, instance_variable: setattr(self, 'instance_variable', instance_variable),
    'instance_method': lambda self: None
})


Appetizer = type('Appetizer', (), {})

Dip = type('Dip', (Appetizer, ), {'description': 'A creamy dip for veggies.'})

print(Dip.description)  # A creamy dip for veggies.
print(Dip.__bases__)  # (<class '__main__.Appetizer'>,)
print(Dip.__name__)  # Dip
print(Dip.__class__)  # <class 'type'>
salsa = Dip()
print(salsa)
print(type(salsa)) # <class '__main__.Dip'>
print(salsa.description)  # A creamy dip for veggies.
