"""I: Interface Segregation Principle

Basically:
    Interfaces should be split as much as possible.
    So that the classes that implement the interfaces do not have to implement unnecessary methods.

Motivation:
    Clients should not be forced to depend on methods they do not use.
    This principle promotes creating smaller, more specific interfaces rather than one large, general-purpose interface.
    The goal is to ensure that a class implementing an interface only needs to define the methods it actually requires.
"""


##################
# Bad Example 1:
##################
class MobilePhone:
    def call(self):
        raise NotImplementedError("This method must be implemented in the subclass.")

    def text(self):
        raise NotImplementedError("This method must be implemented in the subclass.")

    def take_photo(self):
        raise NotImplementedError("This method must be implemented in the subclass.")


class OldPhone(MobilePhone):
    def call(self):
        print("Calling...")

    def text(self):
        print("Texting...")

    def take_photo(self):
        raise NotImplementedError("This phone does not have a camera.")


class SmartPhone(MobilePhone):
    def call(self):
        print("Calling...")

    def text(self):
        print("Texting...")

    def take_photo(self):
        print("Taking a photo...")

# In the example above, the MobilePhone class defines three methods: call(), text(), and take_photo().
# The OldPhone and SmartPhone classes inherit from the MobilePhone class and implement all three methods.
# However, the OldPhone class raises a NotImplementedError for the take_photo() method because it does not have a camera.
# This violates the Interface Segregation Principle because:
# the OldPhone class is forced to implement a method that it does not need.


##################
# Fix (Good Example 1):
##################
class MobilePhone:
    def call(self):
        raise NotImplementedError("This method must be implemented in the subclass.")

    def text(self):
        raise NotImplementedError("This method must be implemented in the subclass.")
    

class Camera:
    def take_photo(self):
        raise NotImplementedError("This method must be implemented in the subclass.")
    

class OldPhone(MobilePhone):
    def call(self):
        print("Calling...")

    def text(self):
        print("Texting...")
        

class SmartPhone(MobilePhone, Camera):
    def call(self):
        print("Calling...")

    def text(self):
        print("Texting...")

    def take_photo(self):
        print("Taking a photo...")
