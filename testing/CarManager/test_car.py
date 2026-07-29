from testing.CarManager.car_manager import Car
from unittest import TestCase, main



class testCar(TestCase):
    def setUp(self):
        self.testCar = Car("VW", "Touareg", 7.4, 85 )
        self.testCar2 = Car("Mercedes-Benz", "E220d", 4.9, 66)

    def test_car_initialization(self):
        self.assertEqual("VW",  self.testCar.make)
        self.assertEqual("Touareg",  self.testCar.model)
        self.assertEqual(7.4, self.testCar.fuel_consumption)
        self.assertEqual(85, self.testCar.fuel_capacity)
        self.assertEqual(0, self.testCar.fuel_amount)

        self.assertEqual("Mercedes-Benz", self.testCar2.make)
        self.assertEqual("E220d", self.testCar2.model)
        self.assertEqual(4.9, self.testCar2.fuel_consumption)
        self.assertEqual(66, self.testCar2.fuel_capacity)
        self.assertEqual(0, self.testCar2.fuel_amount)

    def test_make_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            Car(None,"Touareg", 7.4, 85 )
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("", "Touareg", 7.4, 85)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_None_raises(self):

        with self.assertRaises(Exception) as ex:
            Car("EmptyModel",None, 7.4, 85 )
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("EmptyModel","", 7.4, 85 )
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_negative_number_and_zero_raises(self):

        with self.assertRaises(Exception) as ex:
            Car("Fuel less then zero","Touareg", -123, 85 )
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("Fuel is zero","Touareg", 0, 85 )
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_negative_number_and_zero_raises(self):

        with self.assertRaises(Exception) as ex:
            Car("Fuel capacity negative number", "Touareg", 7.4, -0.6)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            Car("Fuel capacity is zero", "Touareg", 7.4, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_number_raises(self):
       self.assertEqual(0, self.testCar.fuel_amount)
       with self.assertRaises(Exception) as ex:
           self.testCar.fuel_amount = -10

       self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_capacity_less_or_zero_raises(self):
        fuel_amount_before = self.testCar.fuel_amount
        with self.assertRaises(Exception) as ex:
            self.testCar.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.assertEqual(fuel_amount_before, self.testCar.fuel_amount)


        with self.assertRaises(Exception) as ex:
            self.testCar.refuel(0.0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(fuel_amount_before, self.testCar.fuel_amount)

    def test_refuel_correct_was10_add10_become20_car1_raises(self):

        self.testCar.fuel_amount = 10
        self.assertEqual(10, self.testCar.fuel_amount)
        fuel_amount_before_refueling = self.testCar.fuel_amount
        fuel_for_refile = 10

        fuel_expected =  min(fuel_amount_before_refueling + fuel_for_refile, self.testCar.fuel_capacity)
        self.testCar.refuel(fuel_for_refile)


        self.assertEqual(fuel_expected, self.testCar.fuel_amount)

    def test_refuel_correct_was0_add40_become40_car1_raises(self):
        self.assertEqual(0, self.testCar.fuel_amount)
        fuel_amount_before_refueling = self.testCar.fuel_amount
        fuel_for_refile = 40

        fuel_expected = min(fuel_amount_before_refueling + fuel_for_refile, self.testCar.fuel_capacity)
        self.testCar.refuel(fuel_for_refile)

        self.assertEqual(fuel_expected, self.testCar.fuel_amount)

    def test_refuel_correct_was50_add40_become85_car1_raises(self):
        self.testCar.fuel_amount = 50
        self.assertEqual(50, self.testCar.fuel_amount)
        fuel_amount_before_refueling = self.testCar.fuel_amount
        fuel_for_refile = 40

        fuel_expected = min(fuel_amount_before_refueling + fuel_for_refile, self.testCar.fuel_capacity)
        self.testCar.refuel(fuel_for_refile)

        self.assertEqual(fuel_expected, self.testCar.fuel_amount)

    def test_refuel_correct_was0_add40_become40_car2_raises(self):

        self.assertEqual(0, self.testCar2.fuel_amount)
        fuel_amount_before_refueling = self.testCar2.fuel_amount
        fuel_for_refile = 40

        fuel_expected = min(fuel_amount_before_refueling + fuel_for_refile, self.testCar2.fuel_capacity)
        self.testCar2.refuel(fuel_for_refile)

        self.assertEqual(fuel_expected, self.testCar2.fuel_amount)

        self.assertEqual(40, self.testCar2.fuel_amount)

        fuel_amount_before_refueling = self.testCar2.fuel_amount
        fuel_for_refile = 1

        fuel_expected = min(fuel_amount_before_refueling + fuel_for_refile, self.testCar2.fuel_capacity)
        self.testCar2.refuel(fuel_for_refile)

        self.assertEqual(fuel_expected, self.testCar2.fuel_amount)

    def test_refuel_correct_was50_add40_become66_car2_raises(self):
        self.testCar2.fuel_amount = 50
        self.assertEqual(50, self.testCar2.fuel_amount)
        fuel_amount_before_refueling = self.testCar2.fuel_amount
        fuel_for_refile = 40

        fuel_expected = min(fuel_amount_before_refueling + fuel_for_refile, self.testCar2.fuel_capacity)
        self.testCar2.refuel(fuel_for_refile)

        self.assertEqual(fuel_expected, self.testCar2.fuel_amount)

    def test_drive_above_available_distance_raises(self):

        self.assertEqual(0, self.testCar.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.testCar.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(0, self.testCar.fuel_amount)



        self.testCar.fuel_amount = 7
        self.assertEqual(7, self.testCar.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.testCar.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(7, self.testCar.fuel_amount)

    def test_drive_available_distance_raises(self):
        self.assertEqual(0, self.testCar.fuel_amount)
        self.testCar.drive(0)
        self.assertEqual(0, self.testCar.fuel_amount)

        distance = 100

        self.testCar.fuel_amount = 7.4
        start_level = self.testCar.fuel_amount

        self.assertEqual(7.4, self.testCar.fuel_amount)
        self.testCar.drive(distance)
        self.assertEqual(start_level - self.testCar.fuel_consumption*(distance/100), self.testCar.fuel_amount)


if __name__ == '__main__':
    main()