from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    income: float
    plants: list
    clients: list

    VALID_PLANTS_TYPES: dict = {"Flower": Flower,
                                "LeafPlant": LeafPlant}

    VALID_CLIENT_TYPES: dict = {"RegularClient": RegularClient,
                                "BusinessClient": BusinessClient}

    def __init__(self):
        self.income = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS_TYPES.keys():
            raise ValueError("Unknown plant type!")
        plant = self.VALID_PLANTS_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENT_TYPES.keys():
            raise ValueError("Unknown client type!")
        if client_phone_number in (cl.phone_number for cl in self.clients):
            raise ValueError("This phone number has been used!")

        new_client = self.VALID_CLIENT_TYPES[client_type](client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        target_client = next((cl for cl in self.clients if cl.phone_number == client_phone_number), None)
        if not target_client:
            raise ValueError("Client not found!")

        pl_dict = {}
        for pl in self.plants:
            pl_dict[pl.name] = pl_dict.get(pl.name, 0) + 1

        target_plant = next((pl for pl in self.plants if pl.name == plant_name), None)

        if not target_plant:
            raise ValueError("Plants not found!")
        elif pl_dict[plant_name] < plant_quantity:
            return f"Not enough plant quantity."

        for _ in range(plant_quantity):
            self.remove_plant(plant_name)

        order_amount = plant_quantity * target_plant.price * (100 - target_client.discount) / 100

        self.income += order_amount
        target_client.update_total_orders()
        target_client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        target_plant =  next((pl for pl in self.plants if pl.name == plant_name), None)
        if not target_plant:
            return "No such plant name."
        self.plants.remove(target_plant)

        return f"Removed {target_plant.plant_details()}"

    def remove_clients(self):
        clients = list(filter(lambda x: x.total_orders == 0, self.clients))
        counter = len(clients)
        for client in clients:
            self.clients.remove(client)
        return f"{counter} client/s removed."

    def shop_report(self):
        orders = sum(item.total_orders for item in self.clients)
        result_string = (f"~Flower Shop Report~\nIncome: {self.income:.2f}\n"
                         f"Count of orders: {orders}\n")

        plats = f'~~Unsold plants: {len(self.plants)}~~'

        pl_dict = {}
        for pl in self.plants:
            pl_dict[pl.name] = pl_dict.get(pl.name, 0) + 1

        for plant in sorted(pl_dict.items(), key=lambda x: (-x[1], x[0])):
            plats += f"\n{plant[0]}: {plant[1]}"

        clients_string = f'\n~~Clients number: {len(self.clients)}~~'
        for client in sorted(self.clients, key=lambda x:( -x.total_orders, x.phone_number)):
            clients_string += f"\n{client.client_details()}"

        return result_string + plats + clients_string
