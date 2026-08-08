from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    name: str
    hours_worked: int
    HOURLY_RATE: int

    def __init__(self, name: str, hours_worked: int) -> None:
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (3 <= len(value) <= 50):
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")

        self.__name = value


    @property
    def hours_worked(self):
        return self.__hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0 :
            raise ValueError("Cannot have negative hours worked!")
        self.__hours_worked = value


    def calculate_earnings(self)-> float:
        return self.hours_worked * self.HOURLY_RATE

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self):
        total_earnings = self.calculate_earnings()
        return f"Name: {self.name}, Total earnings: ${total_earnings:.2f}"
