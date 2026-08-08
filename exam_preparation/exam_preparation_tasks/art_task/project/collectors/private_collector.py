from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    MONEY_INCREASES = 5000.0
    AVAILABLE_M = 25_000.0
    AVAILABLE_S = 3_000

    def __init__(self, name: str):
        super().__init__(name, self.AVAILABLE_M, self.AVAILABLE_S)


