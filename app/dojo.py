from app.person import Fellow, Staff
from app.room import LivingSpace, Office, Room


class Dojo(object):
    all_rooms = {}
    dojo_persons = {}
    all_office = []
    all_ls = []
    unallocated = {}

    def create_room(self, room_type, room_name):
        output = ""
        for room in room_name:
            if room in Dojo.all_rooms:
                output = output + ('Room already exist.\n')
            elif not room.isalnum():
                output = output + ('Invalid room naming convention!.\n')
            elif room_type == 'office':
                new_room = Office(room)
                self.all_office.append(new_room)
                self.all_rooms[new_room.room_name] = new_room.room_type
                output = output + \
                    ('An office called %s has been created.\n' % room)
            elif room_type == 'living':
                new_room = LivingSpace(room)
                self.all_ls.append(new_room)
                self.all_rooms[new_room.room_name] = new_room.room_type
                output = output + \
                    ('A living space called %s has been created.\n' % room)
            elif room_type != 'living' and room_type != 'office':
                output = output + ('Invalid command.\nFirst argument must be either'
                                   'an office or living.\n')
        return output
