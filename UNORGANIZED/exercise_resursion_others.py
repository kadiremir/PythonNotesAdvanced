
def power(num: int, power: int) -> int:
    if power < 0:
        raise ValueError("Negative power not implemented yet!")
    if power == 0:
        return 1
    actual_power = 1
    result = num
    while actual_power < power:
        result *= num
        actual_power += 1
    return result


def power_recursive(num: int, power: int) -> int:
    if power < 0:
        raise ValueError("Negative power not implemented yet!")
    if power == 0:
        return 1
    return num * power_recursive(num, power - 1)


def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Negative factorial not defined!")
    elif num == 0:
        return 1
    actual_number = 1
    result = 1
    while actual_number <= num:
        result *= actual_number
        actual_number += 1
    return result


def factorial_recursive(num: int) -> int:
    if num < 0:
        raise ValueError("Negative factorial not defined!")
    elif num == 0:
        return 1
    return num * factorial_recursive(num - 1)
    

print(power(2,8))
print(power_recursive(2,8))
print(factorial(5))
print(factorial_recursive(5))
