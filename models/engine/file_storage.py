#!/usr/bin/python3
"""
This module defines the FileStorage
"""

import json


class FileStorage():
    """
    This class handles serialization to a JSON file
    and deserialization from a JSON file to instances

    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary of stored opjects
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """
        Returns a dictionary of classes
        """
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        
        return classes

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = self.classes()[class_name](**value)
        except FileNotFoundError:
            pass
