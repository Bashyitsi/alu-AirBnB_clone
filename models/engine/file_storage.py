#!/usr/bin/python3
import json
from os import path


class FileStorage:
    """The file storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns : dictionary """
        return self.__objects

    def new(self, obj):
        """ Setting object with key """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes to json file """
        temp = {}
        for key in self.__objects:
            temp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+", encoding='utf-8') as out_file:
            json.dump(temp, out_file)

    def reload(self):
        """ deserializes json to file """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as in_file:
                dataset = json.load(in_file)
                for data in dataset.values():
                    name_of_class = data['__class__']
                    self.new(eval(name_of_class + "(**" + str(data) + ")"))
