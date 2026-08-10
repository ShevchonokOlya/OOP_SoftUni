from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)


    @property
    def store_type(self) -> str:
       return "FurnitureStore"

    def store_stats(self):
       return self.store_starting("Furniture")







