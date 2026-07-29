class ImageArea:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        self.__area = self.get_area()

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.__area == other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

#
#
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 == a2)
# print(a1 != a3)
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 != a2)
# print(a1 >= a3)
# a1 = ImageArea(7, 10)
# a2 = ImageArea(35, 2)
# a3 = ImageArea(8, 9)
# print(a1 <= a2)
# print(a1 < a3)

def start_playing(obj: object) -> object:
    return obj.play()


# class Guitar:
#     @staticmethod
#     def play():
#         return "Playing the guitar"
#
# guitar = Guitar()
# print(start_playing(guitar))
#
# class Children:
#     @staticmethod
#     def play():
#         return "Children are playing"
#
# children = Children()
# print(start_playing(children))


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def calculate_area(self):
        return pi * self.__radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def calculate_perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def calculate_area(self):
        return self.__width * self.__height

#
# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())



