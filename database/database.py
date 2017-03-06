"""This module handles the creation is database tables, mapping of objects.

to respective tables and creating a connection to the database.
"""


from sqlalchemy import Column, Integer, PickleType, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class OfficeData(Base):
    """Declare a mapping for Office objects."""

    __tablename__ = 'office'

    office_id = Column(Integer, primary_key=True)
    office_objs = Column(PickleType)


class LivingSpaceData(Base):
    """Declare a mapping for LivingSpace objects."""

    __tablename__ = 'living space'

    living_space_id = Column(Integer, primary_key=True)
    living_space_objs = Column(PickleType)


class PersonData(Base):
    """Declare a mapping for persons_in_dojo in dojo dictionary."""

    __tablename__ = 'persons_in_dojo'

    person_id = Column(Integer, primary_key=True)
    person_objs = Column(PickleType)


class UnallocatedData(Base):
    """Declare a mapping for unallocated persons dictionary."""

    __tablename__ = 'unallocated_persons'

    person_id = Column(Integer, primary_key=True)
    person_objs = Column(PickleType)


class DbConnector(object):
    """Create a connection to a given database."""

    def __init__(self, database_name):
        """Initialize connection with the given attributes."""
        self.database_name = database_name
        self.engine = create_engine(
            'sqlite:///' + self.database_name, echo=False)
        self.Session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)
