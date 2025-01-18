"""L: Liskov Substitution Principle (LSP)

Basically:
    A subclass should be able to replace the parent class without causing errors.
    If you have a Parent class and a Child class, you should
    be able to replace the Parent class with the Child class without affecting the program.
    
    In other words, the Child class should be able to extend the Parent class without changing its behavior.
    
Tip:
    To achieve this, abstract classes and abstract methods can be used. 
    So each subclass should implement the abstract methods of the parent class.
"""


####################
# Good Example 1:
####################
class Bird:
    def fly(self):
        print("The bird is flying.")
        
        
class Eagle(Bird):
    def fly(self):
        print("The eagle is flying.")
       
        
class Seagull(Bird): 
    def fly(self):
        print("The seagull is flying.")
    
# This is a good example because the Eagle and Seagull classes can replace the Bird class without causing errors.


####################
# Bad Example 1:
####################
class Bird:
    def fly(self):
        print("The bird is flying.")


class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly.")

# This is a bad example because the Penguin class can't replace the Bird class without causing errors.


####################
# Bad Example 2:
####################
class KitchenTool:
    def cook(self):
        print("The kitchen tool is cooking.")
    
    def set_temperature(self, temperature):
        print(f"The temperature is set to {temperature} degrees.")
        

class Kettle(KitchenTool):
    def set_temperature(self, temperature):
        print(f"The temperature is set to {temperature} degrees.")

# This is a bad example because the Kettle class can't replace the KitchenTool class without causing errors.
