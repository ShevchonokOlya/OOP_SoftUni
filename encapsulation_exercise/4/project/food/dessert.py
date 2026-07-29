from project import Food


class Dessert(Food):
    def __init__(self, name: str, price: float, grams: float, calories : float):
        super().__init__(name, price, grams)
        self.__calories: float = calories

    @property
    def calories(self):
        return self.__calories

