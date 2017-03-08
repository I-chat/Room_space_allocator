#!/usr/bin/env python
"""
This module uses docopt with the built in cmd module to pass arguments from the
command to any other module or app.

Usage:
    room_allocator create_room <office|living> <room_name>...
    room_allocator add_person <person_first_name> <person_last_name>
    <fellow|staff> [--wants_accomodation=n]
    room_allocator print_room <room_name>
    room_allocator print_allocations [-o=filename]
    room_allocator print_unallocated [-o=filename]
    room_allocator reallocate_person <person_identifier> <new_room_name>
    room_allocator load_people <--o=filename>
    room_allocator save_state [--db=sqlite_database]
    room_allocator load_state <sqlite_database>
    room_allocator (-h | --help | --version)
Options:
    -h, --help  Show this screen and exit.
"""

import cmd
from docopt import docopt, DocoptExit

from app.dojo import Dojo


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    """Enter Interactive mode."""

    intro = 'Welcome to Room Allocator!' \
        + ' (type help for a list of commands.)'
    prompt = '(Room Allocator) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_name = arg["<room_name>"]
        room_type = arg["<room_type>"]
        if room_type == 'office' or room_type == 'living':
            if all([x.isalnum() for x in room_name]):
                print(Dojo.create_room(room_type, room_name))
            else:
                print('Room name should only contain alphanumeric characters.')
        else:
            print('room_type can only accept \'office\' or \'living\' input.')

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_first_name> <person_last_name>
        <designation> [<--wants_accomodation>]"""
        first_name = arg["<person_first_name>"].lower()
        last_name = arg["<person_last_name>"].lower()
        person_type = arg["<designation>"].lower()
        wants_accomodation = arg["<--wants_accomodation>"]
        if wants_accomodation is None:
            wants_accomodation = 'n'
        if (wants_accomodation == 'y' or wants_accomodation == 'n'):
            if person_type == 'fellow' or person_type == 'staff':
                if first_name.isalpha() and last_name.isalpha():
                    print(Dojo.add_person_input_check(first_name, last_name,
                                                      person_type,
                                                      wants_accomodation))
                else:
                    print('First name and last name can only be alphabets.')
            else:
                print('A person can only be a fellow or a staff.')
        else:
            print("wants_accomodation can only be 'Y' or 'N'.")

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        room_name = arg["<room_name>"].lower()
        if room_name.isalnum():
            print(Dojo.print_room(room_name))
        else:
            print('Room name should only contain alphanumeric characters.')

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=<filename>]"""
        file_name = arg['--o']
        print(Dojo.print_allocations(file_name))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=<filename>]"""
        filename = arg['--o']
        print(Dojo.print_unallocated(filename))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        person_id = arg["<person_identifier>"].upper()
        room_name = arg["<new_room_name>"].lower()
        print(Dojo.reallocate_person(person_id, room_name))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people <filename>"""
        filename = arg["<filename>"]
        print(Dojo.load_people(filename))

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=<sqlite_database>]"""
        database_name = arg["--db"]
        print(Dojo.save_state(database_name))

    @docopt_cmd
    def do_load_state(self, arg):
        """"Usage: load_state <sqlite_database>"""
        database_name = arg["<sqlite_database>"]
        print(Dojo.load_state(database_name))

    def do_quit(self, arg):
        """Quit out of Interactive Mode."""
        print('Good Bye!')
        exit()


MyInteractive().cmdloop()
