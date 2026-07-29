from unittest import TestCase, main
from testing.List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(100, 200, 300)

    def test_get_the_biggest_number(self):
        my_list = IntegerList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        big = my_list.get_biggest()
        self.assertEqual(10, big )

    def test_not_integer_initialization_exception(self):

        my_list = IntegerList(1, '2', 3, 9, 4.5)
        self.assertEqual( [1, 3, 9], my_list.get_data() )
        self.assertEqual( [1, 3, 9], my_list._IntegerList__data )

    def test_add_func_wrong_input(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.add('5')
        self.assertEqual( "Element is not Integer",  str(context.exception))

        with self.assertRaises(Exception) as context:
            self.integer_list.add([])
        self.assertEqual("Element is not Integer", str(context.exception))

        with self.assertRaises(Exception) as context:
            self.integer_list.add(2.16)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_add_func_correct_input(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        result =  self.integer_list.add(100)
        self.assertEqual([100, 200, 300, 100], self.integer_list.get_data())
        self.assertEqual([100, 200, 300, 100], result)

    def test_remove_index_wrong_input_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.remove_index(10)
        self.assertEqual( "Index is out of range", str(context.exception))
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        #
        # with self.assertRaises(Exception) as ex:
        #     self.integer_list.remove_index(-1)
        # self.assertEqual( "Index is out of range", str(context.exception))
        # self.assertEqual([100, 200, 300], self.integer_list.get_data())

        # my_list = IntegerList()
        # with self.assertRaises(Exception) as ex:
        #     self.integer_list.remove_index(0)
        # self.assertEqual("Index is out of range", str(context.exception))
        # self.assertEqual([], my_list.get_data())


    def test_remove_index_correct_input_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        result = self.integer_list.remove_index(1)
        self.assertEqual([100, 300], self.integer_list.get_data())
        self.assertEqual(200, result)


    def test_get_wrong_index_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.get(10)
        self.assertEqual( "Index is out of range", str(context.exception))
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        # with self.assertRaises(Exception) as context:
        #     self.integer_list.get(-10)
        # self.assertEqual( "Index is out of range", str(context.exception))
        # self.assertEqual([100, 200, 300], self.integer_list.get_data())

    def test_get_correct_index_input(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        result = self.integer_list.get(1)
        self.assertEqual([100,200,  300], self.integer_list.get_data())
        self.assertEqual(200, result)

    def test_insert_wrong_index_correct_data_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.insert(10, 5)
        self.assertEqual("Index is out of range", str(context.exception))
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        # with self.assertRaises(Exception) as context:
        #     self.integer_list.insert(-10)
        # self.assertEqual( "Index is out of range", str(context.exception))
        # self.assertEqual([100, 200, 300], self.integer_list.get_data())

    def test_insert_correct_index_wrong_data_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.insert(1, "5")
        self.assertEqual("Element is not Integer", str(context.exception))
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

    def test_insert_wrong_index_wrong_data_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        with self.assertRaises(Exception) as context:
            self.integer_list.insert(11, "5")
        self.assertEqual("Index is out of range", str(context.exception))
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

    def test_insert_correct_index_correct_data_raises(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        self.integer_list.insert(1, 5)
        self.assertEqual([100, 5, 200, 300], self.integer_list.get_data())

    #def test_get_the_biggest_from_no_number_exception(self):
        # my_list = IntegerList()
        # with self.assertRaises(Exception) as ex:
        #     my_list.get_biggest()
        # self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_the_biggest_correct_input(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())
        result = self.integer_list.get_biggest()
        self.assertEqual(300, result)
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

        my_list = IntegerList(0, 0 ,0, -10, 0 , 0)
        result = my_list.get_biggest()
        self.assertEqual(0, result)
        self.assertEqual([0, 0 ,0, -10, 0 , 0], my_list.get_data())

    def test_get_the_index_correct_input(self):
        self.assertEqual([100, 200, 300], self.integer_list.get_data())
        result = self.integer_list.get_index(200)
        self.assertEqual(  1 , result)
        self.assertEqual([100, 200, 300], self.integer_list.get_data())

    # def test_get_the_index_INCORRECT_input(self):
    #
    #     self.assertEqual([100, 200, 300], self.integer_list.get_data())
    #     with self.assertRaises(Exception) as context:
    #         self.integer_list.get_index(500)
    #     self.assertEqual("Element is not in IntegerList", str(context.exception))
    #     self.assertEqual([100, 200, 300], self.integer_list.get_data())


if __name__ == '__main__':
    main()