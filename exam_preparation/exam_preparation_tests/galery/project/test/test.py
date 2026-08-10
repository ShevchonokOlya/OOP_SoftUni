from project.gallery import Gallery
import unittest

class TestGallery(unittest.TestCase):
    def setUp(self):
        self.gallery = Gallery("Gallery", "NY", 100.00, True)

    def test_gallery_initialization(self):
        self.assertIsInstance(self.gallery, Gallery)
        self.assertEqual("Gallery", self.gallery.gallery_name)
        self.assertEqual("NY", self.gallery.city)
        self.assertEqual(100.00, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(0, len(self.gallery.exhibitions))



    def test_setting_gallery_name_raises_exception(self):
        with self.assertRaises(ValueError) as er:
            Gallery("        ", "NY", 100.00, True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(er.exception))

        with self.assertRaises(ValueError) as er:
             Gallery("   Test Gallery  ", "NY", 100.00, True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(er.exception))

        with self.assertRaises(ValueError) as er:
             Gallery("Test Gallery", "NY", 100.00, True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            Gallery("@", "NY", 100.00, True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            Gallery('', city = "NY", area_sq_m = 100.00, open_to_public = True)
        self.assertEqual("Gallery name can contain letters and digits only!", str(er.exception))

    def test_setting_correct_gallery_name(self):
        self.gallery.gallery_name = "   Test  "
        self.assertEqual("Test", self.gallery.gallery_name)

        self.gallery.gallery_name = "Test123"
        self.assertEqual("Test123", self.gallery.gallery_name)

        self.gallery.gallery_name = "123"
        self.assertEqual("123", self.gallery.gallery_name)

    def test_setting_city_raises_exception(self):
        with self.assertRaises(ValueError) as er:
            self.gallery.city = " New York"
        self.assertEqual("City name must start with a letter!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.gallery.city = "1New York"
        self.assertEqual("City name must start with a letter!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.gallery.city = ""
        self.assertEqual("City name must start with a letter!", str(er.exception))

    def test_setting_correct_city(self):
        self.gallery.city = "New York"
        self.assertEqual("New York", self.gallery.city)

        self.gallery.city = "N"
        self.assertEqual("N", self.gallery.city)

    def test_setting_area_raises_exception(self):
        with self.assertRaises(ValueError) as er:
            self.gallery.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.gallery.area_sq_m = -1
        self.assertEqual("Gallery area must be a positive number!", str(er.exception))


    def test_setting_correct_area(self):
        self.gallery.area_sq_m = 0.1
        self.assertEqual(0.1, self.gallery.area_sq_m)

        self.gallery.area_sq_m = 100
        self.assertEqual(100, self.gallery.area_sq_m)

    def test_add_exhibition_name_is_already_exists_name(self):
        self.gallery.exhibitions["exhibition1"] = 2002
        res = self.gallery.add_exhibition("exhibition1", 2004)
        self.assertEqual('Exhibition "exhibition1" already exists.', res)

    def test_add_exhibition_with_correct_name(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        res = self.gallery.add_exhibition("exhibition1", 2002)
        self.assertEqual('Exhibition "exhibition1" added for the year 2002.', res)

        self.assertEqual(1, len(self.gallery.exhibitions))

        res = self.gallery.add_exhibition("exhibition2", 2002)
        self.assertEqual('Exhibition "exhibition2" added for the year 2002.', res)

        self.assertEqual(2, len(self.gallery.exhibitions))

    def test_remove_exhibition_which_NOT_existing_name(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        res = self.gallery.remove_exhibition("exhibition1")
        self.assertEqual('Exhibition "exhibition1" not found.', res)
        self.assertEqual(0, len(self.gallery.exhibitions))

        self.gallery.exhibitions["exhibition1"] = 2002
        self.assertEqual(1, len(self.gallery.exhibitions))

        res2 = self.gallery.remove_exhibition("exhibition2")
        self.assertEqual('Exhibition "exhibition2" not found.', res2)
        self.assertEqual(1, len(self.gallery.exhibitions))


    def test_remove_exhibition_with_correct_name(self):
        self.assertEqual(0, len(self.gallery.exhibitions))
        self.gallery.exhibitions["exhibition1"] = 2002
        self.assertEqual(1, len(self.gallery.exhibitions))
        self.gallery.exhibitions["exhibition2"] = 2004
        self.assertEqual(2, len(self.gallery.exhibitions))
        self.gallery.exhibitions["exhibition3"] = 2004
        self.assertEqual(3, len(self.gallery.exhibitions))

        res = self.gallery.remove_exhibition("exhibition2")

        self.assertEqual('Exhibition "exhibition2" removed.', res)
        self.assertEqual(["exhibition1", "exhibition3"] ,  list(self.gallery.exhibitions.keys()))

        res = self.gallery.remove_exhibition("exhibition1")
        self.assertEqual('Exhibition "exhibition1" removed.', res)
        self.assertEqual(1, len(self.gallery.exhibitions))
        self.assertEqual(["exhibition3"], list(self.gallery.exhibitions.keys()))

    def test_listing_exhibitions_if_open_to_public(self):
        self.assertEqual("",  self.gallery.list_exhibitions())
        self.gallery.exhibitions["exhibition1"] = 2002
        self.assertEqual("exhibition1: 2002", self.gallery.list_exhibitions())
        self.gallery.exhibitions["exhibition2"] = 2004
        self.gallery.exhibitions["exhibition3"] = 2003

        self.assertEqual("exhibition1: 2002\nexhibition2: 2004\nexhibition3: 2003", self.gallery.list_exhibitions())

    def test_listing_exhibitions_if_closed_to_public(self):
        self.gallery.open_to_public = False
        self.assertEqual("Gallery Gallery is currently closed for public! Check for updates later on.",  self.gallery.list_exhibitions())
        self.gallery.exhibitions["exhibition1"] = 2002
        self.assertEqual("Gallery Gallery is currently closed for public! Check for updates later on.", self.gallery.list_exhibitions())
        self.gallery.exhibitions["exhibition2"] = 2004
        self.gallery.exhibitions["exhibition3"] = 2003

        self.assertEqual("Gallery Gallery is currently closed for public! Check for updates later on.", self.gallery.list_exhibitions())


if __name__ == '__main__':
    unittest.main()


