from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES: dict[str, type[Computer]] = {"Laptop": Laptop,
                                                       "Desktop Computer": DesktopComputer}

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        computer = self.VALID_COMPUTER_TYPES[type_computer](manufacturer, model)
        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int) -> str:

        computer = next((comp for comp in self.warehouse
                         if comp.processor == wanted_processor
                         and comp.ram >= wanted_ram
                         and comp.price <= client_budget), None)
        if computer is None:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)

        return f"{repr(computer)} sold for {client_budget}$."
