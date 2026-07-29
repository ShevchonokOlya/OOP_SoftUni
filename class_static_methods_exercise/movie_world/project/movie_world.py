from project import Customer
from project import DVD


class MovieWorld:
    __DVD_CAPACITY = 15
    __CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.__CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.__DVD_CAPACITY:
            self.dvds.append(dvd)

    def find_customer_by_id(self, customer_id: int) -> Customer | None:
        customer = next((cust for cust in self.customers if cust.id == customer_id), None)
        if customer:
            return customer
        return None

    def find_dvd_by_id(self, dvd_id: int) -> DVD | None:
        dvd = next((dvd for dvd in self.dvds if dvd.id == dvd_id), None)
        if dvd:
            return dvd
        return None

    def find_by_id(self, customer_id: int, dvd_id: int):
        c = self.find_customer_by_id(customer_id)
        d = self.find_dvd_by_id(dvd_id)
        return c, d

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer, dvd = self.find_by_id(customer_id, dvd_id)


        # if we have such customer
        if customer:

            # if this customer id already rented such dvd
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"

            # if customer age lower that restricted
            if customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        # If the DVD is rented by someone else

        if dvd.is_rented:
            return f"DVD is already rented"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer  , dvd = self.find_by_id(customer_id, dvd_id)
        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"

        return result.strip()


