import unittest
from app.dojo import Dojo
from app.room import Room
from app.person import Staff, Fellow

class TestDojo(unittest.TestCase):

    def clear_all_rooms(self):
        Dojo.all_rooms = {}
        Dojo.all_office = []
        Dojo.all_ls = []

    def test_create_office(self):
        self.clear_all_rooms()
        my_dojo = Dojo()
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
        self.clear_all_rooms()
        my_dojo = Dojo()
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
        self.clear_all_rooms()
        my_dojo = Dojo()
        my_dojo.create_room('office', ['blue'])
        ladi_office = my_dojo.all_office[0]
        self.assertFalse('ladi adeniran' in my_dojo.dojo_all_persons)
        self.assertFalse('ladi adeniran' in ladi_office.room_all_persons)
        my_dojo.add_person('ladi', 'adeniran', 'staff')
        self.assertTrue('ladi adeniran' in my_dojo.dojo_all_persons)
        self.assertTrue('ladi adeniran' in ladi_office.room_all_persons)

    def test_add_fellow(self):
        self.clear_all_rooms()
        my_dojo = Dojo()
        my_dojo.create_room('office', ['red'])
        my_dojo.create_room('living', ['blue'])
        bj_living = my_dojo.all_ls[0]
        bj_office = my_dojo.all_office[0]
        self.assertFalse('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertFalse('bolaji olajide' in bj_office.room_all_persons)
        self.assertFalse('bolaji olajide' in bj_living.room_all_persons)
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.assertTrue('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertTrue('bolaji olajide' in bj_living.room_all_persons)
        self.assertTrue('bolaji olajide' in bj_office.room_all_persons)