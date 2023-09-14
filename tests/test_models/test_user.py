#!/usr/bin/python3
"""Unit test for User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_class(self):
        """Tests the class of an instance of User"""
        user = User()
        self.assertEqual(user.__class__.__name__, "User")

    def test_user_attributes(self):
        """Tests the initialization of attributes in User instance"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    if __name__ == '__main__':
        unittest.main()
