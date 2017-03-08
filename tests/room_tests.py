"""This module is imported to the test script to test the functionalities."""


import unittest
import os

from app.dojo import Dojo
from database.database import (DbConnector, PersonData, LivingSpaceData)


class TestDojo(unittest.TestCase):
    """Test all functionalities of Dojo class."""

    longStr = "RED\n" + "------------" \
        "------------------\n" \
        "bolaji olajide\n"

    longStr2 = "UNALLOCATED LIST\n" + "---------------" \
        "---------------\nbolaji olajide: Living Space\n" \
        "ladi adeniran: Living Space\n"

    longStr3 = "OLUWAFEMI SULE fellow y\nDOMINIC WALTERS staff\nSIMON" \
        " PATTERSON fellow y\nMARI LAWRENCE fellow y\nLEIGH RILEY staff\n" \
        "TANA LOPEZ fellow y\nKELLY McGUIRE staff"

    def tearDown(self):
        """Empty all data structures in Dojo after each test case."""
        Dojo.all_office = []
        Dojo.all_living_space = []
        Dojo.all_persons_in_dojo = {}
        Dojo.unallocated_persons = {}

    def test_create_office(self):
        """Test the creation of offices functionality in Dojo."""
        initial_room_count = len(Dojo.all_office)
        self.assertEqual(initial_room_count, 0)
        Dojo.create_room('office', ['meeting'])
        second_room_count = len(Dojo.all_office)
        self.assertEqual(second_room_count, 1)
        same_meeting_office = Dojo.create_room('office', ['meeting'])
        third_room_count = len(Dojo.all_office)
        self.assertEqual(same_meeting_office, 'Room already exist.\n')
        self.assertEqual(third_room_count, 1)
        double_red_offices = Dojo.create_room('office', ['red', 'red'])
        fourth_room_count = len(Dojo.all_office)
        self.assertEqual(double_red_offices,
                         'An office called red has been created.'
                         '\nRoom already exist.\n')
        self.assertEqual(fourth_room_count, 2)

    def test_create_ls(self):
        """Test the creation of living space functionality in Dojo."""
        initial_room_count = len(Dojo.all_living_space)
        self.assertEqual(initial_room_count, 0)
        Dojo.create_room('living', ['blue'])
        second_room_count = len(Dojo.all_living_space)
        self.assertEqual(second_room_count, 1)
        same_blue_ls = Dojo.create_room('living', ['blue'])
        third_room_count = len(Dojo.all_living_space)
        self.assertEqual(same_blue_ls, 'Room already exist.\n')
        self.assertEqual(third_room_count, 1)
        double_red_ls = Dojo.create_room('living', ['red', 'red'])
        fourth_room_count = len(Dojo.all_living_space)
        self.assertEqual(double_red_ls,
                         'A living space called red has been created.'
                         '\nRoom already exist.\n')
        self.assertEqual(fourth_room_count, 2)

    def test_add_staff(self):
        """Test the allocation of staff to offices only."""
        Dojo.create_room('office', ['blue'])
        Dojo.create_room('living', ['red'])
        office_one = Dojo.all_office[0]
        living_one = Dojo.all_living_space[0]
        initial_person_count = len(office_one.room_members)
        self.assertEqual(initial_person_count, 0)
        Dojo.add_person_input_check('ladi', 'adeniran', 'staff')
        second_person_count = len(office_one.room_members)
        self.assertEqual(second_person_count, 1)
        Dojo.add_person_input_check('bolaji', 'olajide', 'staff', 'y')
        third_person_count = len(office_one.room_members)
        persons_in_living_count = len(living_one.room_members)
        self.assertEqual(third_person_count, 2)
        self.assertEqual(persons_in_living_count, 0)

    def test_add_more_than_six_person_in_office(self):
        """Test that not more than 6 persons can be assigned an office."""
        Dojo.create_room('office', ['blue'])
        office_one = Dojo.all_office[0]
        initial_person_count = len(office_one.room_members)
        self.assertEqual(initial_person_count, 0)
        Dojo.add_person_input_check('ladi', 'adeniran', 'staff')
        second_person_count = len(office_one.room_members)
        self.assertEqual(second_person_count, 1)
        Dojo.add_person_input_check('bolaji', 'olajide', 'staff', 'y')
        Dojo.add_person_input_check(
            'oluwadamilola', 'durodola', 'staff')
        Dojo.add_person_input_check('mumeen', 'olasode', 'staff')
        Dojo.add_person_input_check('ichiato', 'ikikin', 'staff')
        Dojo.add_person_input_check('falz', 'thabadguy', 'staff')
        Dojo.add_person_input_check('valentine', 'mbonu', 'staff')
        third_person_count = len(office_one.room_members)
        self.assertNotEqual(third_person_count, 7)
        self.assertEqual(third_person_count, 6)

    def test_add_fellow(self):
        """Test the allocation of fellows to a living space."""
        Dojo.create_room('living', ['blue'])
        living_one = Dojo.all_living_space[0]
        initial_person_count = len(living_one.room_members)
        self.assertEqual(initial_person_count, 0)
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        second_person_count = len(living_one.room_members)
        self.assertEqual(second_person_count, 1)
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        third_person_count = len(living_one.room_members)
        self.assertEqual(third_person_count, 2)

    def test_test_add_more_than_four_person_in_living(self):
        """Test that not more than 4 persons can be assigned a living space."""
        Dojo.create_room('living', ['blue'])
        living_one = Dojo.all_living_space[0]
        Dojo.add_person_input_check(
            'oluwadamilola', 'durodola', 'fellow', 'y')
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        Dojo.add_person_input_check('mumeen', 'olasode', 'fellow', 'y')
        Dojo.add_person_input_check('ichiato', 'ikikin', 'fellow', 'y')
        initial_person_count = len(living_one.room_members)
        self.assertEqual(initial_person_count, 4)
        Dojo.add_person_input_check('falz', 'thabadguy', 'fellow', 'y')
        second_person_count = len(living_one.room_members)
        self.assertEqual(second_person_count, 4)

    def test_print_room(self):
        """Test the printing of the occupants in a given room if any."""
        Dojo.create_room('office', ['red'])
        Dojo.create_room('living', ['blue'])
        Dojo.add_person_input_check('bolaji', 'olajide', 'staff', 'y')
        answer = Dojo.print_room('red')
        self.assertEqual(
            answer, 'bolaji olajide --> staff\n')
        answer = Dojo.print_room('blue')
        self.assertEqual(
            answer, 'There are no occupants in blue at the moment.')
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        output = Dojo.print_room('red')
        self.assertEqual(output, 'bolaji olajide --> staff\n'
                         'ladi adeniran --> fellow\n')
        answer = Dojo.print_room('blue')
        self.assertEqual(
            answer, 'ladi adeniran --> fellow\n')

    def test_print_allocations(self):
        """Test the printing of all persons who were allocated a room."""
        Dojo.create_room('office', ['red'])
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow')
        content = Dojo.print_allocations()
        self.assertEqual(content, self.longStr)

    def test_file_print_allocations(self):
        """Test the writing to file of persons who were allocated a room."""
        Dojo.create_room('office', ['red'])
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        Dojo.print_allocations('output')
        my_file = open('data/output.txt', 'r')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr)

    def test_file_print_unallocated(self):
        """Test the writing to file of persons who are yet to get a room."""
        Dojo.create_room('office', ['red'])
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        Dojo.print_unallocated('test_output')
        my_file = open('data/test_output.txt')
        content = my_file.read()
        my_file.close()
        self.assertEqual(content, self.longStr2)

    def test_print_unallocated(self):
        """Test the printing of all persons who are yet to be given a room."""
        Dojo.create_room('office', ['red'])
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        content = Dojo.print_unallocated()
        self.assertEqual(content, self.longStr2)

    def test_reallocate_person_to_office(self):
        """Test the reallocation of a person from an office to another."""
        Dojo.create_room('office', ['red'])
        initial_red_room_count = len(Dojo.all_office[0].room_members)
        self.assertEqual(initial_red_room_count, 0)
        Dojo.add_person_input_check('ladi', 'adeniran', 'staff')
        second_red_room_count = len(Dojo.all_office[0].room_members)
        self.assertEqual(second_red_room_count, 1)
        person_id = list(Dojo.all_persons_in_dojo.keys())[0]
        Dojo.create_room('office', ['green'])
        initial_green_room_count = len(Dojo.all_office[1].room_members)
        self.assertEqual(initial_green_room_count, 0)
        Dojo.reallocate_person(person_id, 'green')
        second_green_room_count = len(Dojo.all_office[1].room_members)
        third_red_room_count = len(Dojo.all_office[0].room_members)
        self.assertEqual(second_green_room_count, 1)
        self.assertEqual(third_red_room_count, 0)

    def test_reallocate_person_to_ls(self):
        """Test the reallocation of a person from a living space to another."""
        Dojo.create_room('living', ['red'])
        initial_red_room_count = len(
            Dojo.all_living_space[0].room_members)
        self.assertEqual(initial_red_room_count, 0)
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        second_red_room_count = len(
            Dojo.all_living_space[0].room_members)
        self.assertEqual(second_red_room_count, 1)
        person_id = list(Dojo.all_persons_in_dojo)[0]
        Dojo.create_room('living', ['green'])
        initial_green_room_count = len(
            Dojo.all_living_space[1].room_members)
        self.assertEqual(initial_green_room_count, 0)
        Dojo.reallocate_person(person_id, 'green')
        second_green_room_count = len(
            Dojo.all_living_space[1].room_members)
        third_red_room_count = len(
            Dojo.all_living_space[0].room_members)
        self.assertEqual(second_green_room_count, 1)
        self.assertEqual(third_red_room_count, 0)

    def test_load_people(self):
        """Test the allocation of a person to a room from a text file."""
        Dojo.create_room('living', ['red'])
        Dojo.create_room('office', ['blue'])
        initial_red_room_count = len(
            Dojo.all_living_space[0].room_members)
        initial_blue_room_count = len(Dojo.all_office[0].room_members)
        self.assertEqual(initial_blue_room_count, 0)
        self.assertEqual(initial_red_room_count, 0)
        my_file = open('data/load.txt', 'w')
        my_file.write(self.longStr3)
        my_file.close()
        Dojo.load_people('load')
        second_red_room_count = len(
            Dojo.all_living_space[0].room_members)
        second_blue_room_count = len(Dojo.all_office[0].room_members)
        self.assertEqual(second_blue_room_count, 6)
        self.assertEqual(second_red_room_count, 4)

    def test_save_state(self):
        """Test the saving of all data in the app to a database."""
        Dojo.create_room('living', ['red', 'green'])
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        Dojo.save_state('test_db')
        database = DbConnector('database/db.sqlite3')
        database_session = database.Session
        for instance in database_session.query(LivingSpaceData):
            saved_data = instance.living_space_objs
            first_room_name = saved_data[0].room_name
            second_room_name = saved_data[1].room_name
            self.assertEqual(second_room_name, 'green')
            self.assertEqual(first_room_name, 'red')
        database_session.close()
        for instance in database_session.query(PersonData):
            saved_data = instance.person_objs
            database_person_id = list(saved_data)[0]
            database_fullname = saved_data[database_person_id].full_name
            dojo_person_id = list(Dojo.all_persons_in_dojo)[0]
            dojo_fullname = Dojo.all_persons_in_dojo[dojo_person_id].full_name
            self.assertEqual(database_fullname, dojo_fullname)
        database_session.close()
        os.remove("database/db.sqlite3")

    def test_load_state(self):
        """Test the Loading of all data from the database to the app."""
        Dojo.create_room('living', ['red', 'green'])
        Dojo.add_person_input_check('ladi', 'adeniran', 'fellow', 'y')
        Dojo.add_person_input_check('bolaji', 'olajide', 'fellow', 'y')
        initial_unallocated_count = len(Dojo.unallocated_persons)
        self.assertEqual(initial_unallocated_count, 2)
        Dojo.save_state('test_db')
        self.tearDown()
        second_unallocated_count = len(Dojo.unallocated_persons)
        self.assertEqual(second_unallocated_count, 0)
        Dojo.load_state('test_db')
        third_unallocated_count = len(Dojo.unallocated_persons)
        self.assertEqual(third_unallocated_count, 2)
