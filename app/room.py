"""This module handles the creation of Offices and Living space."""


class Room(object):
    """Create a Room object."""

    def __init__(self, room_name):
        """Initialize Room object with set variable name."""
        self.room_name = room_name
        self.room_members = {}


class Office(Room):
    """Create an Office object with set variable name."""

    def __init__(self, room_name):
        """Initialize Office object with set variable name."""
        super(Office, self).__init__(room_name)
        self.room_type = 'office'


class LivingSpace(Room):
    """Create LivingSpace objects with set variable name."""

    def __init__(self, room_name):
        """Initialize LivingSpace object with set variable name."""
        super(LivingSpace, self).__init__(room_name)
        self.room_type = 'living'
