from project import Animal
from project import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []


    def add_animal(self, animal, price: int) -> str:
        if self.__budget >= price:

            if len(self.animals) < self.__animal_capacity:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"


    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"



    def pay_workers(self) -> str:
        salaries = sum([w.salary for w in self.workers])

        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return  "You have no budget to pay your workers. They are unhappy"


    def tend_animals(self) -> str:
        tending = sum(animal.money_for_care for animal in self.animals)
        if self.__budget >= tending:
            self.__budget -= tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."


    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        for species in ["Lion", "Tiger", "Cheetah"]:

            species_list = [a for a in self.animals if a.__class__.__name__ == species]
            result.append(f"----- {len(species_list)} {species}s:")
            result.extend([repr(a) for a in species_list])

        return "\n".join(result).strip()


    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        for personal in ["Keeper", "Caretaker", "Vet"]:
            species_pers_list = [a for a in self.workers if a.__class__.__name__ == personal]
            result.append(f"----- {len(species_pers_list)} {personal}s:")
            result.extend([repr(a) for a in species_pers_list])

        return "\n".join(result).strip()
