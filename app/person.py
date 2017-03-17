"""This module handles the creation of Fellows and Staff."""


class Person(object):
    """Create a Person object."""

    def __init__(self, first_name, last_name):
        """Initialize Person object with set variable names."""
        self.first_name = first_name
        self.last_name = last_name
        self.assigned_rooms = {'my_office': '', 'my_livingspace': ''}


class Staff(Person):
    """Create a Staff object that inherits properties from the Person class."""

    def __init__(self, first_name, last_name):
        """Initialize Staff object with set variable names."""
        super(Staff, self).__init__(first_name, last_name)
        self.person_type = 'staff'


class Fellow(Person):
    """Create a Fellow object that inherits.

    properties from the Person class.
    """

    def __init__(self, first_name, last_name):
        """Initialize Fellow object with set variable names."""
        super(Fellow, self).__init__(first_name, last_name)
        self.person_type = 'fellow'
