# Room_space_allocator
[![Build Status](https://travis-ci.org/andela-iikikin/Room_space_allocator.svg?branch=wip)](https://travis-ci.org/andela-iikikin/Room_space_allocator)
[![Coverage Status](https://coveralls.io/repos/github/andela-iikikin/Room_space_allocator/badge.svg?branch=wip)](https://coveralls.io/github/andela-iikikin/Room_space_allocator?branch=wip)

Room_space_allocator is a python3 program that allocates room based on different designations.

## Introduction
* **`Room_space_allocator`** is a Python command line program that allocates different rooms to different persons based on their designations.
* It has the Following Features;
    - **`create_room <room_type> <room_name>...`** Creates rooms in Dojo. Using this command, the user can create as many rooms as possible by specifying multiple room names after the create_room command.
    - **`add_person <person_name> <FELLOW|STAFF> [wants_accommodation]`** Adds a person to the system and allocates the person to a random room. `wants_accommodation` is an optional argument which can be either Y or N. The default value if it is not provided is N.
    - **`print_room <room_name>`** Prints  the names of all the people in `room_name` on the screen.
    - **`print_allocations [-o=filename]`** Prints a list of allocations onto the screen. Specifying the optional -o option here outputs the registered allocations to a txt file and stores it in the folder name data.
    - **`print_unallocated [-o=filename]`** Prints a list of unallocated people to the screen. Specifying the -o option here outputs the information to a txt file and stores it in the folder name data.
    - **`reallocate_person <person_identifier> <new_room_name>`** Reallocate the person with person_identifier to new_room_name.
    - **`remove_person <person_identifier>`** Remove the person with person_identifier from the system.
    - **`print_all_persons`** Print everyone in the system to the screen.
    - **`load_people <filename>`** Adds people to rooms from a load_people txt file in the data folder.
    - **`save_state [--db=sqlite_database]`** Stores all the data stored in the app to an SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
    - **`load_state <sqlite_database>`** Loads data from a database into the application.

## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/) - Python is a programming language that lets you work quickly
and integrate systems more effectively.
* [Docopt](http://docopt.org/) - A command line description framework.
* [Nose](https://pypi.python.org/pypi/nose/1.3.7) - Nose extends the test loading and running features of unittest, making
it easier to write, find and run tests.
* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/) - A set of extensions to Ian Bicking’s [virtualenv](https://pypi.python.org/pypi/virtualenv) tool. The extensions include wrappers for creating and deleting virtual environments for Unix based OS and [Virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win) for Windows

## How to Install
### On a Unix based OS
* Install python 3 using `sudo apt-get install python3-dev`
* Install Virtualenvwrapper using `pip install Virtualenvwrapper`
* Make a new virtual environment using `mkvirtualenv --python=python3 <env_name>`
* Activate the new virtual environment using `workon <env_name>`
* Download and extract the project.
* cd into Room_space_allocator folder and run `pip install -r requirements.txt` from the terminal.

### On Windows OS
* Download and install the [python 3](https://www.python.org/downloads/windows/) package for Windows.
* Install Virtualenvwrapper-win using `pip3 install Virtualenvwrapper-win`
* On the command line run `where python3` and copy the path to the python3 interpreter.
* Make a new virtual environment using `mkvirtualenv --python=<path to the python3 interpreter> <env_name>`
* Activate the new virtual environment using `workon <env_name>`
* Download and extract the project.
* cd into Room_space_allocator folder and run `pip install -r requirements.txt` from the command prompt.

## How to Use
### To run nose test
* cd into the project root directory
* run `nosetests`

### To use the functionalities
* cd into the project root directory and run `python main.py`
