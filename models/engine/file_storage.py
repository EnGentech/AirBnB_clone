#!/usr/bin/python3
"""please comment for us"""

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key_dict = obj.__class__.__name__+"."+obj.id
        self.__objects.update({key_dict: obj})

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as sve:
            temp_dict = {}
            for keys, value in self.__objects.items():
                temp_dict.update({keys: value.to_dict()})
            json.dump(temp_dict, sve)

    def reload(self):
        if not os.path.isfile(self.__file_path):
            pass
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
