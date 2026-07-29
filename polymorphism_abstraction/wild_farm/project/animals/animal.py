from abc import ABC, abstractmethod

from project import food
from project import Food


class Animal(ABC):
    WEIGHT = 0.0
    TYPE_OF_FOOD = []

    def __init__(self, name: str, weight: float, food_eaten: float = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, feed_food: Food) -> str | None:
        food_name = type(feed_food).__name__
        if food_name not in self.TYPE_OF_FOOD:
            return f"{type(self).__name__} does not eat {type(feed_food).__name__}!"
        self.weight += self.WEIGHT * feed_food.quantity
        self.food_eaten += feed_food.quantity
        return None


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float,  living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__ } [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal, ABC):
    TYPE_OF_FOOD = []
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
