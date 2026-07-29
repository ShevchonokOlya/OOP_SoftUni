from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTestCase(TestCase):
    def setUp(self) -> None:
        self.test_vehicle = Vehicle(15.0, 200.0)

    def test_type_of_property(self) -> None:
        self.assertIsInstance(self.test_vehicle.fuel, float)
        self.assertIsInstance(self.test_vehicle.capacity, float)
        self.assertIsInstance(self.test_vehicle.horse_power, float)
        self.assertIsInstance(self.test_vehicle.fuel_consumption, float)


    def test_init(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.assertEqual(15.0, self.test_vehicle.capacity )
        self.assertEqual(200.0, self.test_vehicle.horse_power)
        self.assertEqual(1.25, self.test_vehicle.fuel_consumption)

    def test_driving_need_exactly_available_amount_of_fuel(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.test_vehicle.drive(12)
        self.assertEqual(0.0, self.test_vehicle.fuel)

    def test_driving_enough_fuel(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.test_vehicle.drive(6)
        self.assertEqual(7.5, self.test_vehicle.fuel)

    def test_driving_not_enough_fuel_raises_exception(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        with self.assertRaises(Exception) as context:
            self.test_vehicle.drive(20)
        self.assertEqual("Not enough fuel", str(context.exception))
        self.assertEqual(15.0, self.test_vehicle.fuel)

    def test_refuel_correct_amount_of_fuel(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.test_vehicle.fuel = 3
        self.assertEqual(3.0, self.test_vehicle.fuel)
        self.assertEqual(15.0, self.test_vehicle.capacity)
        self.test_vehicle.refuel(6)
        self.assertEqual(9.0, self.test_vehicle.fuel)
        
    def test_refuel_exact_amount_of_fuel(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.test_vehicle.fuel = 10
        self.assertEqual(10.0, self.test_vehicle.fuel)
        self.assertEqual(15.0, self.test_vehicle.capacity)
        self.test_vehicle.refuel(5)
        self.assertEqual(15.0, self.test_vehicle.fuel)


    def test_refuel_raises_exception(self) -> None:
        self.assertEqual(15.0, self.test_vehicle.fuel)
        self.assertEqual(15.0, self.test_vehicle.capacity)
        with self.assertRaises(Exception) as context:
            self.test_vehicle.refuel(6)
        self.assertEqual("Too much fuel", str(context.exception))
        self.assertEqual(15.0, self.test_vehicle.fuel)

        
    def test_string_about_vehicle(self) -> None:
        expected_string = f"The vehicle has 200.0 " \
               f"horse power with 15.0 fuel left and 1.25 fuel consumption"
        result_string = self.test_vehicle.__str__()
        self.assertEqual(result_string, expected_string)


