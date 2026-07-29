from abc import ABC, abstractmethod
class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def team_money(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors, expenses = self.team_money
        rev = 0
        for sponsor in sponsors.values():
            for pos, amount in sponsor.items():
                if race_pos <= pos:
                    rev += amount
                    break
        rev -= expenses
        self.budget += rev

        return f"The revenue after the race is {rev}$. Current budget {self.budget}$"
