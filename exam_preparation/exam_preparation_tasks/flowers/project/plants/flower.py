from project.plants.base_plant import BasePlant

class Flower(BasePlant):
    blooming_season: str
    VALID_SEASONS = ['Spring', 'Summer',  'Fall','Winter']


    def __init__(self, name: str, price: float, water_needed: int, blooming_season : str ) -> None:
        super().__init__(name, price, water_needed)
        self.blooming_season = blooming_season

    @property
    def blooming_season(self) -> str:
        return self.__blooming_season

    @blooming_season.setter
    def blooming_season(self, value: str) -> None:
        if not isinstance(value, str) or value not in Flower.VALID_SEASONS:
            raise ValueError("Blooming season must be a valid one!")
        self.__blooming_season = value

    def plant_details(self) -> str:
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Blooming Season: {self.blooming_season}"

