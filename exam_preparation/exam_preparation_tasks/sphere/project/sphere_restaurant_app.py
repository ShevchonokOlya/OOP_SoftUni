from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    waiters: list
    clients: list
    VALID_WAITERS = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter
    }

    VALID_CLIENTS = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient
    }
    AVAILABLE_WAITER_TYPES = { "FullTimeWaiter" : "full-time" ,
                               "HalfTimeWaiter" : "half-time" ,
                               }

    def __init__(self) -> None:
        self.waiters: list[HalfTimeWaiter | FullTimeWaiter] = []
        self.clients: list[VIPClient | RegularClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str | None:
        if waiter_type not in self.AVAILABLE_WAITER_TYPES.keys():
            return f"{waiter_type} is not a recognized waiter type."

        if any(w.name == waiter_name for w in self.waiters):
            return f"{waiter_name} is already on the staff."

        waiter = self.VALID_WAITERS[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENTS:
            return f"{client_type} is not a recognized client type."

        if any(c.name == client_name for c in self.clients):
            return f"{client_name} is already a client."

        client = self.VALID_CLIENTS[client_type](client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next((waiter for waiter in self.waiters if waiter.name == waiter_name), None)

        if waiter:
            return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."



    def process_client_order(self, client_name: str, order_amount: float):
        client = next((client for client in self.clients if client.name == client_name), None)

        if client:
            return f"{client_name} earned {client.earning_points(order_amount)} points from the order."


        return f"{client_name} is not a registered client."


    def apply_discount_to_client(self, client_name: str):
        client = next((client for client in self.clients if client.name == client_name), None)
        if client:
            discount_percentage, remaining_points = client.apply_discount()
            return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"


    def generate_report(self):
        waiter_details = ''
        total_earnings = 0.0
        for waiter in sorted(self.waiters, key=lambda waiter_info: waiter_info.calculate_earnings(), reverse=True):
            total_earnings += waiter.calculate_earnings()
            waiter_details += f"\n{str(waiter)}"

        total_client_points = sum([client.points for client in self.clients])

        result_string = f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\n"\
                        f"Total Clients Unused Points: {total_client_points}\n"\
                        f"Total Clients Count: {len(self.clients)}\n"\
                        f"** Waiter Details **{waiter_details}"

        return result_string

