from project.hotel import Hotel
from project.room import Room
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 3)
        self.hotel = Hotel("Some Hotel")

    def test_free_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.hotel.free_room(1)
        self.assertEqual(self.hotel.guests, 0)
        self.assertEqual(self.hotel.rooms[0].is_taken, False)
        self.assertEqual(self.hotel.rooms[0].guests, 0)



if __name__ == "__main__":
    unittest.main()