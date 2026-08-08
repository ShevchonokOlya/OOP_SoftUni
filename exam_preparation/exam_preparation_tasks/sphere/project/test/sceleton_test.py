import unittest
import inspect
from abc import ABC

# Imports according to the project folder structure
from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.sphere_restaurant_app import SphereRestaurantApp


class TestSkeleton(unittest.TestCase):

    # --- Testing abstract base classes ---

    def test_base_client_is_abstract(self):
        """Check if BaseClient is an abstract class"""
        self.assertTrue(issubclass(BaseClient, ABC), "BaseClient should inherit from ABC.")
        # self.assertTrue(inspect.isabstract(BaseClient), "BaseClient should be an abstract class.")
        # self.assertIn('earning_points', BaseClient.__abstractmethods__, "The earning_points method should be abstract.")

    def test_base_waiter_is_abstract(self):
        """Check if BaseWaiter is an abstract class"""
        self.assertTrue(issubclass(BaseWaiter, ABC), "BaseWaiter should inherit from ABC.")
        self.assertTrue(inspect.isabstract(BaseWaiter), "BaseWaiter should be an abstract class.")
        self.assertIn('report_shift', BaseWaiter.__abstractmethods__, "The report_shift method should be abstract.")

    # --- Testing encapsulation and validation (Exceptions) ---

    def test_client_encapsulation_name(self):
        """Check client name validation"""
        client = RegularClient("Valid Name")

        with self.assertRaises(ValueError) as context:
            client.name = "   "
        self.assertEqual(str(context.exception), "Client name should be determined!")

        with self.assertRaises(ValueError) as context:
            client.name = ""
        self.assertEqual(str(context.exception), "Client name should be determined!")

    def test_client_encapsulation_membership(self):
        """Check client membership type validation"""
        client = RegularClient("Valid Name")

        with self.assertRaises(ValueError) as context:
            client.membership_type = "Gold"
        self.assertEqual(str(context.exception), "Invalid membership type. Allowed types: Regular, VIP.")

    def test_waiter_encapsulation_name(self):
        """Check waiter name validation"""
        waiter = FullTimeWaiter("Valid Name", 10)

        with self.assertRaises(ValueError) as context:
            waiter.name = "Bo"  # Length is 2
        self.assertEqual(str(context.exception), "Waiter name must be between 3 and 50 characters in length!")

    def test_waiter_encapsulation_hours(self):
        """Check waiter working hours validation"""
        waiter = HalfTimeWaiter("Valid Name", 10)

        with self.assertRaises(ValueError) as context:
            waiter.hours_worked = -5
        self.assertEqual(str(context.exception), "Cannot have negative hours worked!")

    # --- Testing main class structure ---

    def test_sphere_restaurant_app_structure(self):
        """Check proper initialization and presence of application methods"""
        app = SphereRestaurantApp()

        # Check initial values of collections
        self.assertEqual(app.waiters, [], "The waiters collection should be an empty list upon initialization.")
        self.assertEqual(app.clients, [], "The clients collection should be an empty list upon initialization.")

        # Check for the presence of all required methods
        methods_to_check = [
            'hire_waiter',
            'admit_client',
            'process_shifts',
            'process_client_order',
            'apply_discount_to_client',
            'generate_report'
        ]

        for method in methods_to_check:
            self.assertTrue(hasattr(app, method), f"SphereRestaurantApp is missing the '{method}' method.")
            self.assertTrue(callable(getattr(app, method)), f"The '{method}' attribute should be callable.")


if __name__ == "__main__":
    unittest.main()