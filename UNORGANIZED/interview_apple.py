
# Write a function to sum the integers from 1 to n

# Write a function to sum only the even integers from 1 to n

class MyClass:
    my_variable = 1

    def __init__(self):
        self.my_variable = {1:2, 3:5, 4:6}


class YourClass(MyClass):
    def __init__(self):
        self.my_variable = {3:7}
        super().__init__()
        self.my_variable[3] += 1

## 1. Explain the code...

## 2. What would be the output of (without running it):
print(MyClass.my_variable)
print(MyClass().my_variable)
print(YourClass().my_variable)
print(YourClass().my_variable[3] + MyClass.my_variable)
