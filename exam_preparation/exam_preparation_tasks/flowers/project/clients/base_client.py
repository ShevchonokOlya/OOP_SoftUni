from abc import ABC, abstractmethod
from math import floor


class BaseClient(ABC):
    name: str
    phone_number: str
    discount: float
    total_orders: int

    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
        self.discount = 0.0 # discount in percentage (%)
        self.total_orders = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Name must be at least two characters long!")
        self.__name = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit():
            raise ValueError("Phone number can contain only digits!")

        self.__phone_number = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        # if not (0 <= value <= 100):
        #     raise ValueError("discount needed must be between 1 and 100%!")
        self.__discount = value

    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1

    def client_details(self):
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {floor(self.discount)}%"


