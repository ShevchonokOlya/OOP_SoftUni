from project import Animal

class Dog(Animal):
    @staticmethod
    def bark(self) -> str:
        return  "barking..."