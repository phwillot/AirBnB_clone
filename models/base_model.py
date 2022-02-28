#!/usr/bin/python3
"""Base class that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initilization of the instance of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Change the representation of the object"""
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of 
        __dict__ of the instance"""
        createdISO = datetime.isoformat(self.created_at)
        updatedISO = datetime.isoformat(self.updated_at)
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] =  createdISO
        self.__dict__["updated_at"] = updatedISO
        return self.__dict__
