import re
from abc import ABC, abstractmethod
from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):
    MONEY_INCREASES = 0
    name: str
    available_money: float
    available_space: int
    purchased_artifacts: list[BaseArtifact]

    def __init__(self,name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts = []

    @staticmethod
    def is_valid(text) -> bool:
        clean_text = text.strip()
        pattern = r"^[A-Za-z0-9 ]+$"
        return bool(re.search(pattern, clean_text))

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not self.is_valid(value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value


    @property
    def available_money(self) -> float:
        return self.__available_money

    @available_money.setter
    def available_money(self, value: float) -> None:
        if value < 0.0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self) -> int:
        return self.__available_space

    @available_space.setter
    def available_space(self, value: int) -> None:
        if  value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    def increase_money(self):
        self.available_money += self.MONEY_INCREASES

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if artifact_price <= self.available_money and artifact_space_required <= self.available_space:
            return True
        return False

    def __str__(self):
        artifact_string = ', '.join(art.name for art in sorted(self.purchased_artifacts, key=lambda x: x.name, reverse=True))
        if artifact_string == '':
            artifact_string = 'none'
        return f"Collector name: {self.name}; Money available: {self.available_money:.2f}; Space available: {self.available_space}; Artifacts: {artifact_string}"