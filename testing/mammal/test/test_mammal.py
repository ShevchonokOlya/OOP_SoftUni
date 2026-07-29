from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal_example = Mammal(name="Brooklyn", mammal_type='Elephant', sound='Owww')

    def test_init(self):
        self.assertEqual("Brooklyn", self.mammal_example.name)
        self.assertEqual("Elephant", self.mammal_example.type)
        self.assertEqual( "Owww", self.mammal_example.sound)
        self.assertEqual('animals', self.mammal_example._Mammal__kingdom)

        cat_mammal = Mammal( "Tom", 'Cat',  'Meow')
        self.assertEqual("Tom", cat_mammal.name)
        self.assertEqual("Cat", cat_mammal.type)
        self.assertEqual("Meow", cat_mammal.sound)
        self.assertEqual('animals', cat_mammal._Mammal__kingdom)

        #
        # cat_mammal = Mammal(None, None, None)
        # self.assertEqual(None, cat_mammal.name)
        # self.assertEqual(None, cat_mammal.type)
        # self.assertEqual(None, cat_mammal.sound)
        # self.assertEqual('animals', cat_mammal._Mammal__kingdom)
        #
        # cat_mammal = Mammal("", "", "")
        # self.assertEqual("", cat_mammal.name)
        # self.assertEqual("", cat_mammal.type)
        # self.assertEqual("", cat_mammal.sound)
        # self.assertEqual('animals', cat_mammal._Mammal__kingdom)

    def test_making_sound(self):
        self.assertEqual("Brooklyn", self.mammal_example.name)
        self.assertEqual("Owww", self.mammal_example.sound)
        return_sound = self.mammal_example.make_sound()
        self.assertEqual("Brooklyn makes Owww", return_sound)

    def test_getting_kingdom(self):
        self.assertTrue(self.mammal_example._Mammal__kingdom)
        kingdom = self.mammal_example.get_kingdom()
        self.assertEqual("animals", kingdom)

    def test_getting_info(self):
        self.assertEqual("Brooklyn", self.mammal_example.name)
        self.assertEqual("Elephant", self.mammal_example.type)
        info = self.mammal_example.info()
        self.assertEqual("Brooklyn is of type Elephant", info)
        self.assertEqual("Brooklyn", self.mammal_example.name)
        self.assertEqual("Elephant", self.mammal_example.type)

if __name__ == '__main__':
    main()