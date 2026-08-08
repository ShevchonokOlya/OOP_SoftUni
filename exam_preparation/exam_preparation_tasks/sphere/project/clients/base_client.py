from abc import ABC, abstractmethod
from math import floor


class BaseClient(ABC):
    name: str
    membership_type: str
    points: int

    TYPE_OF_CLIENT = "Base"
    AVAILABLE_TYPES = {"Regular", "VIP"}
    POINT_FOR_SPENT_MONEY = 0

    def __init__(self, name: str, membership_type: str) -> None:
        self.name = name
        self.membership_type = membership_type
        self.points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == '':
            raise ValueError("Client name should be determined!")

        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.AVAILABLE_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value


    def earning_points(self, order_amount: float) -> int:
        points = floor(order_amount / self.POINT_FOR_SPENT_MONEY)
        self.points += points
        return points

    def apply_discount(self) -> tuple[int, int]:

        discount_percent = 0
        points = 0

        if self.points >= 100:
            discount_percent = 10
            points = 100
        elif self.points >= 50:
            discount_percent = 5
            points = 50

        self.points -= points

        return discount_percent, self.points
