class Mouse(Mammal):
    WEIGHT = 0.1
    TYPE_OF_FOOD = ['Vegetable', 'Fruit']
    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    WEIGHT = 0.4
    TYPE_OF_FOOD = ['Meat']
    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    WEIGHT = 0.3
    TYPE_OF_FOOD = ['Vegetable', 'Meat']
    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    WEIGHT = 1.0
    TYPE_OF_FOOD = ['Meat']
    def make_sound(self) -> str:
        return "ROAR!!!"


