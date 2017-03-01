import operator
import random

from app.person import Fellow, Person, Staff
from app.room import LivingSpace, Office, Room


class Dojo(object):
    rooms_in_dojo = {}
    all_persons_in_dojo = {}
    all_office = []
    all_living_space = []
    unallocated_persons = {}

    def create_room(self, room_type, room_name):
        output = ""
        for room in room_name:
            if room in Dojo.rooms_in_dojo:
                output = output + ('Room already exist.\n')
            elif not room.isalnum():
                output = output + ('Invalid room naming convention!\n')
            elif room_type == 'office':
                new_room = Office(room)
                self.all_office.append(new_room)
                self.rooms_in_dojo[new_room.room_name] = new_room.room_type
                output = output + \
                    ('An office called %s has been created.\n' % room)
            elif room_type == 'living':
                new_room = LivingSpace(room)
                self.all_living_space.append(new_room)
                self.rooms_in_dojo[new_room.room_name] = new_room.room_type
                output = output + \
                    ('A living space called %s has been created.\n' % room)
            elif room_type != 'living' and room_type != 'office':
                output = output + ('Invalid command.\nFirst argument must be either'
                                   ' office or living.\n')
        return output

    def add_person_input_check(self, first_name, last_name, person_type, wants_accomodation='n'):
        if wants_accomodation == 'y' or wants_accomodation == 'n':
            if person_type == 'fellow':
                if first_name.isalpha() and last_name.isalpha():
                    self.add_fellow(first_name, last_name,
                                    person_type, wants_accomodation)
                else:
                    return('First name and last name can only be alphabets.')
            elif person_type == 'staff':
                if first_name.isalpha() and last_name.isalpha():
                    self.add_staff(first_name, last_name,
                                   person_type, wants_accomodation)
            else:
                return('A person can only be a fellow or a staff.')
        else:
            print("wants_accomodation can only be 'Y' or 'N'.")

    def get_available_room(self, room_type):
        """ Gets any available office at random"""
        available_room = []
        if room_type == 'office':
            for room in self.all_office:
                if len(room.room_members) < 6:
                    available_room.append(room)
            if available_room:
                return(random.choice(available_room))
        else:
            for room in self.all_living_space:
                if len(room.room_members) < 4:
                    available_room.append(room)
            if available_room:
                return(random.choice(available_room))

    def add_fellow(self, first_name, last_name,
                   person_type, wants_accomodation='n'):
        full_name = first_name + ' ' + last_name
        new_person = Fellow(first_name, last_name)
        if wants_accomodation == 'y':
            person_living = self.get_available_room('living')
            person_office = self.get_available_room('office')
            if person_living and person_office:
                self.all_persons_in_dojo[new_person.unique_id] = new_person
                person_living.room_members[
                    new_person.unique_id] = new_person
                person_office.room_members[
                    new_person.unique_id] = new_person
                new_person.assigned_room[
                    'living'] = person_living
                new_person.assigned_room[
                    'office'] = person_office
                return(new_person.full_name + ' with I.D number '
                       + new_person.unique_id + ' has been allocated the '
                       + person_living.room_type + ' ' + person_living.room_name)
            elif person_office is None and person_living is None:
                self.unallocated_persons[new_person.unique_id] = [
                    new_person.full_name, 'Living Space']
                self.unallocated_persons[new_person.unique_id] = [
                    new_person.full_name, 'Office']
                return('No office and living room available.')
            elif person_office:
                self.all_persons_in_dojo[new_person.unique_id] = new_person
                person_office.room_members[
                    new_person.unique_id] = new_person
                new_person.assigned_room[
                    'office'] = person_office
                self.unallocated_persons[new_person.unique_id] = [
                    new_person.full_name, 'Living Space']
                return(new_person.full_name + ' with I.D number '
                       + new_person.unique_id + ' has been allocated the '
                       + person_office.room_type + ' ' + person_office.room_name
                       + '\n Only an Office was allocated. No available Living Space.')
            else:
                self.all_persons_in_dojo[new_person.unique_id] = new_person
                person_living.room_members[
                    new_person.unique_id] = new_person
                new_person.assigned_room[
                    'living'] = person_living
                self.unallocated_persons[new_person.unique_id] = [
                    new_person.full_name, 'Office']
                return(new_person.full_name + ' with I.D number '
                       + new_person.unique_id + ' has been allocated the '
                       + person_living.room_type + ' ' + person_living.room_name
                       + '\n Only a Living Space was allocated. No available Office.')
        else:
            person_office = self.get_available_room('office')
            if person_office:
                self.all_persons_in_dojo[new_person.unique_id] = new_person
                person_office.room_members[
                    new_person.unique_id] = new_person
                new_person.assigned_room[
                    'office'] = person_office
                return(new_person.full_name + ' with I.D number '
                       + new_person.unique_id + ' has been allocated the '
                       + person_office.room_type + ' ' + person_office.room_name)
            else:
                self.unallocated_persons[
                    new_person.unique_id] = [new_person.full_name, 'Office']
                return('No Office available.')

    def add_staff(self, first_name, last_name, person_type, wants_accomodation='n'):
        new_person = Staff(first_name, last_name)
        person_office = self.get_available_room('office')
        if wants_accomodation == 'y' and person_office:
            self.all_persons_in_dojo[new_person.unique_id] = new_person
            person_office.room_members[new_person.unique_id] = new_person
            output = '\nSorry. Only fellows can have a living space.'
            return(new_person.full_name + ' with I.D number '
                   + new_person.unique_id + ' has been allocated the '
                   + person_office.room_type + ' '
                   + person_office.room_name + output)
        elif person_office:
            self.all_persons_in_dojo[new_person.unique_id] = new_person
            person_office.room_members[new_person.unique_id] = new_person
            new_person.assigned_room['office'] = person_office
            return(new_person.full_name + ' with I.D number '
                   + new_person.unique_id + ' has been allocated the '
                   + person_office.room_type + ' ' + person_office.room_name)
        else:
            self.unallocated_persons[
                new_person.unique_id] = [new_person.full_name, 'Office']
            return('No office is available.')

    def print_room(self, room_name):
        """ Gets any given room if created and
         prints out the occupants if any."""
        combine_rooms = self.all_living_space + self.all_office
        if any(x.room_name == room_name for x in combine_rooms):
            for room in combine_rooms:
                if room.room_name == room_name:
                    if not any(room.room_members):
                        return('There are no occupants in ' +
                               room.room_name + ' at the moment.')
                    else:
                        output = ''
                        for key in sorted(room.room_members.values(),
                                          key=operator.attrgetter('full_name')):
                            output += key.full_name + ' --> ' \
                                + key.person_type + '\n'
                        return (output)
        else:
            return('No room named', room_name, 'at the moment.')
