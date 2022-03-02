#!/usr/bin/python3
"""Base class that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initilization of the instance of the class"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key != 'created_at' and key != 'updated_at':
                        setattr(self, key, val)
                    else:
                        setattr(self, key, datetime.fromisoformat(val))

    def __str__(self):
        """Change the representation of the object"""
        # [<class name>] (<self.id>) <self.__dict__>
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary["created_at"].isoformat()
        dictionary['updated_at'] = dictionary["updated_at"].isoformat()
        return dictionary
