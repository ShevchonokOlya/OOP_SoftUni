from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    TYPE_OF_CLIENT = "VIP"
    POINT_FOR_SPENT_MONEY = 5

    def __init__(self, name: str):
        super().__init__(name, self.TYPE_OF_CLIENT)

    # def earning_points(self, order_amount: float) -> int:
    #     pass

