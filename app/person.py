import random


class Person(object):
    """Creates a Person object"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = (first_name + ' ' + last_name)
        self.assigned_room = {}


class Staff(Person):
    """Creates a Staff object that inherits properties from the Person class"""

    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(first_name, last_name)
        self.person_type = 'staff'


class Fellow(Person):
    """Creates a Fellow object that inherits properties from the Person class"""

    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(first_name, last_name)
        self.person_type = 'fellow'
