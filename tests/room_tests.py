import unittest

from app.dojo import Dojo
from app.person import Fellow, Staff
from app.room import Room


class TestDojo(unittest.TestCase):
    longStr = "RED\n" + "------------" \
        "------------------\n" \
        "bolaji olajide\n"

    longStr2 = "UNALLOCATED LIST\n" + "---------------" \
        "---------------\nladi adeniran: fellow Living Space\n" \
        "bolaji olajide: fellow Living Space\n"

# clears all data in lists and dictionary
    def clear_all_rooms(self):
        Dojo.rooms_in_dojo = {}
        Dojo.all_office = []
        Dojo.all_living_space = []
        Dojo.persons_in_dojo = {}
        Dojo.unallocated_persons = {}

    def test_create_office(self):
        TestDojo.clear_all_rooms(self)
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.rooms_in_dojo)
        self.assertEqual(initial_room_count, 0)
        my_dojo.create_room('office', ['meeting'])
        self.assertTrue('meeting' in my_dojo.rooms_in_dojo)
        new_room_count = len(my_dojo.rooms_in_dojo)
        self.assertEqual(new_room_count - initial_room_count, 1)
        same_meeting_office = my_dojo.create_room('office', ['meeting'])
        self.assertEqual(same_meeting_office, 'Room already exist.\n')
        double_red_offices = my_dojo.create_room('office', ['red', 'red'])
        self.assertEqual(
            double_red_offices, 'An office called red has been created.\nRoom already exist.\n')
        self.assertTrue('red' in my_dojo.rooms_in_dojo)

    def test_create_ls(self):
        TestDojo.clear_all_rooms(self)
        my_dojo = Dojo()
        initial_room_count = len(my_dojo.rooms_in_dojo)
        self.assertEqual(initial_room_count, 0)
        my_dojo.create_room('living', ['blue'])
        self.assertTrue('blue' in my_dojo.rooms_in_dojo)
        new_room_count = len(my_dojo.rooms_in_dojo)
        self.assertEqual(new_room_count - initial_room_count, 1)
        same_blue_ls = my_dojo.create_room('living', ['blue'])
        self.assertEqual(same_blue_ls, 'Room already exist.\n')
        double_red_ls = my_dojo.create_room('living', ['red', 'red'])
        self.assertEqual(
            double_red_ls, 'A living space called red has been created.\nRoom already exist.\n')
        self.assertTrue('red' in my_dojo.rooms_in_dojo)

    def test_add_staff(self):
        TestDojo.clear_all_rooms(self)
        my_dojo = Dojo()
        my_dojo.create_room('office', ['blue'])
        ladi_office = my_dojo.all_office[0]
        self.assertFalse('ladi adeniran' in my_dojo.persons_in_dojo)
        self.assertFalse('ladi adeniran' in ladi_office.room_persons)
        my_dojo.add_person('ladi', 'adeniran', 'staff')
        self.assertTrue('ladi adeniran' in my_dojo.persons_in_dojo)
        self.assertTrue('ladi adeniran' in ladi_office.room_persons)
        answer = my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        self.assertEqual(
            answer, 'Sorry. Only fellows can have a living space.')
        my_dojo.add_person('oluwadamilola', 'durodola', 'staff')
        my_dojo.add_person('mumeen', 'olasode', 'staff')
        my_dojo.add_person('ichiato', 'ikikin', 'staff')
        my_dojo.add_person('falz', 'thabadguy', 'staff')
        my_dojo.add_person('valentine', 'Mbonu', 'staff')
        answer = my_dojo.add_person('adegboyega', 'koya', 'staff')
        self.assertEqual(answer, 'No office is available.')

    def test_add_fellow(self):
        TestDojo.clear_all_rooms(self)
        my_dojo = Dojo()
        my_dojo.create_room('office', ['red'])
        my_dojo.create_room('living', ['blue'])
        bj_living = my_dojo.all_living_space[0]
        bj_office = my_dojo.all_office[0]
        self.assertFalse('bolaji olajide' in my_dojo.persons_in_dojo)
        self.assertFalse('bolaji olajide' in bj_office.room_persons)
        self.assertFalse('bolaji olajide' in bj_living.room_persons)
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.assertTrue('bolaji olajide' in my_dojo.persons_in_dojo)
        self.assertTrue('bolaji olajide' in bj_living.room_persons)
        self.assertTrue('bolaji olajide' in bj_office.room_persons)

    def test_print_room(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.create_room('living', ['blue'])
        my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        answer = my_dojo.print_room('red')
        self.assertEqual(
            answer, 'There are no occupants in red at the moment.')
        answer = my_dojo.print_room('blue')
        self.assertEqual(
            answer, 'There are no occupants in blue at the moment.')
        my_dojo.add_person('ladi', 'adeniran', 'fellow')
        answer = my_dojo.print_room('red')
        self.assertEqual(answer, 'ladi adeniran --> fellow')
        answer = my_dojo.print_room('blue')
        self.assertEqual(
            answer, 'There are no occupants in blue at the moment.')

    def test_print_allocations(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow')
        content = my_dojo.print_allocations()
        self.assertEqual(content, self.longStr)

    def test_file_print_allocations(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        my_dojo.print_allocations('output')
        my_file = open('data/output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr)

    def test_file_print_unallocations(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        my_dojo.print_unallocated('test_output')
        my_file = open('data/test_output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr2)

    def test_print_unallocated(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        my_dojo.add_person('ladi', 'adeniran', 'fellow', 'y')
        content = my_dojo.print_unallocated()
        self.assertEqual(content, self.longStr2)
