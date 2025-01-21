class BankAccount:
    """This class represents a bank account."""
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount!")


account = BankAccount(100)
print(account.get_balance())  # Access balance through getter
account.set_balance(150)      # Modify balance through setter


# In Python, the property decorator and the setter method work together to provide a clean and
# controlled way to manage access to an object's attributes. They allow us to define methods that are
# accessed like attributes but with additional logic for getting and setting values.

# The property decorator is used to define properties in a class. It allows us to define a method that
# can be accessed like an attribute. The method should have the same name as the property and should
# return the property value.

# No need for parentheses when accessing the property.

# Here you can not directly access the radius attribute.
# You can only access the radius property.
# This is the motivation behind using properties in Python.
# Encapsulation is the concept of restricting direct access to some of an object's components.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius."""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive.")

    @radius.deleter
    def radius(self):
        """Deleter for radius."""
        print("Deleting radius...")
        del self._radius


# Usage
circle = Circle(5)
print(circle.radius)  # Output: 5

circle.radius = 15    # Sets radius to 15
print(circle.radius)  # Output: 15

del circle.radius     # Deletes the radius

