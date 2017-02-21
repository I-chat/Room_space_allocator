import random


class Person(object):
    """Creates a Person object"""
    person_id = {}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = (first_name + ' ' + last_name)


class Staff(Person):
    """Creates a Staff object that inherits properties from the Person class"""
    assigned_room = {}
    staff_id = 'DJ-S-' + str(random.randint(0x1000, 0x270F))

    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)
        self.person_type = 'staff'
        self.unique_id = self.id_generator()

    def id_generator(self):
        staff_id = 'DJ-S-' + str(random.randint(0x1000, 0x270F))
        while staff_id in list(self.person_id.values()):
            staff_id = 'DJ-S-' + str(random.randint(0x1000, 0x270F))
        self.person_id[staff_id] = self.full_name
        return(staff_id)


class Fellow(Person):
    """Creates a Fellow object that inherits properties from the Person class"""
    assigned_room = {}
    fellow_id = 'DJ-F-' + str(random.randint(0x1000, 0x270F))

    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(first_name, last_name)
        self.person_type = 'fellow'
        self.unique_id = self.id_generator()

    def id_generator(self):
        fellow_id = 'DJ-F-' + str(random.randint(0x1000, 0x270F))
        while fellow_id in list(self.person_id.values()):
            fellow_id = 'DJ-F-' + str(random.randint(0x1000, 0x270F))
        self.person_id[fellow_id] = self.full_name
        return(fellow_id)
