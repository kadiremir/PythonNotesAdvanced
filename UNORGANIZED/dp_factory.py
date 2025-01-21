"""
FACTORY PATTERN:

The Factory Method Pattern
    - defines an interface for creating an object, but lets subclasses decide which class to instantiate.
    - lets a class defer instantiation to subclasses.

Advantages:
    - Allows adding new types without changing the client code.
    - Encapsulate object creation.
    - Separates the instantiation process from the implementation.

Structure:
    - Abstract Product
        - Concrete Product A
        - Concrete Product B
    - Product Factory

Client Code:
    - factory = ProductFactory()
    - prodcut_1 = factory.get_product("product_a")
    - prodcut_2 = factory.get_product("product_b")
    - prodcut_1.do_something()
    - prodcut_2.do_something()
"""

############################################################
# Example 1: Factory Method Pattern
############################################################

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle.draw")


class Square(Shape):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Shape {shape_type} not found")


# Client Code
def main():
    factory = ShapeFactory()

    # Create shapes
    shape1 = factory.get_shape("circle")
    shape2 = factory.get_shape("square")
    # this will raise ValueError: Shape rectangle not found
    # shape3 = factory.get_shape("rectangle")

    # Draw shapes
    shape1.draw()
    shape2.draw()
    # shape3.draw()


if __name__ == "__main__":
    main()
    main_two()
