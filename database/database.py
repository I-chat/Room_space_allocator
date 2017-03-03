import sqlalchemy
from sqlalchemy import Column, Integer, PickleType, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class PersonData(Base):
    __tablename__ = 'person'

    person_id = Column(String, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    fullname = Column(String)
    person_type = Column(String)
    assigned_room = Column(PickleType)


class RoomData(Base):
    __tablename__ = 'room'

    room_id = Column(Integer, primary_key=True)
    name = Column(String)
    room_type = Column(String)
    members = Column(PickleType)


class DojoData(Base):
    __tablename__ = 'persons_in_dojo'

    person_id = Column(Integer, primary_key=True)
    person_obj = Column(PickleType)


class UnallocatedData(Base):
    __tablename__ = 'unallocated_persons'

    person_id = Column(Integer, primary_key=True)
    person_obj = Column(PickleType)


class DbConnector(object):

    def __init__(self, database_name):
        self.database_name = database_name
        self.engine = create_engine(
            'sqlite:///' + self.database_name, echo=False)
        self.Session = sessionmaker(bind=self.engine)()
        Base.metadata.create_all(self.engine)
