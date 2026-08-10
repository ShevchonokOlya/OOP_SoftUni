from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct


class BaseStore(ABC):
    name: str
    location: str
    capacity: int
    products: list

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products : list[BaseProduct] =  []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == '':
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str) or len(value) != 3 or ' ' in value:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self) -> str:
        profit = 0.00
        for prod in self.products:
            profit += prod.price
        products_count = len(self.products)
        return f"Estimated future profit for {products_count} products is {(profit* 0.1):.2f}"

    @property
    @abstractmethod
    def store_type(self) -> str:
        pass

    @abstractmethod
    def store_stats(self):
        pass

    def store_starting(self, type_of_product: str):
        result = (f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                  f"{self.get_estimated_profit()}\n")

        furniture_string = f'**{type_of_product} for sale:'
        dict_of_products = {}
        for item in self.products:
            dict_of_products.setdefault(item.model, [0, 0.0])
            dict_of_products[item.model][0] += 1
            dict_of_products[item.model][1] +=  item.price


        for fur_key, fur_value in sorted(dict_of_products.items()):
            furniture_string += f'\n{fur_key}: {fur_value[0]}pcs, average price: {(fur_value[1]/fur_value[0]):.2f}'

        return result + furniture_string
