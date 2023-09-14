#!/usr/bin/python3
"""The Class of a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User details"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """def __init__(self, *args, **kwargs):
        Initialize a User instance
        super().__init__(*args, **kwargs)"""
