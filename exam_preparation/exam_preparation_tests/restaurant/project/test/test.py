import unittest

from project.restaurant import Restaurant


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        self.test_restaurant = Restaurant("Delicious", 50)

    def test_restaurant_initialization(self):
        self.assertEqual("Delicious" ,self.test_restaurant.name)
        self.assertEqual(50 , self.test_restaurant.capacity)
        self.assertEqual(0, len(self.test_restaurant.waiters))
        self.assertTrue(isinstance(self.test_restaurant, Restaurant))
        self.assertTrue(isinstance(self.test_restaurant.waiters, list))

    def test_name_validation_empty_string(self):
        with self.assertRaises(ValueError) as e:
            self.test_restaurant.name = ""  # Проверяем сеттер напрямую
        self.assertEqual("Invalid name!", str(e.exception))

    def test_name_correct_initialization(self):
        self.assertEqual("Delicious", self.test_restaurant.name)
        test_1 = Restaurant("         1       ", 50)
        self.assertEqual("         1       ",  test_1.name)

    def test_name_incorrect_initialization_value_error(self):
        with self.assertRaises(ValueError) as exception_context:
            rest1 = Restaurant("      ", 100)
        self.assertEqual("Invalid name!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context:
            rest2 = Restaurant("", 100)
        self.assertEqual("Invalid name!", str(exception_context.exception))

        # with self.assertRaises(ValueError) as exception_context:
        #     rest3 = Restaurant(1, 100)
        # self.assertEqual("Invalid name!", str(exception_context.exception))

        with self.assertRaises(ValueError) as exception_context:
            rest3 = Restaurant(None, 100)
        self.assertEqual("Invalid name!", str(exception_context.exception))

    def test_capacity_correct_initialization_value_error(self):
        rest1 = Restaurant("Restaurant", 0)
        self.assertEqual("Restaurant", rest1.name)
        self.assertEqual(0, rest1.capacity)
        self.assertEqual(0, len(rest1.waiters))


        self.assertEqual("Delicious",  self.test_restaurant.name)
        self.assertEqual(50,  self.test_restaurant.capacity)
        self.assertEqual(0, len( self.test_restaurant.waiters))



    def test_capacity_incorrect_initialization_value_error(self):
        with self.assertRaises(ValueError) as exception_context:
            rest1 = Restaurant("Restaurant", -1)
        self.assertEqual("Invalid capacity!", str(exception_context.exception))

    def test_getting_waiters(self):
        self.test_restaurant.add_waiter("Waiter0")
        self.test_restaurant.add_waiter("Waiter1")
        self.test_restaurant.add_waiter("Waiter2")

        waiters = self.test_restaurant.waiters

        result = self.test_restaurant.get_waiters(None, None)
        self.assertEqual(3, len(waiters))
        self.assertEqual(result, waiters)

        self.test_restaurant.add_waiter("Waiter3")
        self.test_restaurant.add_waiter("Waiter4")
        self.test_restaurant.add_waiter("Waiter5")
        self.test_restaurant.add_waiter("Waiter6")
        self.test_restaurant.add_waiter("Waiter7")

        self.test_restaurant.waiters[0]['total_earnings'] = 1000
        self.test_restaurant.waiters[1]['total_earnings'] = 2000
        self.test_restaurant.waiters[2]['total_earnings'] = 2500

        self.test_restaurant.waiters[3]['total_earnings'] = 3000
        self.test_restaurant.waiters[4]['total_earnings'] = 3500
        self.test_restaurant.waiters[5]['total_earnings'] = 4000

        self.test_restaurant.waiters[6]['total_earnings'] = 4500
        self.test_restaurant.waiters[7]['total_earnings'] = 5000

        result2 = self.test_restaurant.get_waiters(3000, 4000)
        self.assertEqual(8, len(waiters))
        self.assertEqual(3, len(result2))
        self.assertEqual([self.test_restaurant.waiters[3],self.test_restaurant.waiters[4],self.test_restaurant.waiters[5]], result2)

        result3 = self.test_restaurant.get_waiters(300, 2800)
        self.assertEqual(8, len(waiters))
        self.assertEqual(3, len(result3))
        self.assertEqual([self.test_restaurant.waiters[0],
                          self.test_restaurant.waiters[1],
                          self.test_restaurant.waiters[2]],
                        result3)

        result4 = self.test_restaurant.get_waiters(30000, 200)
        self.assertEqual(8, len(waiters))
        self.assertEqual(0, len(result4))
        self.assertEqual([], result4)

        self.test_restaurant.add_waiter("Waiter8")
        self.test_restaurant.add_waiter("Waiter9")
        self.test_restaurant.add_waiter("Waiter10")
        self.test_restaurant.add_waiter("Waiter11")
        self.test_restaurant.add_waiter("Waiter12")

        result5 = self.test_restaurant.get_waiters(None, 2000)
        self.assertEqual(13, len(waiters))
        self.assertEqual(7, len(result5))
        self.assertEqual([self.test_restaurant.waiters[0],
                          self.test_restaurant.waiters[1],
                          self.test_restaurant.waiters[8],
                          self.test_restaurant.waiters[9],
                          self.test_restaurant.waiters[10],
                          self.test_restaurant.waiters[11],
                          self.test_restaurant.waiters[12]],
                         result5)

        result6 = self.test_restaurant.get_waiters(7000, None)
        self.assertEqual(13, len(waiters))
        self.assertEqual(0, len(result6))
        self.assertEqual([],result6)

        result7 = self.test_restaurant.get_waiters(5000, None)
        self.assertEqual(13, len(waiters))
        self.assertEqual(1, len(result7))
        self.assertEqual([self.test_restaurant.waiters[7]], result7)

        result8 = self.test_restaurant.get_waiters(5000)
        self.assertEqual(13, len(waiters))
        self.assertEqual(1, len(result8))
        self.assertEqual([self.test_restaurant.waiters[7]], result8)

    def test_get_waiters_with_min_and_max_earnings(self):

        self.test_restaurant.waiters = [
            {"name": "John", "total_earnings": 100},
            {"name": "Jane", "total_earnings": 150},
            {"name": "Joe", "total_earnings": 200}
        ]

        # Теперь тестируем ТОЛЬКО логику фильтрации
        result = self.test_restaurant.get_waiters(min_earnings=120, max_earnings=180)
        self.assertEqual([{"name": "Jane", "total_earnings": 150}], result)


    def test_add_waiter_correct_adding(self):
        test_restaurant = Restaurant("test_restaurant" , 2)
        self.assertEqual(0, (len(test_restaurant.waiters)))

        result1 = test_restaurant.add_waiter("Waiter1")
        self.assertEqual(f"The waiter Waiter1 has been added.", result1)
        self.assertEqual( 1 , (len(test_restaurant.waiters)))
        self.assertEqual("Waiter1",   test_restaurant.waiters[0]['name'])

        result2 = test_restaurant.add_waiter("Waiter2")
        self.assertEqual(f"The waiter Waiter2 has been added.", result2)
        self.assertEqual(2, (len(test_restaurant.waiters)))
        self.assertEqual("Waiter2", test_restaurant.waiters[1]['name'])

    def test_add_waiter_same_name_adding(self):
        test_restaurant = Restaurant("test_restaurant", 2)
        self.assertEqual(0, (len(test_restaurant.waiters)))

        result1 = test_restaurant.add_waiter("Waiter1")
        self.assertEqual(f"The waiter Waiter1 has been added.", result1)
        self.assertEqual(1, (len(test_restaurant.waiters)))
        self.assertEqual("Waiter1", test_restaurant.waiters[0]['name'])

        result2 = test_restaurant.add_waiter("Waiter1")
        self.assertEqual("The waiter Waiter1 already exists!", result2)
        self.assertEqual(1, (len(test_restaurant.waiters)))

    def test_add_waiter_out_of_capacity(self):
        test_restaurant0 = Restaurant("test_restaurant", 0)
        self.assertEqual(0, (len(test_restaurant0.waiters)))

        result0 = test_restaurant0.add_waiter("Waiter2")
        self.assertEqual("No more places!", result0)
        self.assertEqual(0, (len(test_restaurant0.waiters)))

        test_restaurant = Restaurant("test_restaurant", 1)
        self.assertEqual(0, (len(test_restaurant.waiters)))

        result1 = test_restaurant.add_waiter("Waiter1")
        self.assertEqual(f"The waiter Waiter1 has been added.", result1)
        self.assertEqual(1, (len(test_restaurant.waiters)))
        self.assertEqual("Waiter1", test_restaurant.waiters[0]['name'])

        result2 = test_restaurant.add_waiter("Waiter2")
        self.assertEqual("No more places!", result2)
        self.assertEqual(1, (len(test_restaurant.waiters)))

    def test_correct_remove_waiter(self):
        self.test_restaurant.add_waiter("Waiter0")
        self.test_restaurant.add_waiter("Waiter1")
        self.test_restaurant.add_waiter("Waiter2")

        waiters = self.test_restaurant.waiters
        self.assertEqual(3, len(waiters))

        result  = self.test_restaurant.remove_waiter("Waiter0")
        self.assertEqual(2, len(waiters))
        self.assertEqual("The waiter Waiter0 has been removed.", result)

        result2 = self.test_restaurant.remove_waiter("Waiter1")
        self.assertEqual(1, len(waiters))
        self.assertEqual("The waiter Waiter1 has been removed.", result2)

    def test_trying_to_remove_waiter_with_no_such_name_in_list(self):

        self.assertEqual(0, len(self.test_restaurant.waiters))
        result = self.test_restaurant.remove_waiter("Waiter0")
        self.assertEqual(0, len(self.test_restaurant.waiters))

        self.assertEqual("No waiter found with the name Waiter0.", result)

        self.test_restaurant.add_waiter("Waiter0")
        self.test_restaurant.add_waiter("Waiter1")
        self.test_restaurant.add_waiter("Waiter2")

        self.assertEqual(3, len(self.test_restaurant.waiters))
        result2 = self.test_restaurant.remove_waiter("Waiter4")
        self.assertEqual(3, len(self.test_restaurant.waiters))

        self.assertEqual("No waiter found with the name Waiter4.", result2)

    def test_getting_total_earnings(self):
        self.assertEqual(0, len(self.test_restaurant.waiters))
        self.assertEqual(0, self.test_restaurant.get_total_earnings())

        self.test_restaurant.add_waiter("Waiter0")
        self.test_restaurant.add_waiter("Waiter1")
        self.test_restaurant.add_waiter("Waiter2")
        self.test_restaurant.add_waiter("Waiter3")
        self.test_restaurant.add_waiter("Waiter4")
        self.test_restaurant.add_waiter("Waiter5")
        self.test_restaurant.add_waiter("Waiter6")
        self.test_restaurant.add_waiter("Waiter7")

        self.test_restaurant.waiters[0]['total_earnings'] = 1000
        self.test_restaurant.waiters[1]['total_earnings'] = 1000
        self.test_restaurant.waiters[2]['total_earnings'] = 1000
        self.test_restaurant.waiters[6]['total_earnings'] = 1000
        self.test_restaurant.waiters[7]['total_earnings'] = 1000

        self.assertEqual(8, len(self.test_restaurant.waiters))
        self.assertEqual(5000, self.test_restaurant.get_total_earnings())

        test_rest = Restaurant("test_rest", 5)
        test_rest.waiters = [
            {"name": "John", "total_earnings": 100},
            {"name": "Jane", "total_earnings": 100},
            {"name": "Ivan"},
            {"name": "Bobby"},
            {"name": "Joe", "total_earnings": 100}
        ]
        self.assertEqual(5, len(test_rest.waiters))
        self.assertEqual(300, test_rest.get_total_earnings())

if __name__ == '__main__':
    unittest.main()
