#!/usr/bin/python3
"""Engine linked to MySQL database"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class that connects to MySQl server"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor that creates a new instance"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                        user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary with the specified class"""
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = []
            for classname in classes:
                objs.extend(self.__session.query(classname).all())
        dict = {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs}
        return dict

    def new(self, obj):
        """Adds an object in the current session"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object in the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and starts the current session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the session"""
        self.__session.close()
