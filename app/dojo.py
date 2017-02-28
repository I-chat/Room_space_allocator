from app.person import Fellow, Person, Staff
from app.room import LivingSpace, Office, Room


class Dojo(object):
    rooms_in_dojo = {}
    persons_in_dojo = {}
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
