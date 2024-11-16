#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of classes for deserialization."""
        from models.base_model import BaseModel
        return {"BaseModel": BaseModel}

    def all(self):
        """Returns the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Sets a new object in the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the file exists.
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name = v["__class__"]
                    if class_name in self.classes():
                        self.__objects[k] = self.classes()[class_name](**v)
        except FileNotFoundError:
            pass
