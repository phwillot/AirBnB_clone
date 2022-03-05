#!/usr/bin/python3
"""FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances:"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


class FileStorage:
    """class FileStorage:
    serializes instance to a JSON file and deserializes
    JSON file to instances"""

    def __init__(self):
        """initialization of the instance"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """serializes __objects to JSON file"""
        dict_json = {}
        for key in self.__objects.keys():
            dict_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(dict_json, file, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r+") as file:
                dictJson = json.load(file)
                for key, value in dictJson.items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except Exception as e:
            pass
