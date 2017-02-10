import unittest
from app.dojo import Dojo
from app.room import Room
from app.person import Staff, Fellow

class TestDojo(unittest.TestCase):

    def clear_all_rooms():
        Dojo.all_rooms = {}

    def test_create_office(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms()
        initial_room_count = len(my_dojo.all_rooms)
        self.assertEqual(initial_room_count, 0)
        meeting_office = my_dojo.create_room('office', ['meeting'])
        self.assertTrue('meeting' in my_dojo.all_rooms)
        new_room_count = len(my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        same_meeting_office = my_dojo.create_room('office', ['meeting'])
        self.assertEqual(same_meeting_office, 'Room already exist')
        double_red_offices = my_dojo.create_room('office', ['red', 'red'])
        self.assertEqual(double_red_offices, 'Room already exist')
        self.assertTrue('red' in my_dojo.all_rooms)

    def test_create_ls(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms()
        initial_room_count = len(my_dojo.all_rooms)
        self.assertEqual(initial_room_count, 0)
        blue_ls = my_dojo.create_room('living', ['blue'])
        self.assertTrue('blue' in my_dojo.all_rooms)
        new_room_count = len(my_dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
        same_blue_ls = my_dojo.create_room('living', ['blue'])
        self.assertEqual(same_blue_ls, 'Room already exist')
        double_red_ls = my_dojo.create_room('living', ['red', 'red'])
        self.assertEqual(double_red_ls, 'Room already exist')
        self.assertTrue('red' in my_dojo.all_rooms)

    def test_add_staff(self):
        my_dojo = Dojo()
        ladi_office = my_dojo.create_room('office', ['blue'])
        self.assertFalse('ladi adeniran' in my_dojo.dojo_all_persons)
        my_dojo.add_person('ladi', 'adeniran', 'staff')
        self.assertTrue('ladi adeniran' in my_dojo.dojo_all_persons)
        self.assertTrue('ladi adeniran' in Room.room_all_persons)

    def test_add_fellow(self):
        my_dojo = Dojo()
        bj_office = my_dojo.create_room('office', ['red'])
        bj_living = my_dojo.create_room('living', ['blue'])
        self.assertFalse('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertFalse('bolaji olajide' in Room.room_all_persons)
        my_dojo.add_person('bolaji', 'olajide', 'fellow')
        self.assertTrue('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertTrue('bolaji olajide' in Room.room_all_persons)