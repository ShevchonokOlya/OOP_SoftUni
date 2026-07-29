from unittest import result


def number_increment(numbers):
    def increase():
      return [el+ 1 for el in numbers]
    return increase()

# print(number_increment([1, 2, 3]))

def vowel_filter(function):
    def wrapper():
        return [el for el in function() if el.lower() in 'aeiouy']
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

# print(get_letters())

def even_numbers(function):
    def wrapper(*args):
        return [el for el in function(*args) if el % 2 == 0]

    return wrapper

# @even_numbers
# def get_numbers(numbers):
#     return numbers
# print(get_numbers([1, 2, 3, 4, 5]))


def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs) * times
        return wrapper

    return decorator

# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))