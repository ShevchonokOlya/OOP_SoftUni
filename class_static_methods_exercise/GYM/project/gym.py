from project import Customer
from project import Equipment
from project import ExercisePlan
from project import Subscription
from project import Trainer


class Gym:
    def __init__(self):
         self.customers : list[Customer] = []
         self.trainers : list[Trainer] = []
         self.equipment : list[Equipment] = []
         self.plans : list[ExercisePlan] = []
         self.subscriptions : list[Subscription] = []

    @staticmethod
    def _add_instance(inst, target_list : list) -> None:
        if inst not in target_list:
            target_list.append(inst)

    def  add_customer(self, customer: Customer)-> None:
        self._add_instance(customer, self.customers)

    def add_trainer(self, trainer: Trainer) -> None:
        self._add_instance(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment) -> None:
        self._add_instance(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        self._add_instance(plan, self.plans)

    def add_subscription(self, subscription: Subscription) -> None:
        self._add_instance(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):

        subscription = next((subs for subs in self.subscriptions if subscription_id == subs.id), None)
        if subscription:
            customer = next((cus for cus in self.customers if cus.id == subscription.customer_id ), None )
            trainer = next((tr for tr in self.trainers if tr.id == subscription.trainer_id ), None)
            plan = next((pl for pl in self.plans if pl.id == subscription.exercise_id and pl.trainer_id == subscription.trainer_id  ), None)
            equipment_id = plan.equipment_id
            equipment = next((eq for eq in self.equipment if eq.id == equipment_id ), None)

            return f"{str(subscription)}\n{str(customer)}\n{str(trainer)}\n{str(equipment)}\n{str(plan)}"
        return f"No subscription found"
