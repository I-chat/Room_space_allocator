import unittest
from app.dojo import Dojo
from app.room import Room
from app.person import Staff, Fellow

class TestDojo(unittest.TestCase):

    def clear_all_rooms(self):
        Dojo.all_rooms = {}
        Dojo.all_office = []
        Dojo.all_ls = []
        Dojo.dojo_all_persons = {}

    def test_create_office(self):
        TestDojo.clear_all_rooms(self)
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
        TestDojo.clear_all_rooms(self)
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
        TestDojo.clear_all_rooms(self)
        my_dojo = Dojo()
        my_dojo.create_room('office', ['blue'])
        ladi_office = my_dojo.all_office[0]
        self.assertFalse('ladi adeniran' in my_dojo.dojo_all_persons)
        self.assertFalse('ladi adeniran' in ladi_office.room_all_persons)
        my_dojo.add_person('ladi', 'adeniran', 'staff')
        self.assertTrue('ladi adeniran' in my_dojo.dojo_all_persons)
        self.assertTrue('ladi adeniran' in ladi_office.room_all_persons)
        answer = my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        self.assertEqual(answer, 'Sorry. Only fellows can have a living space.')
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
        bj_living = my_dojo.all_ls[0]
        bj_office = my_dojo.all_office[0]
        self.assertFalse('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertFalse('bolaji olajide' in bj_office.room_all_persons)
        self.assertFalse('bolaji olajide' in bj_living.room_all_persons)
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        self.assertTrue('bolaji olajide' in my_dojo.dojo_all_persons)
        self.assertTrue('bolaji olajide' in bj_living.room_all_persons)
        self.assertTrue('bolaji olajide' in bj_office.room_all_persons)

    def test_print_room(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.create_room('living', ['blue'])
        my_dojo.add_person('bolaji', 'olajide', 'staff', 'y')
        answer = my_dojo.print_room('red')
        self.assertEqual(answer, 'There are no occupants in red at the moment.')
        answer = my_dojo.print_room('blue')
        self.assertEqual(answer, 'There are no occupants in blue at the moment.')
        my_dojo.add_person('ladi', 'adeniran', 'fellow')
        answer = my_dojo.print_room('red')
        self.assertEqual(answer, 'ladi adeniran --> fellow')
        answer = my_dojo.print_room('blue')
        self.assertEqual(answer, 'There are no occupants in blue at the moment.')

    def test_file_print_allocations(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow', 'y')
        longStr = "RED\n" + "---------------" \
                "----------------" \
                "-------------------\n" \
                "bolaji olajide\n"
        my_dojo.print_allocations('output')
        my_file = open('data/output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, longStr)

    def test_print_allocations(self):
        my_dojo = Dojo()
        TestDojo.clear_all_rooms(self)
        my_dojo.create_room('office', ['red'])
        my_dojo.add_person('bolaji', 'olajide', 'fellow')
        longStr = "RED\n" + "-----------------" \
                "-----------------------\n" \
                "bolaji olajide\n"
        content = my_dojo.print_allocations()
        self.assertEqual(content, longStr)