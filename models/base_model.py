#!/usr/bin/python3
"""
This module defines the BaseModel class
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel class defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to the current datetime and saves to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance's __dict__,
        with `created_at` and `updated_at` as ISO-formatted strings.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
