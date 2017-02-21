# Room_space_allocator
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
    - **`load_people`** Adds people to rooms from a load_people txt file in the data folder.
    - **`save_state [--db=sqlite_database]`** Stores all the data stored in the app to an SQLite database. Specifying the --db parameter explicitly stores the data in the sqlite_database specified.
    - **`load_state <sqlite_database>`** Loads data from a database into the application.

## Dependencies
* Docopt
* Nose
* Virtualenvwrapper for Unix based OS and Virtualenvwrapper-win for Windows

## How to Install
* Install Virtualenvwrapper using `pip install Virtualenvwrapper`
* Make a new virtual environment using `mkvirtualenv --python=python3 <env_name>``
* Activate the new virtual environment using `workon <env_name>`
* Install nose using `pip install Nose`
* Install Docopt using `pip install docopt==0.6.2`

## How to Use
### To run nose test
* cd into the project root directory
* run `nosetests`
### To use the functionalities
* cd into the app directory in the project folder and run `python main.py`
