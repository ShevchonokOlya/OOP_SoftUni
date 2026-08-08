import unittest
from math import floor
# Предполагаем, что структура проекта соответствует заданию (папка project)
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.sphere_restaurant_app import SphereRestaurantApp


class TestSphereRestaurantApp(unittest.TestCase):

    def setUp(self):
        self.app = SphereRestaurantApp()

    # --- ТЕСТЫ ВАЛИДАЦИИ (BaseClient / BaseWaiter) ---

    def test_client_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            RegularClient("")
        self.assertEqual(str(ve.exception), "Client name should be determined!")

        with self.assertRaises(ValueError) as ve:
            VIPClient("   ")
        self.assertEqual(str(ve.exception), "Client name should be determined!")

    def test_waiter_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            FullTimeWaiter("Jo", 40)  # Слишком короткое
        self.assertEqual(str(ve.exception), "Waiter name must be between 3 and 50 characters in length!")

    def test_waiter_hours_validation(self):
        with self.assertRaises(ValueError) as ve:
            HalfTimeWaiter("John", -1)
        self.assertEqual(str(ve.exception), "Cannot have negative hours worked!")

    # --- ТЕСТЫ ЛОГИКИ КЛИЕНТОВ (Points & Discounts) ---

    def test_regular_client_points(self):
        client = RegularClient("Bob")
        points = client.earning_points(109.9)  # 109.9 / 10 = 10.99 -> floor = 10
        self.assertEqual(points, 10)
        self.assertEqual(client.points, 10)

    def test_vip_client_points(self):
        client = VIPClient("Eve")
        points = client.earning_points(104.0)  # 104 / 5 = 20.8 -> floor = 20
        self.assertEqual(points, 20)
        self.assertEqual(client.points, 20)

    def test_apply_discount_logic(self):
        client = VIPClient("Lila")

        # 0% discount
        client.points = 40
        disc, rem = client.apply_discount()
        self.assertEqual((disc, rem), (0, 40))

        # 5% discount
        client.points = 60
        disc, rem = client.apply_discount()
        self.assertEqual((disc, rem), (5, 10))

        # 10% discount
        client.points = 115
        disc, rem = client.apply_discount()
        self.assertEqual((disc, rem), (10, 15))

    # --- ТЕСТЫ ПРИЛОЖЕНИЯ (SphereRestaurantApp) ---

    def test_hire_waiter_functionality(self):
        res = self.app.hire_waiter("FullTimeWaiter", "John", 40)
        self.assertEqual(res, "John is successfully hired as a FullTimeWaiter.")

        # Duplicate
        res = self.app.hire_waiter("FullTimeWaiter", "John", 20)
        self.assertEqual(res, "John is already on the staff.")

        # Invalid type
        res = self.app.hire_waiter("Manager", "Smith", 40)
        self.assertEqual(res, "Manager is not a recognized waiter type.")

    def test_process_client_order(self):
        self.app.admit_client("RegularClient", "Bob")
        res = self.app.process_client_order("Bob", 100.0)
        self.assertEqual(res, "Bob earned 10 points from the order.")

        # Unregistered
        res = self.app.process_client_order("Unknown", 100.0)
        self.assertEqual(res, "Unknown is not a registered client.")

    def test_apply_discount_to_client_output(self):
        self.app.admit_client("VIPClient", "Eve")
        client = self.app.clients[0]
        client.points = 120

        res = self.app.apply_discount_to_client("Eve")
        # 10% discount, 120-100 = 20 remaining
        self.assertEqual(res, "Eve received a 10% discount. Remaining points 20")

    def test_generate_report_sorting(self):
        self.app.hire_waiter("FullTimeWaiter", "John", 10)  # 150.0
        self.app.hire_waiter("HalfTimeWaiter", "Alice", 20)  # 240.0
        self.app.admit_client("RegularClient", "Bob")
        self.app.clients[0].points = 5

        report = self.app.generate_report()

        # Проверка сортировки: Alice (240) должна быть выше John (150)
        self.assertTrue(report.find("Alice") < report.find("John"))
        self.assertIn("Total Earnings: $390.00", report)
        self.assertIn("Total Clients Unused Points: 5", report)
        self.assertIn("Total Clients Count: 1", report)


if __name__ == "__main__":
    unittest.main()