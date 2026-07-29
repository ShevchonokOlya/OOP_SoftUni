def logged(function):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([str(a) for a in args])
        arg_str += ', '.join([str(a) for a in kwargs])
        name_of_func = function.__name__ + '('+ arg_str + ')'
        return f"you called {name_of_func}\nit returned {function(*args, **kwargs)}"
    return wrapper


#
# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))
#
#
# @logged
# def sum_func(a, b):
#     return a + b
# print(sum_func(1, 4))
#
#
# # test zero
# import unittest
#
# class LoggedTests(unittest.TestCase):
#     def test_zero(self):
#         @logged
#         def func(*args):
#             return 3 + len(args)
#         result = func(4, 4, 4)
#         self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')
#
# if __name__ == '__main__':
#     unittest.main()

def even_parameters(function):
    def wrapper(*args, **kwargs):
        args = list(args) + list(kwargs.values())
        for arg in args:
            if not isinstance(arg, int) or arg % 2 == 1:
                return f"Please use only even numbers!"
        return function(*args, **kwargs)
    return wrapper


#import unittest
# class EvenParametersTests(unittest.TestCase):
#     def test_even(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, 4, 4)
#         self.assertEqual(result, 12)
#
#     def test_odd(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, 5, 4)
#         self.assertEqual(result, "Please use only even numbers!")
#
#     def test_with_non_integer_params(self):
#         @even_parameters
#         def func(*args):
#             return sum(args)
#
#         result = func(4, "4", 4)
#         self.assertEqual(result, "Please use only even numbers!")
#
#     def test_with_no_params(self):
#         @even_parameters
#         def func():
#             return "hi"
#
#         result = func()
#         self.assertEqual(result, "hi")
#
#
# if __name__ == '__main__':
#     unittest.main()



# @even_parameters
# def add(a, b):
#     return a + b
#
# print(add(2, 4))
# print(add("Peter", 1))
#
# @even_parameters
# def multiply(*nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result
#
# print(multiply(2, 4, 6, 8))
# print(multiply(2, 4, 9, 8))

def make_bold(function):
    return _html_helper(function, 'b')

def make_italic(function):
    return _html_helper(function, 'i')

def make_underline(function):
    return _html_helper(function, 'u')

def _html_helper(func, tag):
    def wrapper(*args):
        return f"<{tag}>{func(*args)}</{tag}>"
    return wrapper

#
#
# @make_bold
# @make_italic
# @make_underline
# def greet(name):
#     return f"Hello, {name}"
#
# print(greet("Peter"))
#
# @make_bold
# @make_italic
# @make_underline
# def greet_all(*args):
#     return f"Hello, {', '.join(args)}"
#
# print(greet_all("Peter", "George"))

def type_check(type_of_argument):
    def decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_of_argument):
                    return "Bad Type"
            return function(*args)
        return wrapper
    return decorator
#
# @type_check(int)
# def times2(num):
#     return num*2
# print(times2(2))
# print(times2('Not A Number'))
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
# print(first_letter('Hello World'))
# print(first_letter(['Not', 'A', 'String']))


def cache(func):

    def wrapper(n):
        if wrapper.log.get(n) is None:
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = {}
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#
# fibonacci(3)
# print(fibonacci.log)
# fibonacci(4)
# print(fibonacci.log)
#


def tags(letter):
    def decorator(function):
        def wrapper(*args):
            return f"<{letter}>{function(*args)}</{letter}>"
        return wrapper
    return decorator

# @tags('p')
# def join_strings(*args):
#     return "".join(args)
# print(join_strings("Hello", " you!"))
#
# @tags('h1')
# def to_upper(text):
#     return text.upper()
# print(to_upper('hello'))

class store_result:
    def __init__(self, file_name):
        self.file_name = file_name

    def __call__(self, function):
        def wrapper(*args):
            with open(self.file_name , 'w') as f:
                f.seek(0)
                f.write(f"Function {function.__name__} was called. Result: {function(*args)}\n")

        return wrapper


class store_results:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        with open('results.txt' , 'w') as f:
            f.seek(0)
            f.write(f"Function {self.function.__name__} was called. Result: {self.function(*args)}\n")



# @store_result('result.txt')
# def add(a, b):
#     return a + b
#
# @store_results
# def mult(a, b):
#     return a * b
#
# add(2, 2)
# mult(6, 4)

from time import time
def exec_time(function):
    def wrapper(*args):
        start_time =  time()
        function(*args)
        end_time =  time()
        return end_time - start_time
    return wrapper

#
# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
# print(loop(1, 10000000))
#
# @exec_time
# def concatenate(strings):
#     result = ""
#     for string in strings:
#         result += string
#     return result
# print(concatenate(["a" for i in range(1000000)]))
#
# @exec_time
# def loop():
#     count = 0
#     for i in range(1, 9999999):
#         count += 1
# print(loop())


my_string = "     ".strip()
if not my_string  :
    print("string \'\' => if not my_string")

if my_string is not None:
    print("string \'\' is not None")
