"""This module is imported to the test script to test the functionalities."""

import os
import random

from app.person import Fellow, Staff
from app.room import LivingSpace, Office
from database.database import (OfficeData, DbConnector, UnallocatedData,
                               PersonData, LivingSpaceData)


class Dojo(object):
    """Manage the rooms and persons in the building."""

    all_office = []
    all_living_space = []
    all_persons_in_dojo = {}
    unallocated_persons = {}

    @classmethod
    def create_room(cls, room_type, room_name):
        """Instantiate Room objects."""
        output = ""
        for name in room_name:
            combine_rooms = cls.all_office + cls.all_living_space
            if name.lower() in [room.room_name for room in combine_rooms]:
                output = output + ('Room already exist.\n')
            elif room_type == 'office':
                new_room = Office(name.lower())
                cls.all_office.append(new_room)
                output = output + \
                    ('An office called %s has been successfully created!\n'
                        % name.capitalize())
            elif room_type == 'livingspace':
                new_room = LivingSpace(name.lower())
                cls.all_living_space.append(new_room)
                output = output + \
                    ('A livingspace called %s has been successfully created!\n'
                        % name.capitalize())
        return output

    @classmethod
    def remove_person(cls, person_id):
        """Remove a person from dojo."""
        if person_id in cls.all_persons_in_dojo and\
                person_id in cls.unallocated_persons:
            cls.remove_from_room(person_id)
            del cls.all_persons_in_dojo[person_id]
            del cls.unallocated_persons[person_id]
            return(person_id + " has been successfully removed.")
        elif person_id in cls.all_persons_in_dojo:
            cls.remove_from_room(person_id)
            del cls.all_persons_in_dojo[person_id]
            return(person_id + " has been successfully removed.")
        else:
            return('Invalid identification number.')

    @classmethod
    def remove_from_room(cls, person_id):
        """Remove a person from is all assigned room."""
        if type(cls.all_persons_in_dojo[person_id].assigned_rooms['my_office'])\
                is Office:
            del cls.all_persons_in_dojo[
                person_id].assigned_rooms['my_office'].room_members[
                person_id]
        if type(cls.all_persons_in_dojo[person_id]
                .assigned_rooms['my_livingspace']) is LivingSpace:
            del cls.all_persons_in_dojo[
                person_id].assigned_rooms['my_livingspace'].room_members[
                person_id]

    @classmethod
    def print_all_persons(cls):
        """Print all persons in Dojo."""
        if len(cls.all_persons_in_dojo) > 0:
            output = "Occupants in Dojo\n-------------------\n"
            for key, value in cls.all_persons_in_dojo.items():
                output += key + ' ' + value.first_name\
                        + ' ' + value.last_name + '\n'
            return(output)
        else:
            return("Dojo is currently empty.")

    @classmethod
    def add_person_input_check(cls, first_name, last_name,
                               person_type, wants_accomodation='n'):
        """Check for Invalid inputs."""
        if not (first_name.isalpha() and last_name.isalpha()):
            return('First name and last name can only be alphabets.')
        if wants_accomodation not in ['y', 'n']:
            return("wants_accomodation can only be 'Y' or 'N'.")
        if person_type == 'fellow':
            return(cls.add_fellow(first_name, last_name, person_type,
                                  wants_accomodation))
        elif person_type == 'staff':
            return(cls.add_staff(first_name, last_name, person_type,
                                 wants_accomodation))
        else:
            return('A person can only be a fellow or a staff.')

    @classmethod
    def id_generator(cls, person_type):
        """Generate unique I.Ds for every Person object."""
        if person_type == 'staff':
            staff_id = 'DJ-S-' + str(random.randint(0x1000, 0x270F))
            while staff_id in cls.all_persons_in_dojo:
                staff_id = 'DJ-S-' + str(random.randint(0x1000, 0x270F))
            return(staff_id)
        else:
            fellow_id = 'DJ-F-' + str(random.randint(0x1000, 0x270F))
            while fellow_id in cls.all_persons_in_dojo:
                fellow_id = 'DJ-F-' + str(random.randint(0x1000, 0x270F))
            return(fellow_id)

    @classmethod
    def allocate_office(cls, person_id, office_obj, person_obj):
        """Allocate an office."""
        cls.all_persons_in_dojo[person_id] = person_obj
        office_obj.room_members[
            person_id] = person_obj
        person_obj.assigned_rooms[
            'my_office'] = office_obj
        return(person_obj.first_name.capitalize() + ' has been allocated the '
               + 'office ' + office_obj.room_name.capitalize() + '\n')

    @classmethod
    def allocate_living(cls, person_id, living_obj, person_obj):
        """Allocate a living space."""
        living_obj.room_members[person_id] = person_obj
        person_obj.assigned_rooms[
            'my_livingspace'] = living_obj
        return(person_obj.first_name.capitalize() + ' has been allocated the '
               + 'livingspace ' + living_obj.room_name.capitalize() + '\n')

    @classmethod
    def add_fellow(cls, first_name, last_name,
                   person_type, wants_accomodation='n'):
        """Instantiate Fellow objects and add them to rooms."""
        new_person = Fellow(first_name, last_name)
        unique_id = cls.id_generator(person_type)
        person_living = cls.get_available_room('livingspace')
        person_office = cls.get_available_room('office')
        if wants_accomodation == 'y':
            if person_living and person_office:
                result1 = cls.allocate_office(unique_id, person_office,
                                              new_person)
                result2 = cls.allocate_living(unique_id, person_living,
                                              new_person)
                return('Fellow {first} {last} has been successfully added.\n'
                       + result1 + result2).format(first=first_name.
                                                   capitalize(),
                                                   last=last_name.capitalize())
            elif person_office is None and person_living is None:
                cls.all_persons_in_dojo[unique_id] = new_person
                cls.unallocated_persons[unique_id] = [
                    new_person.first_name + ' ' + new_person.last_name,
                    'living space', 'office']
                return('Fellow {first} {last} has been successfully added.\n'
                       '{first} has been placed on the waiting list, no office'
                       ' available.\n{first} has been placed on the waiting'
                       ' list, no livingspace available.\n')\
                    .format(first=first_name.capitalize(),
                            last=last_name.capitalize())
            elif person_office:
                result1 = cls.allocate_office(unique_id, person_office,
                                              new_person)
                cls.unallocated_persons[unique_id] = [
                    new_person.first_name + ' ' + new_person.last_name,
                    'living space']
                return('Fellow {first} {last} has been successfully added.\n'
                       + result1 + '{first} has been placed on the waiting'
                       ' list, no livingspace available.\n')\
                    .format(first=first_name.capitalize(),
                            last=last_name.capitalize())
            else:
                cls.all_persons_in_dojo[unique_id] = new_person
                result1 = cls.allocate_living(unique_id,
                                              person_living, new_person)
                cls.unallocated_persons[unique_id] = [
                    new_person.first_name + ' ' + new_person.last_name,
                    'office']
                return('Fellow {first} {last} has been successfully added.\n'
                       + result1 + '{first} has been placed on the waiting'
                       ' list, no office available.\n')\
                    .format(first=first_name.capitalize(),
                            last=last_name.capitalize())
        else:
            person_office = cls.get_available_room('office')
            if person_office:
                result1 = cls.allocate_office(unique_id, person_office,
                                              new_person)
                return('Fellow {first} {last} has been successfully added.\n'
                       + result1).format(first=first_name.capitalize(),
                                         last=last_name.capitalize())
            else:
                cls.all_persons_in_dojo[unique_id] = new_person
                cls.unallocated_persons[
                    unique_id] = [new_person.first_name + ' '
                                  + new_person.last_name, 'office']
                return('Fellow {first} {last} has been successfully added.\n'
                       '{first} has been placed on the waiting list,'
                       ' no office available.\n')\
                    .format(first=first_name.capitalize(),
                            last=last_name.capitalize())

    @classmethod
    def add_staff(cls, first_name, last_name, person_type,
                  wants_accomodation='n'):
        """Instantiate staff objects and add them to rooms."""
        new_person = Staff(first_name, last_name)
        unique_id = cls.id_generator(person_type)
        person_office = cls.get_available_room('office')
        if wants_accomodation == 'y' and not person_office:
            cls.all_persons_in_dojo[unique_id] = new_person
            cls.unallocated_persons[
                unique_id] = [new_person.first_name + ' '
                              + new_person.last_name, 'office']
            return('Staff {first} {last} has been successfully added.\n'
                   '{first} has been placed on the waiting list,'
                   ' no office available.\n'
                   'Sorry. Only fellows can have a living space.\n'
                   .format(first=first_name.capitalize(),
                           last=last_name.capitalize()))
        elif wants_accomodation == 'y' and person_office:
            result = cls.allocate_office(unique_id, person_office, new_person)
            output = 'Sorry. Only fellows can have a living space.'
            return('Staff {first} {last} has been successfully added.\n'
                   + result + output + '\n').format(
                   first=first_name.capitalize(),
                   last=last_name.capitalize())
        elif person_office:
            result = cls.allocate_office(unique_id, person_office, new_person)
            new_person.assigned_rooms['my_office'] = person_office
            return('Staff {first} {last} has been successfully added.\n'
                   + result).format(first=first_name.capitalize(),
                                    last=last_name.capitalize())
        else:
            cls.unallocated_persons[
                unique_id] = [new_person.first_name + ' '
                              + new_person.last_name, 'office']
            cls.all_persons_in_dojo[unique_id] = new_person
            return('Staff {first} {last} has been successfully added.\n'
                   '{first} has been placed on the waiting list,'
                   ' no office available.\n')\
                .format(first=first_name.capitalize(),
                        last=last_name.capitalize())

    @classmethod
    def get_available_room(cls, room_type):
        """Get any available office at random."""
        available_room = []
        if room_type == 'office':
            for room in cls.all_office:
                if len(room.room_members) < 6:
                    available_room.append(room)
            if available_room:
                return(random.choice(available_room))
        else:
            for room in cls.all_living_space:
                if len(room.room_members) < 4:
                    available_room.append(room)
            if available_room:
                return(random.choice(available_room))

    @classmethod
    def print_room(cls, room_name):
        """Get any given room if created and print out the occupants if any."""
        combine_rooms = cls.all_living_space + cls.all_office
        if any(x.room_name == room_name.lower() for x in combine_rooms):
            for room in combine_rooms:
                if room.room_name == room_name.lower():
                    if not any(room.room_members):
                        return ('There are no occupants in ' +
                                room.room_name + ' at the moment.')
                    else:
                        output = ''
                        for key in room.room_members.values():
                            output += key.first_name + ' ' + key.last_name\
                                + ' --> ' + key.person_type + '\n'
                        return (output)
        else:
            return 'No room named ' + room_name + ' at the moment.'

    @classmethod
    def generate_allocation_list(cls, room_list):
        """Generate a list of all allocated persons."""
        output = ""
        for room in room_list:
            if len(room.room_members) > 0:
                output += room.room_name.upper() + '\n'
                output += ('-' * 30) + '\n'
                output += (', '.join(
                            [obj.first_name + ' ' + obj.last_name for obj in
                             room.room_members.values()]) + '\n')
        if output:
            return(output)
        else:
            return('There are no occupants in any room.')

    @classmethod
    def print_allocations(cls, filename=''):
        """Get a list of rooms and their respective occupants."""
        combine_rooms = cls.all_living_space + cls.all_office
        unempty_room = [room for room in
                        combine_rooms if len(room.room_members) > 0]
        if filename:
            if '.txt' in filename:
                path = 'data/' + filename
            else:
                path = 'data/' + filename + '.txt'
            print('logging all allocated persons to ' + path + '...')
            result = cls.generate_allocation_list(unempty_room)
            my_file = open(path, 'w')
            if result.endswith("room."):
                return(result)
            else:
                my_file.write(result)
                return('Logging of allocated persons complete.')
        else:
            return(cls.generate_allocation_list(unempty_room))

    @classmethod
    def generate_unallocated_list(cls):
        """Generate a list of all unallocated persons."""
        head = 'UNALLOCATED LIST\n'
        head = head + ('-' * 30) + '\n'
        if len(cls.unallocated_persons) > 0:
            output = ''
            for key, value in sorted(cls.unallocated_persons.items()):
                v3_value = ', ' + value[2] if len(value) == 3 else ""
                output = output + ('{v0}: {v1}: {v2}{v3}\n'.format(
                    v0=key, v1=value[0], v2=value[1], v3=v3_value))
            return(head + output)
        else:
            return('There are no unallocated persons.')

    @classmethod
    def print_unallocated(cls, filename=''):
        """Get a list of unallocated persons."""
        if filename:
            if '.txt' in filename:
                path = 'data/' + filename
            else:
                path = 'data/' + filename + '.txt'

            result = cls.generate_unallocated_list()

            if result.endswith("persons."):
                return('There are no unallocated persons.')
            else:
                my_file = open(path, 'w')
                my_file.write(result)
                return("Logging of unallocated persons complete.")
        else:
            result = cls.generate_unallocated_list()
            return(result)

    @classmethod
    def reallocate_person(cls, person_id, room_name):
        """Check if room is existing and if there is a vacant space."""
        office_obj = [
            room for room in cls.all_office if room.room_name == room_name]
        if office_obj:
            if len(office_obj[0].room_members) == 6:
                return('Room is already filled to capacity.')
            elif person_id in office_obj[0].room_members:
                return (person_id + ' is already a member of room '
                        + room_name)
            else:
                return(cls.reallocate_person_to_office(
                    person_id, room_name, office_obj[0]))
        elif not office_obj:
            living_obj = [room for room in
                          cls.all_living_space if room.room_name == room_name]
            if living_obj:
                if len(living_obj[0].room_members) == 4:
                    return('Room is already filled to capacity.')
                elif person_id in living_obj[0].room_members:
                    return(person_id + 'is already a member of room'
                           + room_name)
                else:
                    return(cls.reallocate_person_to_ls(
                        person_id, room_name, living_obj[0]))
            else:
                return(room_name, 'does not exist.')
        else:
            return(room_name, 'does not exist.')

    @classmethod
    def reallocate_person_to_office(cls, person_id, room_name, room_obj):
        """Reallocate a person from one office to another."""
        if person_id in cls.all_persons_in_dojo:
            if type(cls.all_persons_in_dojo[person_id]
                    .assigned_rooms['my_office']) is Office:
                del cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_office'].room_members[person_id]
                room_obj.room_members[
                    person_id] = cls.all_persons_in_dojo[person_id]
                cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_office'] = room_obj
                return(person_id + ' has been successfully rellocated.')
            elif 'office' in cls.unallocated_persons[person_id]:
                cls.unallocated_persons[person_id].remove('office')
                if len(cls.unallocated_persons[person_id]) <= 1:
                    del cls.unallocated_persons[person_id]
                room_obj.room_members[
                    person_id] = cls.all_persons_in_dojo[person_id]
                cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_office'] = room_obj
                return(person_id + ' has been successfully reallocated.')
            else:
                return(person_id + ' is yet to be allocated an office.')
        else:
            return('Invalid identification number')

    @classmethod
    def reallocate_person_to_ls(cls, person_id, room_name, room_obj):
        """Reallocate a person from a living space to another."""
        if person_id in cls.all_persons_in_dojo:
            if type(cls.all_persons_in_dojo[person_id]
                    .assigned_rooms['my_livingspace']) is LivingSpace:
                del cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_livingspace'].room_members[person_id]
                room_obj.room_members[
                    person_id] = cls.all_persons_in_dojo[person_id]
                cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_livingspace'] = room_obj
                return(person_id + ' has been successfully rellocated.')
            elif 'living space' in cls.unallocated_persons[person_id]:
                cls.unallocated_persons[person_id].remove('living space')
                if len(cls.unallocated_persons[person_id]) <= 1:
                    del cls.unallocated_persons[person_id]
                room_obj.room_members[
                    person_id] = cls.all_persons_in_dojo[person_id]
                cls.all_persons_in_dojo[person_id].assigned_rooms[
                    'my_livingspace'] = room_obj
                return(person_id + ' has been successfully reallocated.')
            else:
                return(person_id + ' is yet to be allocated a living space.')
        else:
            return('Invalid identification number')

    @classmethod
    def load_people(cls, filename):
        """Allocate people to rooms directly from a text file."""
        if '.txt' in filename:
            paths = 'data/' + filename
        else:
            paths = 'data/' + filename + '.txt'

        if os.path.isfile(paths):
            my_file = open(paths)
            output = ""
            for line in my_file:
                arg = line.split()
                if len(arg) == 4:
                    output += cls.add_person_input_check(arg[0].lower(),
                                                         arg[1].lower(),
                                                         arg[2].lower(),
                                                         arg[3].lower())
                elif len(arg) == 3:
                    output += cls.add_person_input_check(arg[0].lower(),
                                                         arg[1].lower(),
                                                         arg[2].lower(),
                                                         wants_accomodation='n'
                                                         )
                else:
                    output += "Incorrect length of parameters."
            return output
        else:
            return("No file named " + filename + " in the data folder.")

    @classmethod
    def save_state(cls, database_name):
        """Persist all current data in the app to a database."""
        print('Saving current state to database....')
        if database_name:
            path = 'database/' + database_name + '.sqlite3'
        else:
            path = 'database/db.sqlite3'
        if os.path.isfile(path):
            return("Permission Denied. You specified an already existing"
                   "database. Kindly choose another.")
        else:
            database = DbConnector(path)

        database_session = database.Session

        living_space_list = LivingSpaceData(
            living_space_objs=cls.all_living_space)
        database_session.add(living_space_list)
        database_session.commit()

        office_list = OfficeData(office_objs=cls.all_office)
        database_session.add(office_list)
        database_session.commit()

        person_dict = PersonData(person_objs=cls.all_persons_in_dojo)
        database_session.add(person_dict)
        database_session.commit()

        unallocated = UnallocatedData(person_objs=cls.unallocated_persons)
        database_session.add(unallocated)
        database_session.commit()

        return("The current state has been successfully saved."
               "You can now quit the application.")

    @classmethod
    def load_state(cls, database_name):
        """Query and load all app data from database back to the app."""
        print("Loading past state from database....")
        path = 'database/' + database_name + '.sqlite3'

        if not os.path.isfile(path):
            return("You have not specified an existing database."
                   " Kindly specify one.")
        else:
            database = DbConnector(path)

        database_session = database.Session
        for instance in database_session.query(OfficeData):
            cls.all_office = instance.office_objs
        database_session.close()
        for instance in database_session.query(LivingSpaceData):
            cls.all_living_space = instance.living_space_objs
        database_session.close()
        for instance in database_session.query(PersonData):
            cls.all_persons_in_dojo = instance.person_objs
        database_session.close()
        for instance in database_session.query(UnallocatedData):
            cls.unallocated_persons = instance.person_objs
        database_session.close()

        return("The past state has been successfully loaded.")
