from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    name: str
    income: float
    products: list
    stores: list

    AVAILABLE_STORES = {'FurnitureStore': FurnitureStore,
                        'ToyStore': ToyStore
                        }
    AVAILABLE_PRODUCTS = { "Chair": Chair,
                          "HobbyHorse": HobbyHorse
                          }

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):

        if product_type not in self.AVAILABLE_PRODUCTS:
            raise Exception("Invalid product type!")

        product = self.AVAILABLE_PRODUCTS[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."



    def register_new_store(self, store_type: str, name: str, location: str):

        if store_type not in self.AVAILABLE_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.AVAILABLE_STORES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."


    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        else:
            items_to_sell = []
            for prod in products:
                store_type = 'Furniture' if store.store_type =='FurnitureStore' else 'Toys'
                if store_type == prod.sub_type:
                    items_to_sell.append(prod)
            if len(items_to_sell) == 0:
                return f"Products do not match in type. Nothing sold."
            for item in items_to_sell:
                store.products.append(item)
                if item in self.products:
                    self.products.remove(item)
                    self.income += item.price

            store.capacity -= len(items_to_sell)
            return f"Store {store.name} successfully purchased {len(items_to_sell)} items."



    def unregister_store(self, store_name: str):
        target_store = next(filter(lambda store: store.name == store_name, self.stores), None)
        if target_store:
            if len(target_store.products) > 0:
                return "The store is still having products in stock! Unregistering is inadvisable."
            self.stores.remove(target_store)
            return f"Successfully unregistered store {store_name}, location: {target_store.location}."

        else:
            raise Exception("No such store!")

    def discount_products(self, product_model: str):
        products_count = 0
        for prod in self.products:
            if prod.model == product_model:
                prod.discount()
                products_count += 1
        return f"Discount applied to {products_count} products with model: {product_model}"


    def request_store_stats(self, store_name: str):
        target_store = next(filter(lambda store: store.name == store_name, self.stores), None)
        if  target_store:
            return target_store.store_stats()
        return "There is no store registered under this name!"


    def statistics(self):
        result_string = f"Factory: {self.name}\nIncome: {self.income:.2f}\n***Products Statistics***"
        total_price = sum([pr.price for pr in self.products])
        product_string = f"\nUnsold Products: {len(self.products)}. Total net price: {total_price:.2f}"

        models_list = [product.model for product in self.products]
        model_set = set(models_list)
        for model in sorted(model_set):
            product_string += f"\n{model}: {models_list.count(model)}"
        stores_string = f"\n***Partner Stores: {len(self.stores)}***"
        for store in sorted(self.stores, key=lambda x: x.name):
            stores_string += f"\n{store.name}"

        return result_string + product_string + stores_string







