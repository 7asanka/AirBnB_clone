#!/usr/bin/python3
"""
this module defines the base_model class
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    the BaseModel class

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): The datetime instance was created.
        updated_at (datetime): The datetime instance was last updated.

    Methods:
        save(): Updates the 'updated_at' attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "crated_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the updated_at attribute to the current datetime
        """
        storage.save()
        updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance

        Returns:
            dict: Dictionary representation of the instance
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
