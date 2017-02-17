class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name
        self.room_persons = {}


class Office(Room):

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_type = 'office'


class LivingSpace(Room):

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'living'
