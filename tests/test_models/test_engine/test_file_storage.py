#!/usr/bin/python3
import os
import unittest
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
""" testing the file storage"""


class TestCaseFileStorage(unittest.TestCase):
    """ class for test cases """

   def test_pep8_Filestorage(self):
       """tests pep8"""
       style = pep8.StyleGuide(quite=True)
       p = style.check_files(['models/engine/file_storage.py'])
       self.assertEqual(p.total_errors, 0, "check pep8")
       
    def setUp(self):
        """ setting up the various
            components for the test """
        self.dir_path = 'file.json'
        self.my_model = FileStorage()

    def tearDown(self):
        """ dispose json file """
        if path.exists(self.dir_path):
            os.remove(self.dir_path)

    def test_all(self):
        """ check type return by all function """
        self.assertEqual(type(self.my_model.all()), dict)

    def test_new(self):
        test_model = BaseModel()
        self.my_model.new(test_model)
        len_dict = len(self.my_model.all())
        self.assertGreater(len_dict, 0)

    def test_save(self):
        """ save content to file
         and create if not exist"""
        self.my_model.save()
        self.assertEqual(path.exists(self.dir_path), True)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + cy.id, objs)
        self.assertIn("Amenity." + am.id, objs)
        self.assertIn("Review." + rv.id, objs)

    def test_reload_no_file(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)
