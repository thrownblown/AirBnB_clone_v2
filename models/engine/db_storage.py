#!/usr/bin/python3
"""SQLAlchemy storage module
"""

import sqlalchemy, json, os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __engine = None
    __session = None

    def __init__(self):
        """the init method
        """
        user = os.getenv('HBNB_MYSQL_USER', "hbnb_dev")
        passwd = os.getenv('HBNB_MYSQL_PWD', "hbnb_dev_pwd")
        host = os.getenv('HBNB_MYSQL_HOST', "localhost")
        database = os.getenv('HBNB_MYSQL_DB', "hbnb_dev_db")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user,
            passwd,
            host,
            database), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if os.getenv('HBNB_ENV') == 'test':
            meta = MetaData()
            meta.drop_all()

    def all(self, cls=None):
        """returns a dictionary
        Keyword Args:
            cls: the class to filter
        Return:
            returns a dictionary of __object
        """
        filtered = {}
        if cls:
            for k, v in self.__objects.items():
                if type(v) == cls:
                    filtered[k] = v
            return filtered
        return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an object
        Keyword Args:
            obj: given object to be deleted
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()
