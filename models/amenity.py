#!/usr/bin/python3
"""This Amedity class inherit from the Basemodels"""

from models import BaseModel


class Amenity(BaseModel):
    """Class of Amedity"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
