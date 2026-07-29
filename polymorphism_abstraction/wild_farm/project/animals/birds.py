class Owl(Bird):
    WEIGHT = 0.25
    TYPE_OF_FOOD = ['Meat']
    def make_sound(self) -> str:
        return "Hoot Hoot"


class Hen(Bird):
    WEIGHT = 0.35
    TYPE_OF_FOOD = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    def make_sound(self) -> str:
        return "Cluck"
