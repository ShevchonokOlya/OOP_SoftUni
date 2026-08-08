from abc import ABC, abstractmethod


class BaseArtifact(ABC):
    name: str
    price: float
    space_required: int

    def __init__(self, name: str, price: float, space_required: int):
        self.name = name
        self.price = price
        self.space_required = space_required

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError("Artifact name cannot be null or empty!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0.0:
            raise ValueError("Artifact price should be more than 0.0!")
        self.__price = value

    @property
    def space_required(self) -> int:
        return self.__space_required

    @space_required.setter
    def space_required(self, value: int) -> None:
        if value <  1 or value > 1000:
            raise ValueError("Space required for the artifact exhibition must be between 1 and 1000!")
        self.__space_required = value



    def artifact_information(self):
        type_of_art = str(self.__class__.__name__).replace("Artifact", "")
        return f"{type_of_art} Artifact: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}"

    @abstractmethod
    def __str__(self):
        pass