#!/usr/bin/python3
""" Contains unittests for FileStorage class """
import unittest
import os
from models import storage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    """ Tests FileStorage class """

    def test_all(self):
        """ Tests all method """
        # create storage instance and instance of BaseModel

        obj = BaseModel()
        __objects = storage.all()
        # test that storage.all() returns dictionary
        self.assertIsInstance(__objects, dict)
        # test that BaseModel instance in dictionary of objects
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(key, __objects)
        # test that the value in dictionary is of same type and equal to obj
        self.assertEqual(obj, __objects[key])
        self.assertIsInstance(__objects[key], BaseModel)

    def test_new(self):
        """ Tests new method """
        # create storage instance and instance of BaseModel
        obj = BaseModel()
        # create dictionary to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "1995-2-2T10:23:35.123450"
        new_dict["updated_at"] = "1999-1-4T7:15:05.543210"
        # create instance with **kwargs and test that object is not in __objects
        obj2 = BaseModel(**new_dict)
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        self.assertNotIn(key, storage.all())
        # obj2 is reset to new instance of BaseModel and
        # should be added to dictionary with new
        obj2 = BaseModel()
        key = "{}.{}".format(type(obj2).__name__, obj2.id)
        __objects = storage.all()
        self.assertIn(key, __objects)
        self.assertEqual(obj2, __objects[key])

    def test_save(self):
        """ Tests save method """
        # storage = FileStorage()
        file = "file.json"
        # Remove file if it exists
        if os.path.exists(file):
            os.remove(file)
        # Test if save creates the file
        storage.save()
        self.assertTrue(os.path.exists(file))
        # Overwrite created file
        with open(file, 'w') as f:
            f.write("Placeholder")
        # Check if save overwrites existing files
        with open(file, 'r') as f:
            content = f.read()
            storage.save()
            new_content = f.read()
        self.assertNotEqual(content, new_content)

    def test_reload(self):
        """ Tests reload method """

        from json import dumps

        # Check if reloading without doing anything reloads the same thing
        old_dict = storage.all()
        storage.reload()
        new_dict = storage.all()
        self.assertEqual(old_dict.keys(), new_dict.keys())

        # Make new object and a dictionary for that object
        obj = BaseModel()
        obj.id = 1
        dict_dict = {"BaseModel.1": obj.to_dict()}
        obje_dict = {"BaseModel.1": obj}

        # Overwrite file.json so that it includes just this dictionary
        if os.path.exists("file.json"):
            os.remove("file.json")
        with open("file.json", 'w') as f:
            f.write(dumps(dict_dict))

        # Reload
        storage.reload()
        self.assertNotEqual(storage.all().keys(), obje_dict.keys())
