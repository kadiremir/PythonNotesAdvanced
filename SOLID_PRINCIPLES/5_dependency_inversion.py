"""D: Dependency Inversion Principle (DIP)

Basically:
    Make classes depend on abstract classes rather than non-abstract classes.
    e.g. Make classes inherit from abstract classes.

More formally:
    A high-level module is a module that depends on other modules.
    A low-level module is a module that is depended on by other modules.
    The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules.
    Both should depend on abstractions.
    Additionally, abstractions should not depend on details. Details should depend on abstractions.
"""

####################
### Bad Example 1:
####################

class LightBulb:
    def turn_on(self):
        return "LightBulb: turned on"

    def turn_off(self):
        return "LightBulb: turned off"


class Switch:
    def __init__(self, l: LightBulb):
        self.light_bulb = l
        self.on = False

    def press(self):
        if self.on:
            print(self.light_bulb.turn_off())
            self.on = False
        else:
            print(self.light_bulb.turn_on())
            self.on = True

# This violates the Dependency Inversion Principle because the Switch class depends on the LightBulb class.
# The Switch class should depend on an abstraction, not a concrete class.

####################
### Good Example 1:
####################

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        return "LightBulb: turned on"

    def turn_off(self):
        return "LightBulb: turned off"

class Television(Switchable):
    def turn_on(self):
        return "Television: turned on"

    def turn_off(self):
        return "Television: turned off"


class Switch:
    def __init__(self, l: Switchable):
        self.switch = l
        self.on = False

    def press(self):
        if self.on:
            print(self.switch.turn_off())
            self.on = False
        else:
            print(self.switch.turn_on())
            self.on = True

l = LightBulb()
t = Television()
switch = Switch(l)
switch.press()
switch = Switch(t)
switch.press()

# This is a better implementation because the Switch class now depends on the Switchable interface, which is an abstraction.
