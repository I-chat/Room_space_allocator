import unittest
from app.dojo import Dojo

class TestDojo(unittest.TestCase):
    def setUp(self):
        self.my_dojo = Dojo()

    def clear_all_rooms():
        Dojo.all_rooms = {}

    def test_create_office(self):
        TestDojo.clear_all_rooms()
        initial_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(initial_room_count, 0)
        blue_office = self.my_dojo.create_room('office', ['blue'])
        self.assertTrue('blue' in self.my_dojo.all_rooms)
        new_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        another_blue_office = self.my_dojo.create_room('office', ['blue'])
        self.assertEqual(another_blue_office, 'Room already exist')
        double_red_offices = self.my_dojo.create_room('office', ['red', 'red'])
        self.assertEqual(double_red_offices, 'Room already exist')
        self.assertTrue('red' in self.my_dojo.all_rooms)

    def test_create_ls(self):
        initial_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(initial_room_count, 0)
        blue_office = self.my_dojo.create_room('living', ['blue'])
        self.assertTrue('blue' in self.my_dojo.all_rooms)
        new_room_count = len(self.my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        another_blue_office = self.my_dojo.create_room('living', ['blue'])
        self.assertEqual(another_blue_office, 'Room already exist')
        double_red_offices = self.my_dojo.create_room('office', ['red', 'red'])
        self.assertEqual(double_red_offices, 'Room already exist')
        self.assertTrue('red' in self.my_dojo.all_rooms)

    def test_add_fellow(self):
        pass