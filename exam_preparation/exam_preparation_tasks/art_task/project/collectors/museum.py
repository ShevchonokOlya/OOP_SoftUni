from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    MONEY_INCREASES = 1_000.0
    AVAILABLE_M = 15_000.0
    AVAILABLE_S = 2_000

    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_M , self.AVAILABLE_S)




