class CounterMeta(type):

    count = 0

    def __new__(cls, name, bases, dct):
        klass = super().__new__(cls, name, bases, dct)
        cls.count += 1
        return klass


class Pie(metaclass=CounterMeta):
    pass


class Cake(metaclass=CounterMeta):
    pass


class Pastry(metaclass=CounterMeta):
    pass


class ApplePie(CounterMeta):
    # This class inherits from CounterMeta but does not use it as a metaclass.
    pass


apple_pie = Pie()
print(CounterMeta.count)  # 3
print(apple_pie.__class__.count)  # 3

