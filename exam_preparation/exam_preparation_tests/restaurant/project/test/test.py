import unittest

from restaurant.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.test_restaurant = Restaurant("Delicious", 50)

    def test_restaurant_initialization(self):
        self.assertEqual("Delicious" ,self.test_restaurant.name)
        self.assertEqual("50" , self.test_restaurant.capacity)
        self.assertEqual(0, len(self.test_restaurant.waiters))
        self.assertTrue(isinstance(self.test_restaurant, Restaurant))
        self.assertTrue(isinstance(self.test_restaurant.waiters, list))

if __name__ == '__main__':
    unittest.main()
