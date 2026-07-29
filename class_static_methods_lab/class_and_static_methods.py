
from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)
    @staticmethod

    def multiply(*args):
        return reduce(lambda x, y: x * y, args)
    @staticmethod
    def divide(*args) :
        return reduce(lambda x, y: x / y, args)
    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))

class Shop:
    def __init__(self, name: str, product_type: str, capacity: int):
        self.name = name
        self.type = product_type
        self.capacity = capacity
        self.items : dict = {}

    @classmethod
    def small_shop(cls, name: str, product_type: str):
        return cls(name , product_type, 10 )

    def add_item(self, item_name: str):
        if item_name not in self.items.keys():
            self.items[item_name] = 1
            return f"{item_name} added to the shop"

        if self.items[item_name] < self.capacity:
             self.items[item_name] += 1
             return f"{item_name} added to the shop"

        return f"Not enough capacity in the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name in self.items.keys() and amount <=  self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                self.items.pop(item_name)
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


# fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
# small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
# print(fresh_shop)
# print(small_shop)
#
# print(fresh_shop.add_item("Bananas"))
# print(fresh_shop.remove_item("Tomatoes", 2))
#
# print(small_shop.add_item("Jeans"))
# print(small_shop.add_item("Jeans"))
# print(small_shop.remove_item("Jeans", 2))
# print(small_shop.items)

from math import floor
class Integer:

    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def value_from_roman(roman: str):
        if roman == 'I':
            return 1
        if roman == 'V':
            return 5
        if roman == 'X':
            return 10
        if roman == 'L':
            return 50
        if roman == 'C':
            return 100
        if roman == 'D':
            return 500
        if roman == 'M':
            return 1000
        return -1

    @classmethod
    def from_float(cls, float_value: str):
        if type(float_value) != float:
            return "value is not a float"
        return cls(floor(float(float_value)))

    @classmethod
    def from_roman(cls, value: str):
        result = 0
        list_of_numbers = []

        for letter in value:
            list_of_numbers.append(cls.value_from_roman(letter))


        for i in range(len(list_of_numbers) -1):
            s1 = list_of_numbers[i]
            if i + 1 < len(list_of_numbers):
                s2 =  list_of_numbers[i + 1]
                if s1 >= s2:
                    result = result + s1
                    i = i + 1
                else:
                    result += s2 - s1
                    i = i + 2
            else:
                result += s1
                i = i + 1

        return cls(result)


    @classmethod
    def from_string(cls, value: str):
        if type(value) != str:
            return "wrong type"
        else:

            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"

