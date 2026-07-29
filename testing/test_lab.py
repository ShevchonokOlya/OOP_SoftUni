
from multiprocessing.pool import worker


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class WorkerTest(TestCase):

    def test_initialize(self):
        worker = Worker('Test', 10000, 100)
        self.assertEqual('Test', worker.name)
        self.assertEqual(10000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_incremented_after_the_rest(self):
        worker = Worker('Test', 10000, 100)
        worker.rest()
        self.assertEqual(101, worker.energy)
        self.assertEqual(0, worker.money)
        worker.rest()
        self.assertEqual(102, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_tries_to_work_with_negative_energy(self):
        worker = Worker('Test', 10000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_tries_to_work_with_zero_energy(self):
        worker = Worker('Test', 10000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_salary_increased_after_the_work(self):
        worker = Worker('Test', 10000, 100)
        worker.work()
        self.assertEqual(10000, worker.money)
        worker.work()
        self.assertEqual(20000, worker.money)

    def test_energy_decreased_after_the_work(self):
        worker = Worker('Test', 10000, 100)
        worker.work()
        self.assertEqual(99, worker.energy)
        worker.work()
        self.assertEqual(98, worker.energy)

    def test_get_info_returns_proper_string(self):
        worker = Worker('Test', 10000, 100)
        result = worker.get_info()
        self.assertEqual(result, 'Test has saved 0 money.' )
        worker.work()
        result2 = worker.get_info()
        self.assertEqual(result2, 'Test has saved 10000 money.' )


if __name__ == '__main__':
    main()


from unittest import TestCase, main
class CatTest(TestCase):

    def test_initialize(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(False, my_cat.fed)
        self.assertEqual(False, my_cat.sleepy)
        self.assertEqual(0, my_cat.size)

    def test_size_is_incremented_after_eating(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)

        self.assertEqual(0, my_cat.size)
        my_cat.eat()
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(1, my_cat.size)


    def test_Cat_is_fed_after_eating(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(False, my_cat.fed)

        my_cat.eat()
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(True, my_cat.fed)

    def test_Cat_is_already_fed_exception_after_eating(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(False, my_cat.fed)

        my_cat.eat()
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(True, my_cat.fed)

        with self.assertRaises(Exception) as ex:
            my_cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))
        self.assertEqual(True, my_cat.fed)

    def test_cat_cannot_sleep_starving_exception(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(False, my_cat.fed)
        self.assertEqual(False, my_cat.sleepy)
        with self.assertRaises(Exception) as ex:
            my_cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertEqual(False, my_cat.sleepy)
        self.assertEqual(False, my_cat.fed)

    def test_cat_cannot_sleep_after_sleeping_exception(self):
        my_cat = Cat('Kitten')
        self.assertEqual('Kitten', my_cat.name)
        self.assertEqual(False, my_cat.fed)
        self.assertEqual(False, my_cat.sleepy)
        my_cat.eat()


        self.assertTrue(my_cat.sleepy)
        my_cat.sleep()


        self.assertFalse(my_cat.sleepy)




if __name__ == '__main__':
    main()