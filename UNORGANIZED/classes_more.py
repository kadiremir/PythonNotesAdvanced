"""This file is to explain more details about classes in Python.

1. super() method:

It allows to call the parent class methods.
It is useful when you want to call the parent class methods in the child class.

2. __del__ method:

Remark with the custom message that it is always automatically called at the end of the program.
"""


class Human:

    _count = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Human._count += 1

    def __str__(self):
        return f"A human with Name: {self.name}, Age: {self.age}"

    def __del__(self):
        print(f"{self.name} is deleted.")
        Human._count -= 1

    @classmethod
    def get_population(cls):
        print("Checking population.")
        return cls._count

    @property
    def get_birth(self):
        print("Calculating birth year.")
        return 2025 - self.age


class Student(Human):
    def __init__(self, name: str, age: int, department: str):
        super().__init__(name, age)
        self.department = department

    def __str__(self):
        text = super().__str__()
        return text + f", Department: {self.department}"


person1 = Human("Kadir", 38)
person2 = Student("Emir", 23, "Mathematics")
print(person1)
print(person2)
print(person2.get_birth)
print(Human.get_population())
