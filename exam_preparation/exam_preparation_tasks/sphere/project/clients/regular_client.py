from math import floor

from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    TYPE_OF_CLIENT = "Regular"
    POINT_FOR_SPENT_MONEY = 10

    def __init__(self, name: str):
        super().__init__(name, self.TYPE_OF_CLIENT)

    # def earning_points(self, order_amount: float) -> int:
    #     points = floor(order_amount/self.POINT_FOR_SPENT_MONEY)
    #     self.points += points
    #     return   points

