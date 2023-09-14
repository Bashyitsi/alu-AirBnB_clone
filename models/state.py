#!/usr/bin/python3
"""Then Class State that inherits from the BaseModel"""

from models import BaseModel


class State(BaseModel):
    """The State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
